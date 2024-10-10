def calculate_minimum_changes_to_make_anagrams(s):
    if len(s) % 2 != 0:
        return -1
    
    # Split the string into two equal parts
    mid = len(s) // 2
    s1 = s[:mid]
    s2 = s[mid:]
    
    # Count the frequency of characters in each substring
    frequency_s1 = {}
    frequency_s2 = {}
    for char in s1:
        frequency_s1[char] = frequency_s1.get(char, 0) + 1
    for char in s2:
        frequency_s2[char] = frequency_s2.get(char, 0) + 1
    
    # Calculate the number of changes needed to make s1 and s2 anagrams
    minimum_changes = 0
    for char, count in frequency_s1.items():
        minimum_changes += max(count - frequency_s2.get(char, 0), 0)
    
    return minimum_changes
