class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        
        while i < j:
            current_sum = numbers[i] + numbers[j]
            
            if current_sum == target:
                return [i+1, j+1]  # Note: Use [i + 1, j + 1] if LeetCode 167 asks for 1-indexed output
            elif current_sum < target:
                i += 1  # Sum is too small, move left pointer right
            else:
                j -= 1  # Sum is too large, move right pointer left
                
        return []