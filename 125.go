func chekcPalindrome(s string) bool {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		if runes[i] != runes[j] {
			return false
		}
	}
	return true
}

func isPalindrome(s string) bool {
	res := ""
	for i := 0; i < len(s); i++ {
		if unicode.IsLetter(rune(s[i])) == true || unicode.IsDigit(rune(s[i])) {
			res += strings.ToLower(string(s[i]))
		}
	}
	fmt.Println(res)
	return chekcPalindrome(res)
}
