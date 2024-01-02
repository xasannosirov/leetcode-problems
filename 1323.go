func maximum69Number (num int) int {
	temp := strconv.Itoa(num)
	res := ""
	check := false
	for _, str := range temp {
		if check == false && str == '6' {
			res += "9"
			check = true
		} else {
			res += string(str)
		}
	}
	resu, _ := strconv.Atoi(res)
	return resu
}
