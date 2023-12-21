func divide(dividend int, divisor int) int {
	if dividend < 0 && divisor == -1 && dividend != -1 {
		return (dividend * -1)-1
	}
	return dividend / divisor
}
