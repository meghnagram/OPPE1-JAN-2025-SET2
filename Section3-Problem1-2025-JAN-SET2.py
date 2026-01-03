def employees_with_salary_above(employees:list, min_salary:int):
    """Returns the employees names with salary greater than are equal to the given salary.
    
    Args:
        employees (list[dict]):
            list of dictionary of employees with 
            the keys name, salary and department.
        min_salary (int): The cutoff salary.

    Returns:
        list[str]: 
            list of names of the employees with salary 
            greater than or equal to the cutoff
            in the order of occurance.
    """
    
    
    return [
        employee['name']
        for employee in employees
        if employee['salary'] >= min_salary
    ]
    

def total_salary_in_department(employees:list, department:str):
    """Returns the total salary of all the employees in the department.
    
    Args:
        employees (list[dict]):
            list of dictionary of employees with 
            the keys name, salary and department.
        department (str): The department to find the total salary.

    Returns:
        int: The total salary of the employees in the given department.
    """
    
    
    return sum(
        employee['salary']
        for employee in employees
        if employee['department'] == department
    )
    

def ceil_to_five_hundreds(num: int):
    """Given an integer, increase it to the next multiple of 500 if it is not a multiple of 500.

    Args:
        num (int): The number to increment.
    
    Returns:
        int: The number ceiled to the next five hundreds.

    Examples:
    >>> ceil_to_five_hundreds(24500)
    24500
    >>> ceil_to_five_hundreds(24600)
    25000
    >>> ceil_to_five_hundreds(24400)
    24500
    """
    
    
    remainder = num%500
    return num-remainder + bool(remainder)*500
    


def max_salary_after_increment_in_department(employees:list, department:str, inc_percent:int):
    """Returns the maximum salary in the given department after increment.
    
    The Maximum salary is incremented with the given percentage,
    rounded to the nearest integer and ceiled to the next five hundreds

    Rounding can be done using round function.
    
    Args:
        employees (list[dict]):
            list of dictionary of employees with 
            the keys name, salary and department.
        department (str): The department to find the maximum salary.
        inc_percent (int): Percentage of increment in the salary.

    Returns:
        int: 
            The maximum salary in the given department after increment 
            and ceiling it to the next five hundreds.
    """
    
    
    employees_in_dept = filter(lambda x: x['department'] == department, employees)
    max_salary = max(map(lambda x: x['salary'], employees_in_dept))
    max_salary_after_inc = round(max_salary * (1+inc_percent/100))
    return ceil_to_five_hundreds(max_salary_after_inc)


# #AnotherMethod:

# def employees_with_salary_above(employees:list, min_salary:int):
#     """Returns the employees names with salary greater than are equal to the given salary.
    
#     Args:
#         employees (list[dict]):
#             list of dictionary of employees with 
#             the keys name, salary and department.
#         min_salary (int): The cutoff salary.

#     Returns:
#         list[str]: 
#             list of names of the employees with salary 
#             greater than or equal to the cutoff
#             in the order of occurance.
#     """
#     l=[]
#     for i in employees:
#         if i['salary']>=min_salary:
#             l.append(i['name'])
#     return l
                
    

# def total_salary_in_department(employees:list, department:str):
#     """Returns the total salary of all the employees in the department.
    
#     Args:
#         employees (list[dict]):
#             list of dictionary of employees with 
#             the keys name, salary and department.
#         department (str): The department to find the total salary.

#     Returns:
#         int: The total salary of the employees in the given department.
#     """
#     sum=0
#     for i in employees:
#         if i['department']==department:
#             sum += i['salary']
#     return sum
    

# def ceil_to_five_hundreds(num: int):
#     """Given an integer, increase it to the next multiple of 500 if it is not a multiple of 500.

#     Args:
#         num (int): The number to increment.
    
#     Returns:
#         int: The number ceiled to the next five hundreds.

#     Examples:
#     >>> ceil_to_five_hundreds(24500)
#     24500
#     >>> ceil_to_five_hundreds(24600)
#     25000
#     >>> ceil_to_five_hundreds(24400)
#     24500
#     """
#     n=num//1000
#     r=num%1000
    
#     if 501<=r<=999:
#         return((n+1)*1000)
#     if 0<r<499:
#         return((n)*1000 +500)
#     if r==500 or r==0:
#         return num
        
    


# def max_salary_after_increment_in_department(employees:list, department:str, inc_percent:int):
#     """Returns the maximum salary in the given department after increment.
    
#     The Maximum salary is incremented with the given percentage,
#     rounded to the nearest integer and ceiled to the next five hundreds

#     Rounding can be done using round function.
    
#     Args:
#         employees (list[dict]):
#             list of dictionary of employees with 
#             the keys name, salary and department.
#         department (str): The department to find the maximum salary.
#         inc_percent (int): Percentage of increment in the salary.

#     Returns:
#         int: 
#             The maximum salary in the given department after increment 
#             and ceiling it to the next five hundreds.
#     """
    
#     max=0
#     for i in employees:
#         if i['department']==department and i['salary']>max :
#             max = i['salary']
    
#     newmax=round(max+max*inc_percent/100)
    
#     return ceil_to_five_hundreds(newmax)
    
# mployee Data Analysis
# A list of employee records as a list of dictionaries with keys name, department and salary. Implement the following functions.

# employees_with_salary_above(employees:list[dict], min_salary:int)->str - Returns the list of names of employees whose salary is greater than or equal to the given minimum salary
# total_salary_in_department(employees:list[dict], department: str)->int - Returns the total salary expense in the given department.
# ceil_to_five_hundreds(num:int)->int - Returns a number ceiled to the next five hundreds.
# max_salary_after_increment_in_department(employees:list[dict], department:str, inc_percent: int) -> int - Returns the maximum salary in the given department after increment with the given percentage and ceiling it to the next five hundreds


# Example

# employees = [
#     {'name': 'Alice', 'department': 'HR', 'salary': 50000},
#     {'name': 'Bob', 'department': 'Engineering', 'salary': 70000},
#     {'name': 'Charlie', 'department': 'HR', 'salary': 45000},
#     {'name': 'David', 'department': 'Engineering', 'salary': 60000},
#     {'name': 'Eve', 'department': 'Marketing', 'salary': 55000},
# ]
# print(employees_with_salary_above(employees, 60000)) # ['Bob','David']
# print(total_salary_in_department(employees, 'HR')) # 95000
# print(ceil_to_five_hundreds(25100)) # 25500
# print(max_salary_after_increment_in_department(employees, 'Engineering', 7)) # after increment 74900, after rounding 75000

