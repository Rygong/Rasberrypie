num = int(input())

n = num

count = int(0)

while True:
    n_1 = num
    n_2 = num

    n_1 = int(num/10)
    n_2 = num%10
    n_3 = (n_1 + n_2) % 10
    num = (n_2 *10) + n_3

    count = count + 1

    if(num == n):
        break
print(count)