func isPowerOfFour(n int) bool {
    for n > 0 && n % 4 == 0 {
        n /= 4
    }
    return n == 1
}
