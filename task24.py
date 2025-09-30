def most_common_char(text: str) -> str:

    counts = {}

    for ch in text:
        if ch.isalpha():
            counts[ch] = counts.get(ch, 0) + 1
            
    return max(counts, key=counts.get) if counts else ""

text = "assalomu alaykum"
print(most_common_char(text))