func integerBreak(n int) int {
    if n == 2 {
        return 1
    }
    if n == 3 { 
        return 2
    }
    
    max := 1
    for n > 4 {
        max *= 3
        n -= 3
    }
    max *= n 
    return max
}
