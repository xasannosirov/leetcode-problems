func findWordsContaining(words []string, x byte) []int {
	var temp []int
	for index, value := range words {
		if strings.Contains(value, string(x)) {
			temp = append(temp, index)
		}
	}
	return temp
}
