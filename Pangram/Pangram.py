def is_pangram(sentence, letters):
    set1 = set(ch.lower() for ch in sentence if ch.isalpha())
    set2 = set(letters.lower())
    
    return set1 == set2 
    
is_pangram("hello", "helo")
