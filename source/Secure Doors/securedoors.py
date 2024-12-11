def audit_access_log():
    n = int(input())
    current_employees = set()
    
    for _ in range(n):
        action, name = input().split()
        
        if action == 'entry':
            if name in current_employees:
                print(f"{name} entered (ANOMALY)")
            else:
                print(f"{name} entered")
                current_employees.add(name)
        elif action == 'exit':
            if name in current_employees:
                print(f"{name} exited")
                current_employees.remove(name)
            else:
                print(f"{name} exited (ANOMALY)")

audit_access_log()