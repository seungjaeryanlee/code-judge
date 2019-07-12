def hello_world():
    return 'Hello World!'

def problem(problem_id):
    def deco(cls):
        cls.problem_id = problem_id
        return cls
    return deco
