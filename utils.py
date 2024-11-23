

def write_solution(file_path, solution):
    with open(file_path, 'w') as f: 
            f.write(solution)
            
def extract_code(text: str) -> str:
    # Find the first and last occurrence of ```
    start = text.find('```')
    if start == -1:
        return text  # Return original text if no triple backticks found
    
    # Find the second set of backticks
    end = text.find('```', start + 3)
    if end == -1:
        return text  # Return original text if closing backticks not found
    
    # Extract the code between the backticks
    # Skip any language identifier after the first backticks
    code_start = text.find('\n', start + 3)
    if code_start == -1 or code_start > end:
        return text  # Return original text if no newline found
        
    return text[code_start + 1:end].strip()
