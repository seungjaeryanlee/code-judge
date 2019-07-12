"""Implement console scripts in setup.py."""
import importlib
import sys

def cj():
    """Check keyword and call appropriate method."""
    keyword = sys.argv[1]
    if keyword == 'judge':
        judge()
    elif keyword == 'show':
        show()

def judge():
    """Judge specified file."""
    filepath = sys.argv[2]
    folderpath, filename = '/'.join(filepath.split('/')[:-1]), '.'.join(filepath.split('/')[-1].split('.')[:-1])
    sys.path.insert(0, folderpath)

    solution_module = importlib.import_module(filename)
    solution_function = solution_module.solution

    if solution_function.problem_id == 'project_euler:1':
        print('Detected Project Euler Problem 1')
        try:
            answer = solution_function()
        except:
            print('[FAIL] An exception occurred.')
            print(sys.exc_info()[1])
        else:
            if answer == 233168:
                print('[SUCCESS] Correct answer: 233168')
            else:
                print('[SUCCESS] The answer {} is incorrect'.format(answer))
    else:
        print('Problem ID not recognized')


def show():
    """Print problem in command line."""
    problem_id = sys.argv[2]


    if problem_id == 'project_euler:1':
        print("")
        print("+---------------------------------------------------------------------+")
        print("|                               PROBLEM                               |")
        print("+---------------------------------------------------------------------+")
        print("If we list all the natural numbers below 10 that are multiples of 3 or ")
        print("5, we get 3, 5, 6 and 9. The sum of these multiples is 23.")
        print("")
        print("Find the sum of all the multiples of 3 or 5 below 1000.")
