"""
Given a number in Roman numeral format, convert it to decimal.

The values of Roman numerals are as follows:

{
'M': 1000,
'D': 500,
'C': 100,
'L': 50,
'X': 10,
'V': 5,
'I': 1
}
In addition, note that the Roman numeral system uses subtractive notation for numbers such as IV and XL.

For the input XIV, for instance, you should return 14.
"""

# start with the highest numeral
# work down

ROMAN_MAP = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}

def convert_to_decimal(roman_numeral: str) -> int:
    roman_descending = [k for k, v in sorted(ROMAN_MAP.items(), key=lambda item: item[1], reverse=True)]
    decimal = 0
    placement = dict()
    passed_numerals = []
    
    for roman in roman_descending:
        if roman in roman_numeral:
            curr_index = roman_numeral.index(roman)
            placement[roman] = curr_index
            
            if passed_numerals:
                for passed in passed_numerals:  # need to specify a hierarchy 
                    if curr_index + 1 == placement[passed]:
                        # current index after larger numeral -> subtract
                        decimal -= ROMAN_MAP[roman]
                    elif curr_index - 1 == placement[passed]:
                        # current index before larger numeral -> add
                        decimal += ROMAN_MAP[roman]
                    else:
                        # current index does not effect larger numeral -> add
                        decimal += ROMAN_MAP[roman]
            else:
                decimal += ROMAN_MAP[roman]
                
            passed_numerals.append(roman)
        
        print(decimal)
            
    return decimal


if __name__ == "__main__":
    print(convert_to_decimal("XIV"))
