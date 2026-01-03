def find_missing_number(nums: list, n: int) -> int:
    """Finds the missing number in a list of integers ranging from 1 to n.

    Args:
        nums (list): A list of integers from 1 to n with one number missing.
        n (int): The number n describing the range
    Returns:
        int: The missing number in the list.
    """
    
    
    # using set difference
    return (set(range(1,n+1)) - set(nums)).pop() 
    
    # using sum difference
    # return sum(range(1,n+1)) - sum(set(nums)) 
    

# #Another Method
# def find_missing_number(nums: list, n: int) -> int:
#     """Finds the missing number in a list of integers ranging from 1 to n.

#     Args:
#         nums (list): A list of integers from 1 to n with one number missing.
#         n (int): The number n describing the range
#     Returns:
#         int: The missing number in the list.
#     """
#     # for i in range(1,n+1,):
#     #     if i not in nums:
#     #         return i
#     #         break
    
#     #method 2
#     l=list(set(nums))  #list of unique elements
#     return n*(n+1)//2 - sum(l)
        
#   Find missing number in a range of numbers
# Given a list with numbers from 1 to n (inclusive) except one number in the range, write a function to find the missing number.

# Assume that only one number from the range will be missing in the given list.

# Example

# Given the inputs nums=[1, 4, 2, 4, 6, 5, 6] and n is 6.

# The number 3 is missing from the range. So, find_missing_number(nums) should return 3 as it is the missing number.  

