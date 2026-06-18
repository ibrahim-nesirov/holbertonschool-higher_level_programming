import math

def f(x, y):
    return -2*(1+x)*math.exp(-2*x) + 0.5

def z(x):
    return (-2*x - 1)*math.exp(-2*x) + 0.5*x + 2

x0 = float(input("\nx-in ilkin qiymeti(x0): "))
y0 = float(input("y-in ilkin qiymeti(y0): "))
h = float(input("Addim(h): "))
n = int(input("Iterasiya sayi: "))


def euler_method(f, x0, y0, h, n):
    results = [(x0, y0)]
    for i in range(n):
        x, y = results[-1]
        y_new = y + h*f(x, y)
        x_new = x + h
        results.append((x_new, y_new))
    return results
approx_solution = euler_method(f, x0, y0, h, n)
exact_solution = z(1)

print(f"\nx=1 olduqda deqiq hell: {exact_solution}")
print("\nDeyerler cedveli:")
print(" x    | y (texmini) | y (deqiq) ")
print("-"*38)

for x, y in approx_solution:
    y_exact = z(x)
    print(f"{x:.2f} | {y:.6f}    | {y_exact:.6f}")

y_approx = approx_solution[-1][1]
error = abs(exact_solution - y_approx)
print(f"\nx=1-deki xeta: {error:.6f}\n")