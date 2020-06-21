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
