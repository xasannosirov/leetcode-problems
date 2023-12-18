func findTheDifference(s string, t string) byte {
	var check int
	for _, i := range t {
		check = check + int(i)
	}
	for _, i := range s {
		check = check - int(i)
	}
	check = int(math.Abs(float64(check)))
	return byte(check)
}
