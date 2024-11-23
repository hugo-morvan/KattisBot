#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solver import OptimizedQwenGenerator
from recommend import *
from submit import *
from utils import *
from autokattis import OpenKattis
from dotenv import load_dotenv
import time

def main():
    """ Main program """
    
    load_dotenv()
    user = os.getenv("USER")
    password = os.getenv("PASSWORD")
    print("Loading .env:", end=" ")
    test = os.getenv("TEST")
    print(test)
    
    generator = OptimizedQwenGenerator()
    
    while True:
        # Login (has to do it every time to update solved problems)
        # could try to do every 2 and solve reccomended problem [0] and [1]
        # Could try to use multiples cores to do the differents steps , but code generation is the bottelneck
        kt = OpenKattis(user, password)

        pid, file_path = get_problem(kt)
        description = get_description(kt, pid)
        print("Generating solution")
        solution = generator.generate_solution(description)
        code = extract_code(solution)
        print(f'Solution generated: \n')
        print(code)
        write_solution(file_path, code)
        print('solution written to file')
        submit_problem(file_path , pid)
        time.sleep(60) # Don't spam the kattis servers !
        
    return 0

if __name__ == "__main__":
    main()