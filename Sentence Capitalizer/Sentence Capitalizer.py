import re

def capitalize(text):
    return re.sub(r'(^|[.!?]+)(\s*)([a-z])', lambda m: m.group(1) + m.group(2) + m.group(3).upper(), text)

print(capitalize("this is a simple sentence."))
