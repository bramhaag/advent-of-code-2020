import re

PASSPORT_PATTERN = re.compile(r'^.*(?=.*byr)(?=.*iyr)(?=.*eyr)(?=.*hgt)(?=.*hcl)(?=.*ecl)(?=.*pid).*$')

with open('input.txt', 'r') as file:
    passports = map(lambda p: p.replace('\n', ''), file.read().split("\n\n"))

print(len([p for p in passports if PASSPORT_PATTERN.match(p)]))
