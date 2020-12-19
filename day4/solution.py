"""
Part 1:
Valid passports have all the required fields, CID is optional

Part 2:

    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.

"""


class Passport:
    def __init__(self, passport):
        self.passport = passport

    # part 1
    def check_fields(self):
        return len(self.passport) == 8 or (len(self.passport) == 7 and 'cid' not in self.passport)

    # abstract year checking into a helper
    def valid_year(self, key, start, end):
        return len(self.passport[key]) == 4 and int(self.passport[key]) >= start and int(self.passport[key]) <= end

    def check_years(self):
        return self.valid_year('byr', 1920, 2002) and \
               self.valid_year('iyr', 2010, 2020) and \
               self.valid_year('eyr', 2020, 2030)

    def check_hcl(self):
        return self.passport['hcl'][0] == "#" and self.passport['hcl'][1:].isalnum()

    def check_ecl(self):
        return self.passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    def check_pid(self):
        return len(self.passport['pid']) == 9

    def check_hgt(self):
        if self.passport['hgt'][-2:] == "cm":
            return int(self.passport['hgt'][:-2]) >= 150 and int(self.passport['hgt'][:-2]) <= 193
        elif self.passport['hgt'][-2:] == "in":
            return int(self.passport['hgt'][:-2]) >= 59 and int(self.passport['hgt'][:-2]) <= 76

    def is_valid(self):
        return (self.check_fields() and self.check_years()
                and self.check_hcl() and self.check_ecl() and self.check_pid() and self.check_hgt())


def get_passports(file):
    passports = []
    passport = {}
    for line in file:
        if line != "\n":
            line = line.rstrip().split(" ")  # splits into fields
            line = [field.split(":") for field in line]
            for field in line:
                passport[field[0]] = field[1]
        else:
            passports.append(passport)
            passport = {}
    passports.append(passport)
    return passports


if __name__ == "__main__":
    part_1_count, part_2_count = 0, 0
    with open('input.txt') as file:
        passports = get_passports(file)
        checked_passports = [Passport(passport) for passport in passports]
        for p in checked_passports:
            if p.check_fields():
                part_1_count += 1
            if p.is_valid():
                part_2_count += 1
    print(part_1_count, part_2_count)
