func checkPowersOfThree(n int) bool {
    if n <= 0 {
		return false
	}
	for n > 0 {
		temp := n % 3
		if temp == 2 {
			return false
		}
		n = n / 3
	}
	return true
}
