def all_unique(word):
    seen = set()
    for char in word:
        if char in seen:
            return False
        seen.add(char) 
    return True

print(all_unique("abc"))
