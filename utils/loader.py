
def programmers(file):
    with open(file, 'r')  as f:
        content = f.read().strip()

    return list(map(eval, content.split('\t')))

