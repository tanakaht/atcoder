import subprocess, time


def test(X):
    print(f'test {X}:')
    with open(f'./{X}_testcase.txt') as f:
        testcases = [i.split('\n\n') for i in f.read().split('\n\n\n')]
        try:
            for i, (input_, output_) in enumerate(testcases):
                with open('./tmp.txt', 'w') as f:
                    f.write(input_)
                ts = time.time()
                code_output_ = subprocess.check_output(f'python {X}.py < tmp.txt', shell=True).decode('utf-8')[:-1]
                assert code_output_ == output_, f'  the output for input should be {output_}, not {code_output_}'
                tf = time.time()
                if tf-ts>3:
                    print(f'    It took {time.time()-ts:.2f} s for input \n{input_}')
            print(f'test {X} passed')
        except ValueError:
            print(f'{X}_testcase.txt is wrong')

if __name__ == '__main__':
    test("A")
    test("B")
    test("C")
    test("D")
    test("E")
    test("F")
