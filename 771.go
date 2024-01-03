func numJewelsInStones(jewels string, stones string) int {
    count := 0

	for _, stone := range stones {
		if strings.Contains(jewels, string(stone)) {
			count = count + 1
		}
	}
    return count
}
