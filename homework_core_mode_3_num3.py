import re

def normalize_phone(phone_numbers):
    number = re.sub(r'[^\d+]', '', phone_numbers)
    if not number.startswith('+'):
        if number.startswith('380'):
            number = '+' + number
        else:
            number = '+38' + number
    return number

phone_numbers = [
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "
]

normalized_numbers = [normalize_phone(number) for number in phone_numbers]
print(normalized_numbers)
