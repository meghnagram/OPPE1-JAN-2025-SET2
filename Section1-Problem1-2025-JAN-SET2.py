def is_both_divisible_by(a: int, b: int, c: int) -> bool:
    """
    Checks if the integer `c` divides both integers `a` and `b`.

    Args:
        a (int): The first integer.
        b (int): The second integer.
        c (int): The divisor (assumed to be non-zero).

    Returns:
        bool: True if `c` divides both `a` and `b`, False otherwise.
    """
    
    return a % c == 0 and b % c == 0

# #Another Method:

# def is_both_divisible_by(a: int, b: int, c: int) -> bool:
#     if a%c==0 and b%c==0:
#         return True
#     else:
#         return False

# Check If a number divides two other numbers
# Write a function is_both_divisible_by that takes three integers a, b and c as input and checks if a and b numbers are divisible by c. Assume that c number is non-zero.

# Example

# >>>is_both_divisible_by(10, 15, 5) # both 10 and 15 are divisible by 5
# True
# >>>is_both_divisible_by(10, 13, 5) # 13 is not divisible by 5
# False
# >>>is_both_divisible_by(19, 15, 5) # 19 is not divisible by 5
# False
