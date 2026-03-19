class Solution:
    def search(self, arr: List[int], target: int) -> int:
        # Initialize left and right pointers for binary search
        left = 0
        right = len(arr)-1
        
        # Edge case: single element array
        if len(arr)==1 and arr[0]==target:
            return 0
        elif len(arr)==1 and arr[0]!=target:
            return -1
        else:
            # Binary search on rotated sorted array
            while left<=right:
                mid = (left+right)//2
                
                # Check if middle element is the target
                if arr[mid]==target:
                    return mid
                
                # Find the sorted part of the array
                # If left to mid is sorted
                elif arr[left]<=arr[mid]:
                    # Check if target is in the sorted left half
                    if arr[left]<=target<arr[mid]:
                        right = mid-1  # Search in left half
                    else:
                        left = mid+1   # Search in right half
                # If right to mid is sorted
                else:
                    # Check if target is in the sorted right half
                    if arr[mid]<target<=arr[right]:
                        left = mid+1   # Search in right half
                    else:
                        right = mid-1  # Search in left half
        
        # Target not found
        return -1
