import re

PASSPORT_PATTERN = re.compile(r'^.*(?=.*byr)(?=.*iyr)(?=.*eyr)(?=.*hgt)(?=.*hcl)(?=.*ecl)(?=.*pid).*$', re.DOTALL)

with open('input.txt', 'r') as file:
    passports = file.read().split("\n\n")

print(len([p for p in passports if PASSPORT_PATTERN.match(p)]))
