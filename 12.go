func intToRoman(num int) string {
	roman_ints := []int{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1}
	roman_strs := []string{"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"}
	roman := ""
	for ind, value := range roman_ints {
		for num >= value{
			roman += roman_strs[ind]
			num -= value
		}
	}
	return roman
}
