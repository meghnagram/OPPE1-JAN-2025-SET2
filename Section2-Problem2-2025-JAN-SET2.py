

from collections import Counter
nums = [int(input()) for i in range(int(input()))]

value_counts = dict(Counter(nums))
max_frequency = max(value_counts.values())

most_common_values = sorted([
    value 
    for value, count in value_counts.items() 
    if count == max_frequency
])

print(most_common_values)

# #Another Method

# # Write your code here to read the input and print the output

# n=int(input())
# l=[]
# s=[]
# for i in range(n):
#     l.append(int(input()))
    
# s=list(set(l))
# d={}
# for i in s:
#     d[i]=0
    
# for i in l:
#     d[i]=d[i]+1

# max=0
# for k,v in d.items():
#     if v>max:
#         max=v 
# final=[]       
# for k,v in d.items():
#     if v==max:
#         final.append(k)

# final.sort()        


# print(final)

# Most Frequent Numbers form the input
# Write a program to find the most frequent numbers from the given numbers in the input. The most frequent values should be printed in ascending order.

# NOTE: This is an I/O type question, you need to write the whole code for taking input and printing the output.

# Input Format

# The first line contains an integer n
# The next n lines each contain n numbers.
# Output Format

# A single list containing the most frequent numbers sorted in ascending order.
# Example

# Input

# 10
# 3
# 5
# 3
# 2
# 5
# 8 
# 3
# 8 
# 5
# 0
# Output

# [3, 5]
# Explanation

# First line contains the number of inputs 10. And the input has 10 more numbers. From the numbers 3 and 5 occurs thrice in the list which is the maximum number of times any number is repeated.

# Thus the output is [3, 5] which is printed as a list.

        
