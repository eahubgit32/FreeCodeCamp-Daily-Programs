def digits_or_letters(s):


    digit_count = 0
    letter_count = 0

    for char in s:
        if char.isdigit():
            digit_count +=1 
        elif char.isalpha():
            letter_count += 1

    if digit_count > letter_count: return "digits"
    elif letter_count > digit_count: return "letters"
    else: return "tie"

    return s


print(digits_or_letters("abc123"))
