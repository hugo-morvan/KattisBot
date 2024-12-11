from collections import defaultdict

def main():
    n = int(input())
    course_combinations = defaultdict(int)
    
    for _ in range(n):
        courses = sorted(map(int, input().split()))
        course_combinations[tuple(courses)] += 1
    
    max_popularity = max(course_combinations.values())
    most_popular_students = sum(1 for count in course_combinations.values() if count == max_popularity)
    
    print(most_popular_students)

if __name__ == "__main__":
    main()