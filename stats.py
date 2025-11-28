def total_word_count(words):
    total = len(words.split())
    print(f"Found {total} total words")

def char_count(words):
    counts = {}
    for ch in words.lower():
        if ch.isspace():
            continue
        counts[ch] = counts.get(ch, 0) + 1

    return counts