def average(salary: list[int]) -> float:
    salary.sort()
    n = len(salary)
    return sum(salary[1:n-1])/(n-2)
