import argparse, os

parser = argparse.ArgumentParser()

parser.add_argument('path')
parser.add_argument('--problems', default='A B C D E F')


def make_contest_file(path, problems):
    os.mkdir(path)
    for problem in problems:
        with open(f'{path}/{problem}.py', 'w') as f:
            pass
            # f.write('import sys\ninput = sys.stdin.readline\n')
        with open(f'{path}/{problem}_testcase.txt', 'w'):
            pass

    testdef_s = '''
def test(X):
    print(f'test {X}:')
    with open(f'./{X}_testcase.txt') as f:
        testcases = [i.split('\\n\\n') for i in f.read().split('\\n\\n\\n')]
        try:
            for i, (input_, output_) in enumerate(testcases):
                with open('./tmp.txt', 'w') as f:
                    f.write(input_)
                ts = time.time()
                code_output_ = subprocess.check_output(f'python {X}.py < tmp.txt', shell=True).decode('utf-8')[:-1]
                assert code_output_ == output_, f'  the output for input {input_} should be {output_}, not {code_output_}'
                tf = time.time()
                if tf-ts>3:
                    print(f'    It took {time.time()-ts:.2f} s for input \\n{input_}')
            print(f'test {X} passed')
        except ValueError:
            print(f'{X}_testcase.txt is wrong')'''

    with open(f'{path}/test.py', 'w') as f:
        test_s = '\n    '.join([f'test("{problem}")' for problem in problems])
        f.write(f'''import subprocess, time

{testdef_s}

if __name__ == '__main__':
    {test_s}
''')


if __name__ == '__main__':
    args = parser.parse_args()
    make_contest_file(args.path, args.problems.split())
