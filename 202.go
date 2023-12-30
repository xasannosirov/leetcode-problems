func degreeSum(m int) int {
	powersum := 0
	for ; m > 0; m /= 10 {
		powersum += (m % 10) * (m % 10)
	}
	return powersum
}

func isHappy(n int) bool {
	if n == 1 || n == 7{
		return true
	} else if n < 10{
		return false
	} else {
		return isHappy(degreeSum(n))
    }
}
