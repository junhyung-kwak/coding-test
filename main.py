from solution import solution

if __name__ == "__main__":
    from glob import glob
    import time
    import argparse 
    # load inputs
    from utils import loader

    parser = argparse.ArgumentParser(description="coding-test",)
    parser.add_argument("--site", type=str, default="programmers", choices=["programmers",])
    parser.add_argument("--split", type=str, default="\t", )
    args = parser.parse_args()

    loader = getattr(loader, args.site)

    for file in glob('./test_case/*.txt'):
        inputs = loader(file, args.split)
        st = time.time()
        ret = solution(*inputs[:-1])
        et = time.time()
        
        print('* test start', file, )
        print('| sol :', ret, ', target :', f'{inputs[-1]} ')
        print(f'| result :', f'{(ret== inputs[-1])},',  f'{(et-st)*1000:.4f} ms')
        print('| test end', file, )
        print('\n')
