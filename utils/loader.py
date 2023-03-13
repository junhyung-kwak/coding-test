
def programmers(file, split='\t'):
    with open(file, 'r')  as f:
        content = f.read().strip()

    return list(map(eval, content.split(split)))

