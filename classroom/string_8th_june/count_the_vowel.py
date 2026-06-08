"""wap to input a sentence and display the frequency of vowels present in thet sentence ingroing the case"""
sentence = input("enter the sentence :")
vlowel = {}
for i in sentence:
    if i in "aeiouAEIOU":
        if i in vlowel:
            vlowel[i] += 1
        else:
            vlowel[i] = 1
print(vlowel)