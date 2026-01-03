def merge_dictionaries(d1:dict, d2:dict):
    """
    Merges two dictionaries by summing values of common keys.

    If a key exists in both `d1` and `d2`, their values are summed.
    Keys that are unique to one dictionary are included as-is in the result.

    Args:
        d1 (dict): The first dictionary, where values are integers or floats.
        d2 (dict): The second dictionary, where values are integers or floats.

    Returns:
        dict: A new dictionary containing all keys from both `d1` and `d2`.
        Values for overlapping keys are summed, while unique keys retain their original values.

    """
    
   
    merged_dict = d1.copy()
    for key, value in d2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value
    return merged_dict

# #Another method

# def merge_dictionaries(d1:dict, d2:dict):
    
#     d={}
#     d=dict(d1)
#     for key in d2:
#         if key not in d1.keys():
#             d[key]=d2[key]
#         else:
#             d[key]=d1[key]+d2[key]
#     return(d)
# Merge two dictionaries and sum on conflicts
# Write a program to merge two dictionaries. If a key is present in both dictionaries, sum the values.

# Assume the values are numbers(int or float).

# Example

# >>> d1 = {'a': 1, 'b': 2}
# >>> d2 = {'b': 3, 'c': 4}
# >>> merge_dictionaries(d1, d2), 
# {'a': 1, 'b': 5, 'c': 4}    
   

