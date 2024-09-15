'''
Consider the string str1 containing only lowercase letters, return the string with the same letters in uppercase.

Example 1:
Input: str1 = "Source, screen and assess leading ML developers & data Scientists"
Output: SOURCE, SCREEN AND ASSESS LEADING ML DEVELOPERS & DATA SCIENTISTS

Example 2:
Input: str1 = "Boost your AI/ML skills and get hired"
Output: BOOST YOUR AI/ML SKILLS AND GET HIRED
'''

class Solution:
   def to_upper(self, str1):
       return str1.upper()
       
sol = Solution()
# str1 = "Source, screen and assess leading ML developers & data Scientists"
print(sol.to_upper(str1))
