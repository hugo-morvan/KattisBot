def check_pangram(phrase):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    used_letters = set()
    
    for char in phrase.lower():
        if char.isalpha():
            used_letters.add(char)
    
    missing_letters = alphabet - used_letters
    
    if not missing_letters:
        return "pangram"
    else:
        return f"missing {''.join(sorted(missing_letters))}"

def main():
    N = int(input())
    results = []
    
    for _ in range(N):
        phrase = input()
        results.append(check_pangram(phrase))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()