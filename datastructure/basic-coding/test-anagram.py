def  calculate(s):
	if len(s)%2 !=0:
		return -1

	mid = len(s)//2
	s1 = s[:mid]
	s2 = s[mid:]
	freqency_of_char_s1 = {}
	freqency_of_char_s2 = {}

	for char in s1:
		freqency_s1[char] = freqency_of_char_s1.get(char, 0) + 1
	for char in s2:
		freqency_s2[char] = freqency_of_char_s2.get(char, 0) + 1
    
    minimum_chages = 0
    for char , count in freqency_s1.items():
    	minimum_chages +=max(count -freqency_s2(char, 0),0)
    return minimum_chages







if __name__ == "__main__":
	calculate("aAabab")