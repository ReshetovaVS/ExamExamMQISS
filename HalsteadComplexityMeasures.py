import math

from radon.visitors import HalsteadVisitor

my_code = '''
import sys

n = int(input())
input_list = [int(input()) for el in range(n)]
print()
if n <= 7 or n > 10000:
    print("Ошибка ввода числа измерений.  Ожидается 7 < N < 10000.")
    sys.exit()
max_s = -sys.maxsize
for i in range(n - 7):
    for j in range(n - 7 - i):
        current_s = input_list[i] + input_list[i + j + 7]
        if current_s > max_s:
            max_s = current_s

print(max_s)
'''

visitor = HalsteadVisitor.from_code(my_code)

print("Уникальные операторы: " + str(visitor.operators_seen))
print("Уникальные операнды: " + str(visitor.operands_seen))

n1, n2 = visitor.distinct_operators, visitor.distinct_operands
N1, N2 = visitor.operators, visitor.operands
n = n1 + n2
N = N1 + N2
if n1 and n2:
    length = n1 * math.log(n1, 2) + n2 * math.log(n2, 2)
else:
    length = 0
volume = N * math.log(n, 2) if n != 0 else 0
difficulty = (n1 * N2) / float(2 * n2) if n2 != 0 else 0
effort = difficulty * volume
time = effort / 18.
bugs = volume / 3000.

print("n1: " + str(n1))  # the number of distinct operators
print("n2: " + str(n2))  # the number of distinct operands
print("N1: " + str(N1))  # the total number of operators
print("N2: " + str(N2))  # the total number of operands
print("n: " + str(n))  # the vocabulary, i.e. n1 + n2
print("N: " + str(N))  # the length, i.e. N1 + N2
print("N*: " + str(length))  # calculated_length: n1 * log2(n1) + n2 * log2(n2)
print("V: " + str(volume))  # V = N * log2(h)
print("D: " + str(difficulty))  # D = h1 / 2 * N2 / h2
print("E: " + str(effort))  # E = D * V
print("T: " + str(time))  # T = E / 18 seconds
print("B: " + str(bugs))  # B = V / 3000 - an estimate of the errors in the implementation
