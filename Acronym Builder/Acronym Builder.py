def build_acronym(phrase):
    ignored_words = ["and", "of"]
    processed_phrase = phrase.replace('-', ' ').replace('_', ' ')

    words = processed_phrase.split()

    acronym_letters = []
    for word in words:
        if word.lower() not in ignored_words and word:
            acronym_letters.append(word[0].upper())

    return "".join(acronym_letters)

print(build_acronym("Search Engine Optimization"))
