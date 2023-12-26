func climbStairs(n int) int {
    dp1, dp2 := 1, 1
    for i := 2; i <= n; i++ {
        dp2, dp1 = dp1+dp2, dp2
    }
    return dp2
}
