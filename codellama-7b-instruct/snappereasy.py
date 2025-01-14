#!/usr/bin/env python3

def get_state(snapper):
    if snapper % 2 == 0:
        return 'ON'
    else:
        return 'OFF'

for _ in range(int(input())):
    N, K = map(int, input().split())
    states = [get_state(i) for i in range(1, N+1)]
    for _ in range(K):
        states = [s if i % 2 == 0 else 'OFF' if s == 'ON' else 'ON' for i, s in enumerate(states[::-1], start=1)]
    print('Case #{}'.format(_+1), states[-1])
# Generator time: 5.9354 seconds