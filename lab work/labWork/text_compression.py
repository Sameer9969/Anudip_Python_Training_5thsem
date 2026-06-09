"""
3 
Sample Output 
Original Text: 
AAABBBCCCDDDAAA 
 
Character Frequencies: 
A -> 6 
B -> 3 
C -> 3 
D -> 3 
 
Unique Characters: 
['A', 'B', 'C', 'D'] 
 
Most Frequent Character: A 
 
Compressed Output: 
A3B3C3D3A3 
 
Original Length: 15 
Compressed Length: 10 
 
Compression Ratio: 66.67%"""

#----------------------------------------------
# Text Compression Analyzer
#----------------------------------------------

text = "AAABBBCCCDDDAAA"

print("Original Text:")
print(text)

#----------------------------------------------
# 1. Count occurrences of each character
#----------------------------------------------

print("\nCharacter Occurrences:")

for ch in text:

    count = 0

    for char in text:

        if ch == char:
            count += 1

    print(ch, "->", count)

#----------------------------------------------
# 2. Create dictionary of character frequencies
#----------------------------------------------

frequency = {}

for ch in text:

    if ch in frequency:
        frequency[ch] += 1

    else:
        frequency[ch] = 1

print("\nCharacter Frequencies:")

for ch in frequency:
    print(ch, "->", frequency[ch])

#----------------------------------------------
# 3. Display unique characters
#----------------------------------------------

unique_chars = []

for ch in text:

    if ch not in unique_chars:
        unique_chars.append(ch)

print("\nUnique Characters:")
print(unique_chars)

#----------------------------------------------
# 4. Find most frequent character
#----------------------------------------------

max_char = ""
max_count = 0

for ch in frequency:

    if frequency[ch] > max_count:

        max_count = frequency[ch]
        max_char = ch

print("\nMost Frequent Character:", max_char)

#----------------------------------------------
# 5. Create compressed output
#----------------------------------------------

compressed = ""

count = 1

for i in range(1, len(text)):

    if text[i] == text[i - 1]:

        count += 1

    else:

        compressed += text[i - 1] + str(count)

        count = 1

# Add last group
compressed += text[-1] + str(count)

print("\nCompressed Output:")
print(compressed)

#----------------------------------------------
# 6. Calculate compression ratio
#----------------------------------------------

original_length = len(text)

compressed_length = len(compressed)

compression_ratio = (compressed_length / original_length) * 100

print("\nOriginal Length:", original_length)

print("Compressed Length:", compressed_length)

print("\nCompression Ratio:",
    round(compression_ratio, 2), "%")