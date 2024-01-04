func findRelativeRanks(score []int) []string {
	res, other, temp := []string{}, []int{}, append([]int{}, score...)
	sort.Ints(temp)
	if len(temp) >= 3 {
		other = append([]int{}, temp[:len(temp)-3]...)
	}
	for i := 0; i < len(score); i++ {
		if score[i] == temp[len(temp)-1] {
			res = append(res, "Gold Medal")
		} else if score[i] == temp[len(temp)-2] {
			res = append(res, "Silver Medal")
		} else if score[i] == temp[len(temp)-3] {
			res = append(res, "Bronze Medal")
		} else {
			for j := 0; j < len(other); j++ {
				if other[j] == score[i] {
					res = append(res, strconv.Itoa(len(other)+3-j))
					break
				}
			}
		}
	}
	return res
}
