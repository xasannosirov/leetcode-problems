func getConcatenation(nums []int) []int {
  res := []int{}
  res = append(res, nums...)
  res = append(res, nums...)
  return res
}
