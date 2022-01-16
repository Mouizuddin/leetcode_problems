'''         28. Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string.
This is consistent to C's strstr() and Java's indexOf().

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Example 3:
Input: haystack = "", needle = ""
Output: 0
'''
# Solution :
# trick : this can be solved by using the string .find() -> method

def solution(haystack: str, needle: str) -> int:
    return haystack.find(needle)
'''
The find() method finds the first occurrence of the specified value.
The find() method returns -1 if the value is not found.
'''
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
print(solution('aaaaa',"bba")) # Output: -1
