func minPartitions(n string) int {
    var temp byte = 0

    for i := 0; i < len(n); i++ {
        if n[i] > temp {
            temp = n[i]
        }
    }

    return int(temp - 48)
}
