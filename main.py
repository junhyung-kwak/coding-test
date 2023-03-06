from solution import solution

if __name__ == "__main__":
    from glob import glob
    import time
    # load inputs
    from utils import loader
    site = "programmers"

    loader = getattr(loader, site)

    for file in glob('./test_case/*.txt'):
        inputs = loader(file)
        st = time.time()
        ret = solution(*inputs)
        et = time.time()
        print('sol :', ret, f'{(et-st)*1000:.4f} ms')
