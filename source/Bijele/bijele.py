def main():
    # Read input
    input_data = list(map(int, input().split()))
    
    # Initialize the required number of each piece
    required_kings = 1
    required_queens = 1
    required_rooks = 2
    required_bishops = 2
    required_knights = 2
    required_pawns = 8
    
    # Calculate the difference for each piece
    kings_diff = required_kings - input_data[0]
    queens_diff = required_queens - input_data[1]
    rooks_diff = required_rooks - input_data[2]
    bishops_diff = required_bishops - input_data[3]
    knights_diff = required_knights - input_data[4]
    pawns_diff = required_pawns - input_data[5]
    
    # Output the differences
    print(kings_diff, queens_diff, rooks_diff, bishops_diff, knights_diff, pawns_diff)

if __name__ == "__main__":
    main()