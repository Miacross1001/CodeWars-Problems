import re

def to_camel_case(text):
    split_string = re.split('-|_|\n', text)
    res = []

    if len(text) == 0:
        pass
    else:
        res.append(split_string[0])

    for elem in split_string[1:]:
        res.append(elem[0].upper() + elem[1:])

    del split_string
    return ''.join(res)


#print(to_camel_case("the-stealth-warrior")) # theStealthWarrior
#print(to_camel_case("The_Stealth_Warrior")) # TheStealthWarrior
#print(to_camel_case("")) # Nothing
