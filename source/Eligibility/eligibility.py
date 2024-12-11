def is_eligible(name, start_date, birth_date, courses):
    from datetime import datetime
    
    # Convert dates to datetime objects
    start_date = datetime.strptime(start_date, '%Y/%m/%d')
    birth_date = datetime.strptime(birth_date, '%Y/%m/%d')
    
    # Calculate age based on birth date
    age = datetime.now().year - birth_date.year - ((datetime.now().month, datetime.now().day) < (birth_date.month, birth_date.day))
    
    # Check basic requirements
    if start_date <= datetime(2010, 12, 31) or age >= 18:
        return "eligible"
    
    # Check if completed more than 8 semesters of full-time study
    if courses > 40:
        return "ineligible"
    
    # Coach petition
    return "coach petitions"

# Read input
num_cases = int(input())
for _ in range(num_cases):
    name, start_date, birth_date, courses = input().split()
    result = is_eligible(name, start_date, birth_date, int(courses))
    print(f"{name} {result}")