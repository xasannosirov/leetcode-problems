func maxCoins(piles []int) int {
	sort.Ints(piles)
	res, n := 0, len(piles)
    
	for i := n - 2; i >= n/3; i -= 2 {
		res += piles[i]
	}

	return res
}
