alphabet = {
    "a": "2",
    "b": "22",
    "c": "222",
    "d": "3",
    "e": "33",
    "f": "333",
    "g": "4",
    "h": "44",
    "i": "444",
    "j": "5",
    "k": "55",
    "l": "555",
    "m": "6",
    "n": "66",
    "o": "666",
    "p": "7",
    "q": "77",
    "r": "777",
    "s": "7777",
    "t": "8",
    "u": "88",
    "v": "888",
    "w": "9",
    "x": "99",
    "y": "999",
    "z": "9999",
    " ": "0"
}


def translate(string):
    last_char = alphabet[string[0]]
    output = last_char
    string = string[1:]
    for char in string:
        if last_char in alphabet[char] or alphabet[char] in last_char:
            output += " "
        output += alphabet[char]
        last_char = alphabet[char]
    return output


testcase_numbers = int(input())
for i in range(testcase_numbers):
    input_string = input()
    output = translate(input_string)
    print(f"Case #{i + 1}: " + output)
