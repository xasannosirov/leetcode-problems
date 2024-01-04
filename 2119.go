func stringReverse(num string) string {
    rns := []rune(num)
    for i, j := 0, len(rns)-1; i < j; i, j = i+1, j-1 {  
        rns[i], rns[j] = rns[j], rns[i] 
    } 
    return string(rns) 
}

func intReverse(num int) int {
	res := 0
	for num > 0 {
		remainder := num % 10
		res = (res * 10) + remainder
		num /= 10
	}
	return res
}

func isSameAfterReversals(num int) bool {
	reversed1 := strconv.Itoa(intReverse(num))
	reversed2, _ := strconv.Atoi(stringReverse(reversed1))
	return reversed2 == num
}
