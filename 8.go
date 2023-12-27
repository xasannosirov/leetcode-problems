func myAtoi(s string) int {
	s = strings.TrimSpace(s)

	if len(s) == 0 {
		return 0
	}

	multiplier := 1
	if s[0] == '-' {
		multiplier = -1
		s = s[1:]
	} else if s[0] == '+' {
		s = s[1:]
	}

	num := 0
	for _, c := range s {
		if !unicode.IsDigit(c) {
			break
		}

		curr := int(c - '0')
		if num > math.MaxInt32/10 || (num == math.MaxInt32/10 && curr >= 7) {
			return math.MaxInt32
		}
		if num < math.MinInt32/10 || (num == math.MinInt32/10 && curr >= 8) {
			return math.MinInt32
		}

		num = num*10 + curr*multiplier
	}

	return num
}
