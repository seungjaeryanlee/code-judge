def problem(problem_id):
    """Decorator for solution function to specify problem_id."""
    def deco(cls):
        cls.problem_id = problem_id
        return cls
    return deco
