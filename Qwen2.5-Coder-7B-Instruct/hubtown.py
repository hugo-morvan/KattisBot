import math

def main():
    n, m = map(int, input().split())
    
    citizens = []
    for _ in range(n):
        x, y = map(int, input().split())
        citizens.append((x, y))
    
    trains = []
    for i in range(m):
        x, y, c = map(int, input().split())
        trains.append(((x, y), c))
    
    def angle(citizen, train):
        dx, dy = citizen[0] - train[0], citizen[1] - train[1]
        return math.atan2(dy, dx)
    
    max_citizens = 0
    assignments = []
    
    for i in range(n):
        best_train = -1
        min_angle_diff = float('inf')
        
        for j in range(m):
            train_angle = angle(citizens[i], trains[j][0])
            if train_angle < 0:
                train_angle += 2 * math.pi
            
            diff = abs(train_angle - angle((0, 0), trains[j][0]))
            if diff > math.pi:
                diff = 2 * math.pi - diff
            
            if diff < min_angle_diff or (diff == min_angle_diff and best_train == -1):
                min_angle_diff = diff
                best_train = j
        
        if trains[best_train][1] > 0:
            assignments.append((i, best_train))
            trains[best_train] = ((trains[best_train][0]), trains[best_train][1] - 1)
    
    max_citizens = len(assignments)
    print(max_citizens)
    
    for assignment in assignments:
        print(assignment[0], assignment[1])

if __name__ == "__main__":
    main()
# Generator time: 11.7000 seconds