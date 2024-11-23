import sys
import torch
import subprocess
import platform
import os
def diagnose_gpu_issues():
    print("=== PyTorch GPU Diagnostic Report ===\n")
    
    # Check PyTorch version
    print(f"PyTorch Version: {torch.__version__}")
    
    # Check CUDA availability
    print(f"CUDA Available: {torch.cuda.is_available()}")
    
    # Check if CUDA version matches PyTorch build
    if hasattr(torch.version, 'cuda'):
        print(f"PyTorch CUDA Version: {torch.version.cuda}")
    
    # Check available GPUs
    if torch.cuda.is_available():
        print(f"Number of GPUs: {torch.cuda.device_count()}")
        for i in range(torch.cuda.device_count()):
            print(f"GPU {i}: {torch.cuda.get_device_name(i)}")
    
    # Check system CUDA installation
    try:
        nvidia_smi = subprocess.check_output(["nvidia-smi"], universal_newlines=True)
        print("\nNVIDIA-SMI Output:")
        print(nvidia_smi)
    except Exception as e:
        print("\nError running nvidia-smi:", str(e))
    
    # Check Python version
    print(f"\nPython Version: {sys.version}")
    
    # Check OS
    print(f"Operating System: {platform.platform()}")
    
    # Print CUDA_HOME environment variable
    print(f"CUDA_HOME: {os.environ.get('CUDA_HOME', 'Not Set')}")

if __name__ == "__main__":
    diagnose_gpu_issues()