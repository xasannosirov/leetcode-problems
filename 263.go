func isUgly(n int) bool {
    switch {
	case n <= 0:
		return false
	case n == 1:
		return true
	case n % 2 == 0:
		return isUgly(n/2)
	case n % 3 == 0:
		return isUgly(n/3)
	case n % 5 == 0:
		return isUgly(n/5)
	default:
		return false
	}
}
