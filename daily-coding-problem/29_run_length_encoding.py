"""
Run-length encoding is a fast and simple method of encoding strings. The basic
idea is to represent repeated successive characters as a single count and
character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be
encoded have no digits and consists solely of alphabetic characters. You can
assume the string to be decoded is valid.
"""

# one run through of the string
# keep prev index saved to know if its a sequence or not
# keep sequence total

def run_length_encode(alpha_string):
    def assemble_string():
        """convenience method for encoded string piece"""
        return f"{str(count)}{prev_letter}"

    prev_letter = ""
    count = 1
    encoded = ""
    for letter in alpha_string:
        if prev_letter:
            if letter == prev_letter:
                count += 1
            else:
                encoded += assemble_string()
                count = 1
        prev_letter = letter

    # clean up for last letter
    if count > 1:
        encoded += assemble_string()
    else:
        encoded += assemble_string()

    return encoded


if __name__ == "__main__":
    provided_test = run_length_encode("AAAABBBCCDAA")
    print("\nInput AAAABBBCCDAA yielded the result:", provided_test,
    "expected result matches yield:", provided_test == "4A3B2C1D2A")

    added_test = run_length_encode("AAAABBBCCDAAB")
    print("\nInput AAAABBBCCDAAB yielded the result:", added_test,
    "expected result matches yield:", added_test == "4A3B2C1D2A1B")

    another_test = run_length_encode("GGGHHYYBBFO")
    print("\nInput GGGHHYYBBFO yielded the result:", another_test,
    "expected result matches yield:", another_test == "3G2H2Y2B1F1O")
