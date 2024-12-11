import sys

def main():
    # Read input
    N = int(input())
    commands = [input().strip() for _ in range(N)]
    
    # Process each command
    for command in commands:
        if command.startswith("Simon says"):
            # Output the rest of the command
            print(command.split("Simon says ", 1)[1])

if __name__ == "__main__":
    main()