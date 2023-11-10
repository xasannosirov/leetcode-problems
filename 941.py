class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        max_num = max(arr)
        index_num = arr.index(max_num)
        for i in range(len(arr[:-1])):
            if arr[i] == arr[i+1]:
                return False

        if arr == sorted(arr) or arr == sorted(arr, reverse=True):
            return False
        if arr[:index_num+1] == sorted(arr[:index_num+1]) and arr[index_num+1:] == sorted(arr[index_num+1:], reverse=True):
            return True
        return False
