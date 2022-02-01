# Sample code for Hitachi Hokudai Lab. and Hokkaido University Contest 2021 A

* This is an explanation of the sample code used in the Hitachi Hokudai Lab. and Hokkaido University Contest 2021 A. Based on the distributed code the participants can create input samples and evaluate the score of their output on their own local machine.
* Please note that you are using the provided sample code on your own responsibility. In particular, neither Hokkaido University nor Hitachi Ltd. can be held responsible or liable, in case the execution of the provided sample code causes any damage to your computer.
* The provided program for score evaluation is identical with the program which will be used to evaluate your score during the contest. However, since the random seed used to generate the input cases during the contest may vary from your input cases, the final score of your program might vary.

## Sample code overview

The sample code can be found in this folder.

* `judge_A.cpp`
    * This program is the game engine which simulates the environment and scores the contestant output.
* `sample_A.sh`
    * This is an example program that outputs a simple answer (input and output format 2).
* `testcases/*.in`
    * In testcase subfolder, examples of testcases can be found.


## Compilation

To create executable files `judge_A`, please compile judge_A.cpp as follows.

```bash
g++ -std=c++17 -O2 judge_A.cpp -o judge_A
```

# Output the score

For the test case `testcases/A.in`, score calculation are performed as follows.

```bash
./judge_A ./sample_A.sh < testcases/A.in > test_case.result
```

By executing the above command, the score will be output to `test_case.result`.

## Acknowledgement

* The sample code is released under the MIT license.
