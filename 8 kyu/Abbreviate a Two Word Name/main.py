def abbrev_name(name):
    result = []
    name = name.split()
    for elem in name:
        result.append(elem[0].upper())
    return '.'.join(result)
