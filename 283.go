func moveZeroes(nums []int) {
	newIndex := 0

	for index := range nums {
		if nums[index] != 0 {
			nums[newIndex] = nums[index]
			newIndex++
		}
	}
	for ; newIndex < len(nums); newIndex++ {
		nums[newIndex] = 0
	}
	return
}
