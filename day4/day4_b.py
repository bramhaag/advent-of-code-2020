import re

PASSPORT_PATTERN = re.compile(r'^.*'
                              r'(?=.*byr:(19[2-9][0-9]|200[0-2])\s)'
                              r'(?=.*iyr:20(1[0-9]|20)\s)'
                              r'(?=.*eyr:20(2[0-9]|30)\s)'
                              r'(?=.*hgt:(1([5-8][0-9]|9[0-3])cm|(59|[6-7][0-9]|7[0-6])in)\s)'
                              r'(?=.*hcl:#[0-9a-f]{6}\s)'
                              r'(?=.*ecl:(amb|blu|brn|gry|grn|hzl|oth)\s)'
                              r'(?=.*pid:[0-9]{9}\s)'
                              r'.*$', re.DOTALL)

with open('input.txt', 'r') as file:
    passports = map(lambda p: p + ' ', file.read().split("\n\n"))

print(len([p for p in passports if PASSPORT_PATTERN.match(p)]))