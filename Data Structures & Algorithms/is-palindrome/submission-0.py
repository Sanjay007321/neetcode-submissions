class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_str = "".join(char.lower() for char in s if char.isalnum())
        
        # Check if the cleaned string reads the same forward and backward
        return cleaned_str == cleaned_str[::-1]