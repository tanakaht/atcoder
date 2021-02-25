def test(solver1, solver2, test_cases, str2solverinput, output_file='./testcase.txt'):
    cnt = 0
    with open(output_file, 'w') as f:
        for test_case in test_cases:
            test_case = str2solverinput(test_case)
            if solver1(test_case) != solver2(test_case):
                f.write(test_case+'\n')
                cnt += 1
    print(f'answer is not match in {cnt} cases')
