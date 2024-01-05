func removeDuplicates(nums []int) int {
  temp := 1
  for i := temp; i < len(nums); i ++ {
    if nums[temp-1] != nums[i]{
      nums[temp] = nums[i]
      temp++
    }
  }
  return temp
}
