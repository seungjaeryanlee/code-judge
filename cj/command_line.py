import importlib
import sys

import cj


def evaluate():
    filepath = sys.argv[1]
    folderpath, filename = '/'.join(filepath.split('/')[:-1]), '.'.join(filepath.split('/')[-1].split('.')[:-1])
    sys.path.insert(0, folderpath)

    solution_module = importlib.import_module(filename)
    solution_class = solution_module.Solution
    solution_instance = solution_class()
    solution_function = solution_instance.solution

    if solution_instance.problem_id == 'project_euler:1':
        print('Detected Project Euler Problem 1')
        try:
            answer = solution_function()
        except:
            print('[FAIL] An exception occurred.')
        else:
            if answer == 233168:
                print('[SUCCESS] Correct answer: 233168')
            else:
                print('[SUCCESS] The answer {} is incorrect'.format(answer))
    else:
        print('Problem ID not recognized')
