def create_name(inception, file_names):
    lens = []
    c = []
    for name in file_names:
        lens.append(len(name))
    a = max(lens)
    for el in inception:
        if el not in c:
            c.append(el)
    name_inception = " ".join(c)
    if len(name_inception) < a:
        b = a - len(name_inception)
        new_name = name_inception + "_" * b
        return new_name