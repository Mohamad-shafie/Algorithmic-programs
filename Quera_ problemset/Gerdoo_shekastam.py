# Question Link: https://quera.org/problemset/3540
inpt = input()
n_x_y = list(map(int, inpt.split(" ")))
n, x, y = n_x_y[0], n_x_y[1], n_x_y[2]
x_steps, y_steps, posible = 0, 0, True

while n % x:
    y_steps += 1
    n -= y
    if n < 0 :
        posible = False
        break
x_steps = n / x

if posible:
    print(int(x_steps), end=" ")
    print(int(y_steps))
else:
    print(-1)