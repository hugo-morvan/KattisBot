def main():
    cipher_text = input().upper()
    per_name = "PERPERPERPERPERPERPER"
    
    # Calculate the number of days needed
    days_needed = len(cipher_text) // 3
    
    print(days_needed)

if __name__ == "__main__":
    main()