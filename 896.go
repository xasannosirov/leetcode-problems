func monotoneIncrease(nums []int) bool {
	for i := 0; i < len(nums)-1; i++ {
		if !(nums[i] <= nums[i+1]) {
			return false
		}
	}
	return true
}

func monotoneDecrease(nums []int) bool {
	for i := 0; i < len(nums)-1; i++ {
		if !(nums[i] >= nums[i+1]) {
			return false
		}
	}
	return true
}

func isMonotonic(nums []int) bool {
	if monotoneDecrease(nums) {
		return true
	} else if monotoneIncrease(nums) {
		return true
	}
	return false
}
