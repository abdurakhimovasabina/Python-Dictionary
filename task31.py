def count_letters(text: str) -> dict[str, int]:

    counts = {}

    for ch in text:
        if ch.isalpha():
            counts[ch] = counts.get(ch, 0) + 1
            
    return counts

text2 = "assalomu alaykum"
print(count_letters(text2))