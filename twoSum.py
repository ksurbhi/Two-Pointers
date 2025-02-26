class Solution:
    # Using two Pointer
    # Time: O(n), Space O(1
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # using 2 Pointers
        start = 0
        end = len(numbers)-1
        while start <= end:
            sum = numbers[start] + numbers[end]
            if sum == target:
                return [start+1, end+1]
            elif sum < target:
                start += 1
            else:
                end -= 1


class Solution:
    # using Hashmap
    # Time: O(n), Space: O(n)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Using Hashmap
        # my_dict = {}
        # for i  in range(len(numbers)):
        #     diff = target - numbers[i] 
        #     if diff in my_dict:
        #         return[my_dict[diff],i+1]
        #     my_dict[numbers[i]] = i + 1 
        
            
        
