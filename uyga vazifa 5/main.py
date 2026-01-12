son = int(input("Son kiriting: "))
if son > 0:
    son = son + 1
print(f"Natija: {son}\n")

son = int(input("Son kiriting: "))
if son > 0:
    son += 1
else:
    son = -2
print(f"Natija: {son}\n")

son = int(input("Son kiriting: "))
if son > 0:
    son += 1
elif son < 0:
    son = -2
else:
    son = 10
print(f"Natija: {son}\n")

a = int(input("1-son: "))
b = int(input("2-son: "))
c = int(input("3-son: "))

musbat_soni = 0
if a > 0: musbat_soni += 1
if b > 0: musbat_soni += 1
if c > 0: musbat_soni += 1

print(f"Musbat sonlar soni: {musbat_soni}\n")

musbat = 0
manfiy = 0
if a > 0: musbat += 1
elif a < 0: manfiy += 1
if b > 0: musbat += 1
elif b < 0: manfiy += 1
if c > 0: musbat += 1
elif c < 0: manfiy += 1

print(f"Musbat: {musbat}, Manfiy: {manfiy}, Nol: {3 - musbat - manfiy}\n")

a = int(input("a = "))
b = int(input("b = "))
if a > b:
    print(f"Katta son: {a}")
elif b > a:
    print(f"Katta son: {b}")
else:
    print("Sonlar teng\n")

    a = int(input("1-son: "))
b = int(input("2-son: "))
if a < b:
    print("Kichigi 1-o'rinda")
else:
    print("Kichigi 2-o'rinda\n")

    a = int(input("a = "))
b = int(input("b = "))
if a > b:
    print(f"Katta: {a}, Kichik: {b}")
else:
    print(f"Katta: {b}, Kichik: {a}\n")

    A = float(input("A = "))
B = float(input("B = "))
if A > B:
    A, B = B, A  # almashtirish
print(f"Tartiblangan: A = {A}, B = {B}\n")

a = int(input("a = "))
b = int(input("b = "))
if a != b:
    print(f"Yig'indisi: {a + b}")
else:
    print("Teng bo'lgani uchun natija: 0\n")

    a = int(input("a = "))
b = int(input("b = "))
if a != b:
    if a > b:
        print(f"Kattasi: {a}")
    else:
        print(f"Kattasi: {b}")
else:
    print("Natija: 0\n")

    a = int(input("1-son: "))
b = int(input("2-son: "))
c = int(input("3-son: "))

kichik = a
if b < kichik:
    kichik = b
if c < kichik:
    kichik = c

print(f"Eng kichik son: {kichik}\n")
