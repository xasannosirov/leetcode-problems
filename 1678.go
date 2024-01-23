func interpret(command string) string {
	temp := strings.ReplaceAll(command, "()", "o")
	temp = strings.ReplaceAll(temp, "(", "")
	temp = strings.ReplaceAll(temp, ")", "")
	return temp
}
