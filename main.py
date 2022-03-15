def is_digit(str_:str, i:int) -> bool:
    
    if (str_[i] == '0' or str_[i] == '1'or str_[i] == '2' or str_[i] == '3' or str_[i] == '4' or str_[i] == '5' or str_[i] == '6' or str_[i] == '7' or str_[i] == '8' or str_[i] == '9'):
        return True

    return False

def is_vowel(str_:str, i:int) -> bool:

    if (str_[i] == "a" or str_[i] == "e" or str_[i] == "i" or str_[i] == "o" or str_[i] == "u"):
        return True

    return False

def is_special_char(str_:str, i:int) -> bool:

    if (str_[i] == "~" or str_[i] == "!" or str_[i] == "@" or str_[i] == "#" or str_[i] == "$" or str_[i] == "%" or str_[i] == "^" or str_[i] == "&" or str_[i] == "*" or str_[i] == "?"):
        return True

    return False


# Main Function
if __name__ == "__main__":

    str_ = input("Please input the given string: ") 
    #str_ = str_.lower()

    digit_count = 0
    vowel_count = 0
    consonant_count = 0
    special_char_count = 0

    # Traversing through string
    for i in range(len(str_)):

        if(is_digit(str_, i)):
            digit_count+=1

        elif(is_vowel(str_, i)):
            vowel_count+=1

        elif(is_special_char(str_, i)):
            special_char_count+=1

        else:
            consonant_count+=1

    print("\nOutput\n")

    print("Digit count: ",digit_count)

    print("Vowel count: ",vowel_count)

    print("Consonat count: ",consonant_count)

    print("Special character count: ",special_char_count)

    print("\n")

    