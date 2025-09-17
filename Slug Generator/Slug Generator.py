def generate_slug(s):

    s = s.lower()
    filtered_chars = ''
    for char in s:
        if char.isalnum() or char.isspace():
            filtered_chars += char

    words = filter(None, filtered_chars.split(' '))

    slug = "%20".join(words)
    
    return slug


print(generate_slug("hello world"))
