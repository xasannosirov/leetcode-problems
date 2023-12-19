func romanToInt(s string) int {
	roman_values := map[string]int{
		"I":1,
		"V":5,
		"X":10,
		"L":50,
		"C":100,
		"D":500,
		"M":1000,
	}
	decimal := 0
	for i, _ := range s {
		if i < len(s)-1 && roman_values[string(s[i])] < roman_values[string(s[i+1])] {
			decimal -= roman_values[string(s[i])]
		} else {
			decimal += roman_values[string(s[i])]
		}
	}
	return decimal
}
