from collections import defaultdict

def main():
    n = int(input())
    birthdays = defaultdict(int)
    
    for _ in range(n):
        name, like, bday = input().split()
        birthdays[name] = (int(like), bday)
    
    # Sort friends by (like, bday) and then by name
    sorted_friends = sorted(birthdays.items(), key=lambda x: (-x[1][0], x[0]))
    
    # Collect friends who will be remembered
    remembered_friends = [name for _, (like, bday) in sorted_friends if like == max(like for _, (_, bday) in sorted_friends)]
    
    # Print the number of remembered friends
    print(len(remembered_friends))
    
    # Print the names of the remembered friends in lexicographical order
    for friend in remembered_friends:
        print(friend)

if __name__ == "__main__":
    main()