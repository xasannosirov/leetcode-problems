func generate(numRows int) [][]int {
	res := [][]int{}
	
	if numRows == 1{
		return append(res, []int{1})
	} else if numRows == 2 {
		return append(res, []int{1}, []int{1,1})
	}

	res = append(res, []int{1}, []int{1,1}, []int{1,2,1})
	check := []int{1,2,1}

    for i := 2; i < numRows-1; i++ {
		k, l := 0, 1
		new := []int{1}
		for j := 0; j < i; j++{
			new = append(new, check[k]+check[l])
			k,l = k+1, l+1
		} 
		new = append(new, 1)
		res = append(res, new)
		check = new
	}

	return res
}
