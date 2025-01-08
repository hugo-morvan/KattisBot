def find_unrelated_position(n, names):
    unrelated_index = names.index('unrelated')
    return (unrelated_index + 1) % n

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    names = data[1:]
    
    unrelated_index = find_unrelated_position(n, names)
    unrelated_name = names[unrelated_index]
    
    # Move the unrelated person to the end of the list
    names.pop(unrelated_index)
    names.append(unrelated_name)
    
    # Print the names in the new order
    for name in names:
        print(name)

if __name__ == "__main__":
    main()
# Generator time: 22.6551 seconds