func twoSum(nums []int, target int) []int {
    if len(nums) == 2 && nums[0]+nums[1] == target {
        return []int{0, 1}
    }
    res := []int{}
    for i := 0; i < len(nums); i++ {
        for j := i + 1; j < len(nums); j++ {
            if nums[i]+nums[j] == target {
				return []int{i,j}
            }
        }
    }
    return res
}
