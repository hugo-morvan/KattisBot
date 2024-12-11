import sys

def main():
    input = sys.stdin.read
    data = input().split()
    
    # Parse input
    N = int(data[0])
    Q = int(data[1])
    positions = list(map(int, data[2:N+2]))
    
    # Process queries
    for _ in range(Q):
        query = data[2*N+2+_*3:2*N+2+(_+1)*3]
        if query[0] == '1':
            company_id = int(query[1]) - 1
            new_position = int(query[2])
            positions[company_id] = new_position
        else:
            company_a = int(query[1]) - 1
            company_b = int(query[2]) - 1
            distance = abs(positions[company_a] - positions[company_b])
            print(distance)

if __name__ == "__main__":
    main()