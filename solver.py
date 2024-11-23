########### Auto Solving stuff ########################
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from typing import Optional

class OptimizedQwenGenerator:
    def __init__(
        self,
        model_name: str = "Qwen/Qwen2.5-Coder-3B-Instruct",
        use_half_precision: bool = True
    ):
        # Initialize device
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        
        # Load model with optimizations
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float16 if use_half_precision and self.device == "cuda" else "auto",
            device_map="auto"
        )
        
        # Load tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        
        # Enable evaluation mode
        self.model.eval()
        
        # Cache for template
        self._system_message = {
            "role": "system", 
            "content": "You are Qwen, a highly skilled competitive python programmer. When given a prompt, you only output code. Your code should take in inputs using the input() function and return outputs using print()."
        }
        
        # Initialize CUDA graph variables if using GPU
        self.static_input_shape = None
        self.static_graph = None

    def generate_solution(self, description: str, max_new_tokens: int = 512) -> str:
        # Prepare messages
        messages = [
            self._system_message,
            {"role": "user", "content": description}
        ]
        
        # Apply template
        text = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )
        
        # Tokenize with optimization for GPU
        with torch.inference_mode():
            model_inputs = self.tokenizer([text], return_tensors="pt").to(self.device)
            
            # Use CUDA graphs for repeated operations with same input size
            if (self.device == "cuda" and 
                (self.static_input_shape is None or 
                 self.static_input_shape != model_inputs.input_ids.shape)):
                
                self.static_input_shape = model_inputs.input_ids.shape
                torch.cuda.empty_cache()
                
                # Generate with optimized settings
                generated_ids = self._generate_optimized(model_inputs, max_new_tokens)
            else:
                generated_ids = self._generate_optimized(model_inputs, max_new_tokens)
        
        # Post-process generated IDs
        generated_ids = [
            output_ids[len(input_ids):] 
            for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
        ]
        
        # Decode and clean up response
        response = self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
        return response  

    def _generate_optimized(self, model_inputs, max_new_tokens: int):
        '''
        If you need to adjust generation speed vs quality:

        Lower temperature (e.g., 0.5) for more focused output
        Lower max_new_tokens if you don't need long responses
        Adjust top_p (e.g., 0.8) for more deterministic output  
        '''
        return self.model.generate(
            **model_inputs,
            max_new_tokens=max_new_tokens,
            pad_token_id=self.tokenizer.pad_token_id,
            eos_token_id=self.tokenizer.eos_token_id,
            use_cache=True,
            num_beams=1,        # Disable beam search for faster generation
            do_sample=True,     # Enable sampling for more natural code
            temperature=0.5,    # Add some randomness while keeping output focused
            top_p=0.95,         # Nucleus sampling to maintain code quality
        )
