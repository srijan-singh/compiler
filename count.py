digit = {'0','1','2','3','4','5','6','7','8','9'}

vowel = {'a','e','i','o','u'}

special_char = {"@","!","*","%","&"}

s = "ab@*122"

digit_count = 0
vowel_count = 0
special_char_count = 0
consonant_count = 0

for element in s:
    if element in digit:
        digit_count+=1

    elif element in vowel:
        vowel_count+=1

    elif element in special_char:
        special_char_count+=1

    else:
        consonant_count+=1


print("Digit Count: ",digit_count)
print("Vowel Count: ",vowel_count)
print("Special Char Count: ",special_char_count)
print("Consonant Count: ",consonant_count,)