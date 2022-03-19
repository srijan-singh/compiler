# Set of digits
digit = {'0','1','2','3','4','5','6','7','8','9'}

# Set of vowels
vowel = {'a','e','i','o','u'}

# Set of special characters
special_char = {"@","!","*","%","&"}

# Input String
string = input()

digit_count = 0
vowel_count = 0
special_char_count = 0
consonant_count = 0

for element in string:
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