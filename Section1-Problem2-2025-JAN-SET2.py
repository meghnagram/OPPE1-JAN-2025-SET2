def is_rotation(str1: str, str2: str) -> bool:
    """
    Checks if one string is a rotation of another.

    Example:
      >>>is_rotation('abcde','cdeab')
      True
      >>>is_rotation('hello','ehllo')
      False
      >>>is_rotation('hello','helol')
      False

    Args:
        str1 (str): The original string.
        str2 (str): The string to check if it's a rotation of str1.

    Returns:
        bool: True if str2 is a rotation of str1, False otherwise.
    """
    
    return len(str1) == len(str2) and  str2 in 2*str1

# #Another Method:

# def is_rotation(str1: str, str2: str) -> bool:
                 
#     if len(str1) != len(str2):
#         return False
#     return str2 in (str1 + str1)


# Check String Rotation
# Write a function that checks if one string is a rotation of another.

# Hint: all the rotations of a particular string will be present in the string formed by concatenating it with itself.

# For example the rotations of the word apple can be formed by.

# a[pplea]pple - pplea
# ap[pleap]ple - pleap
# app[leapp]le - leapp
# appl[eappl]e - eappl
# apple[apple] - apple

# Example

# >>>is_rotation('abcde','cdeab')
# True
# >>>is_rotation('hello','ehllo')
# False
# >>>is_rotation('hello','helol')
# False
# Explanation

# Since cdeab is a rotation of abcde,
# So, is_rotation('abcde','cdeab') should return True
