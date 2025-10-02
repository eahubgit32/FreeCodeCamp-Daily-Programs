def to_binary(decimal):

    if decimal == 0:
        return "0"
        
    remainders = [] 

    while decimal > 0:

        remainders.append(str(decimal % 2))

        decimal = decimal // 2

    return "".join(reversed(remainders))

print(to_binary(5))
