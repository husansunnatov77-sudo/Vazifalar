# k = int(input("k:"))
# n = int(input("n:"))

# for i in range(n):
#     print(k)

# a = int(input("a:"))
# b = int(input("b:"))

# count = 0
# for i in range(a, b + 1):
#     print(i)
#     count += 1

# print("Soni:", count)

# a = int(input("a:"))
# b = int(input("b:"))

# count = 0
# for i in range(b - 1, a, -1):
#     print(i)
#     count += 1

# print("Soni:", count)

# price = float(input("son:"))

# for i in range(1, 11):
#     print(i, "kg =", i * price)

# price = float(input("son:"))

# for i in range(1, 11):
#     print(i / 10, "kg =", (i / 10) * price)

# price = float(input("son:"))

# x = 1.2
# while x <= 2:
#     print(x, "kg =", x * price)
#     x += 0.2

# a = int(input("a:"))
# b = int(input("b:"))

# s = 0
# for i in range(a, b + 1):
#     s += i

# print(s)

# a = int(input("a:"))
# b = int(input("b:"))

# p = 1
# for i in range(a, b + 1):
#     p *= i

# print(p)

# a = int(input("a:"))
# b = int(input("b:"))

# s = 0
# for i in range(a, b + 1):
#     s += i * i

# print(s)

# n = int(input())

# s = 0
# for i in range(1, n + 1):
#     s += 1 / i

# print(s)

# n = int(input())

# s = 0
# for i in range(n, 2 * n + 1):
#     s += i * i

# print(s)

n = int(input())

s = 1
for i in range(1, n + 1):
    s *= (1 + i / 10)

print(s)

n = int(input())

s = 0
sign = 1
for i in range(1, n + 1):
    s += sign * (1 + i / 10)
    sign *= -1

print(s)

n = int(input())

s = 0
for i in range(1, n + 1):
    s += 2 * i - 1
    print(i, "kvadrati =", s)

n = int(input())
a = float(input())

p = 1
for i in range(n):
    p *= a

print(p)

n = int(input())
a = float(input())

p = 1
for i in range(1, n + 1):
    p *= a
    print("a^", i, "=", p)

n = int(input())
a = float(input())

s = 1
p = 1
print(1)

for i in range(1, n + 1):
    p *= a
    print(p)
    s += p

print("Yig'indi =", s)

n = int(input())
a = float(input())

s = 1
p = 1
sign = -1

for i in range(1, n + 1):
    p *= a
    s += sign * p
    sign *= -1

print(s)

n = int(input())

f = 1
for i in range(1, n + 1):
    f *= i

print(f)

n = int(input())

s = 0
f = 1
for i in range(1, n + 1):
    f *= i
    s += f

print(s)
