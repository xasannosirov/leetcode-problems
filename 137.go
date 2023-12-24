func singleNumber(nums []int) int {
    for _, num := range nums {
        count := 0
        for _, n := range nums {
            if n == num {
                count++
            }
        }
        if count == 1 {
            return num
        }
    }
    return -1
}
