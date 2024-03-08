"""
Spreadsheets often use this alphabetical encoding for its columns: "A", "B", "C", ..., "AA", "AB", ..., "ZZ", "AAA", "AAB", ....

Given a column number, return its alphabetical column id. For example, given 1, return "A". Given 27, return "AA".
"""

def get_alpha_code(num: int) -> str:
    alpha = list(map(chr, range(97, 123)))
    major = num // 26
    minor = num % 26
    if major > 26:
        return
    elif 0 < major <= 26:
        return alpha[major-1] + alpha[minor]
    else:
        return alpha[minor]


if __name__ == "__main__":
    print(get_alpha_code(26))
        