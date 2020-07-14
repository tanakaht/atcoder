
import subprocess


def test_A():
    with open('./A_testcase.txt') as f:
        testcases = [i.split('\n\n') for i in f.read().split('\n\n\n')]
        try:
            for input_, output_ in testcases:
                with open('./tmp.txt', 'w') as f:
                    f.write(input_)
                code_output_ = subprocess.check_output('python A.py < tmp.txt', shell=True).decode('utf-8')[:-1]
                assert code_output_ == output_, f'In problem A, the output for input {input_} should be {output_}, not {code_output_}'
            print('test A passed')
        except ValueError:
            print('A_testcase.txt is wrong')
        

def test_B():
    with open('./B_testcase.txt') as f:
        testcases = [i.split('\n\n') for i in f.read().split('\n\n\n')]
        try:
            for input_, output_ in testcases:
                with open('./tmp.txt', 'w') as f:
                    f.write(input_)
                code_output_ = subprocess.check_output('python A.py < tmp.txt', shell=True).decode('utf-8')[:-1]
                assert code_output_ == output_, f'In problem A, the output for input {input_} should be {output_}, not {code_output_}'
            print('test B passed')
        except ValueError:
            print('B_testcase.txt is wrong')
        


if __name__ == '__main__':
    test_A()
    test_B()
