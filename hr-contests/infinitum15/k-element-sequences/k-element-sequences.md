Given two integers, N and K, find the number of sequences that meet the following criteria:

The sequence is of size K (i.e., contains K integers).
Each element in the sequence is a positive integer.
The sum of all elements in the sequence is N.
Input Format

The first line contains the number of test cases, T. 
The T subsequent lines each describe a test case as two space-separated integers, N and K.

Constraints

1<=T<=1000
1<=K<=N<=2*10^6
Output Format

For each test case, print the total number of possible KK-element sequences of positive integers such that the sum of the elements in each sequence is N. As the answer may be large, output your answer modulo (10^9+7)

Sample Input

3
4 3
5 2
7 7
Sample Output

3
4
1
Explanation

In the first test case, N=4, K=3
The possible sequences are: 
(1,1,2)
(1,2,1) 
(2,1,1)

There are three possible sequences, so our first line of output is the result of 3 mod(10^9+7), which is 3.