"""
Given a string s, determine if it is a palindrome, considering only alphanumeric
 characters and ignoring cases.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.

Things to keep in mind:
How can you find only the alphanumeric characters?
How can you reverse a string?
How can you find the upper or lower case?
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        reversed_string = [i for i in s if i.isalnum()]
        reversed_string = reversed_string[::-1]
        original_string = [i for i in s if i.isalnum()]

        for i in range(0, len(reversed_string)):
            if reversed_string[i].lower() != original_string[i].lower():
                return False
        return True


string_1 = "A man, a plan, a canal: Panama"
string_2 = "race a car"
sol = Solution()
print(sol.isPalindrome(string_1))
print(sol.isPalindrome(string_2))