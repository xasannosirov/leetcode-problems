func generateMatrix(n int) [][]int {
    result := make([][]int, n)
    for i := range result {
        result[i] = make([]int, n)
    }
    son := n
    i, c, m := 0, 1, 0
    for i <= son/2 {
        j := m
        for j < son-m {
            result[i][j] = c
            c++
            j++
        }
        j = m + 1
        for j < son-m-1 {
            result[j][son-m-1] = c
            c++
            j++
        }
        j = son - m - 1
        for c <= son*son && j >= m {
            result[son-i-1][j] = c
            c++
            j--
        }
        j = son - m - 2
        for j > m {
            result[j][i] = c
            c++
            j--
        }
        i++
        m++
    }
    return result
}
