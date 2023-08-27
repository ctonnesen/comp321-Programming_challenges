testcases = int(input())
for i in range(testcases):
    test = input().lower()
    string_set = set(test)
    alphabet_set = {
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
        "w", "x", "y", "z"}
    missing = alphabet_set.difference(string_set)
    if not missing:
        print("pangram")
    else:
        alphabetic = sorted(missing)
        print(f"missing {''.join(alphabetic)}")
