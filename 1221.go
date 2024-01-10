func balancedStringSplit(s string) int {
	count := 0

	leftCount, rightCount := 0, 0

	for i := 0; i < len(s); i++ {
		if s[i] == 'L' {
			leftCount++
		} else {
			rightCount++
		}

		if leftCount == rightCount {
			count++
			leftCount = 0
			rightCount = 0
		}
	}

	return count
}
