#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if isinstance(roman_string, str) and roman_string != '':
        num = rom_int.get(roman_string[len(roman_string) - 1])
        track = rom_int.get(roman_string[len(roman_string) - 1])

        for i in range(len(roman_string) - 1):
            rom = rom_int.get(roman_string[(len(roman_string) - 2) - i])
            if rom < track:
                num -= rom
                track = rom
            else:
                num += rom
                track = rom
        return (num)
    else:
        return (0)
