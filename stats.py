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

def sorted_words(dict):
    results = []

    for k, v in dict.items():
        if not k.isalpha():
            continue
        results.append({"char": k, "num": v})

    results.sort(reverse=True, key=sort_on)
    
    return results

def sort_on(items):
    return items["num"]