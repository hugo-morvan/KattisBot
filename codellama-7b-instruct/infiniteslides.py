def find_minimum(W):
    # Calculate the distance between the two slides.
    dist = (2 * W**2) / 3
    
    return dist

if __name__ == "__main__":
    # Get input from user
    W = float(input())
    print("The minimum Euclidean distance is: ", find_minimum(W))
# Generator time: 4.3738 seconds