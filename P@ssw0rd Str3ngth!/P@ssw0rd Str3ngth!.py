import re

def check_strength(password):

    score = 0
    
    if len(password) >= 8:
        score += 1

    if re.search(r'[a-z]', password) and re.search(r'[A-Z]', password):
        score += 1

    if re.search(r'\d', password):
        score += 1

    if re.search(r'[!@#$%^&*]', password):
        score += 1

    if score == 4:
        return "strong"
    elif score >= 2:
        return "medium"
    else:
        return "weak"


print(f"'123456' is {check_strength('123456')}")          
print(f"'pass!!!' is {check_strength('pass!!!')}")       
print(f"'Qwerty' is {check_strength('Qwerty')}")            
print(f"'PASSWORD' is {check_strength('PASSWORD')}")       
print(f"'PASSWORD!' is {check_strength('PASSWORD!')}")       
print(f"'PassWord%^!' is {check_strength('PassWord%^!')}") 
print(f"'qwerty12345' is {check_strength('qwerty12345')}")  
print(f"'S3cur3P@ssw0rd' is {check_strength('S3cur3P@ssw0rd')}") 
print(f"'C0d3&Fun!' is {check_strength('C0d3&Fun!')}")  
