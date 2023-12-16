func numIdenticalPairs(nums []int) int {
	var count int
	for ind, elem := range nums {
		for i := ind+1; i < len(nums); i++ {
			if elem == nums[i] {
				count ++
			}
		}
	}
	return count
}
