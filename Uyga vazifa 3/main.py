3- uyga vazifa

A = int(input("A = "))
musbat = A > 0
print(musbat)

A = int(input("A = "))
toq = A % 2 == 1
print(toq)

A = int(input("A = "))
juft = A % 2 == 0
print(juft)

A = int(input("A = "))
B = int(input("B = "))
natija = (A > 2) and (B <= 3)
print(natija)

A = int(input("A = "))
B = int(input("B = "))
natija = (A >= 0) or (B < -2)
print(natija)

A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))
natija = (A < B) and (B < C)
print(natija)

A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))
natija = (A < B and B < C) or (C < B and B < A)
print(natija)

A = int(input("A = "))
B = int(input("B = "))
natija = (A % 2 == 1) and (B % 2 == 1)
print(natija)

A = int(input("A = "))
B = int(input("B = "))
natija = (A % 2 == 1) or (B % 2 == 1)
print(natija)

A = int(input("A = "))
B = int(input("B = "))

biri_toq = (A % 2 == 1)
ikkinchisi_toq = (B % 2 == 1)
natija = (biri_toq and not ikkinchisi_toq) or (not biri_toq and ikkinchisi_toq)
print(natija)

A = int(input("A = "))
B = int(input("B = "))

ikkisi_toq = (A % 2 == 1) and (B % 2 == 1)
ikkisi_juft = (A % 2 == 0) and (B % 2 == 0)
natija = ikkisi_toq or ikkisi_juft
print(natija)

A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))
natija = (A <= 0) and (B <= 0) and (C <= 0)
print(natija)

A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))
natija = (A > 0) or (B > 0) or (C > 0)
print(natija)

A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))
musbat1 = (A > 0)
musbat2 = (B > 0)
musbat3 = (C > 0)
soni = musbat1 + musbat2 + musbat3
natija = (soni == 1)
print(natija)

A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))

musbat1 = (A > 0)
musbat2 = (B > 0)
musbat3 = (C > 0)
soni = musbat1 + musbat2 + musbat3
natija = (soni == 2)
print(natija)

A = int(input("A = "))
ikki_xonali = (A >= 10) and (A <= 99)
juft = (A % 2 == 0)
natija = ikki_xonali and juft
print(natija)

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
agar_teng_bolsa = (a == b or b == c or a == c)
print(f"Javob (17-18): {agar_teng_bolsa}\n")

son1 = int(input("1-son: "))
son2 = int(input("2-son: "))
son3 = int(input("3-son: "))
qarama_qarshi_bormi = False
if (son1 == -son2 or son1 == -son3 or son2 == -son3):
    qarama_qarshi_bormi = True
print(f"Javob (19): {qarama_qarshi_bormi}\n")

n = int(input("son = "))

yuzlik = n // 100
onlik = (n // 10) % 10
birlik = n % 10
print(f"Raqamlar: {yuzlik}, {onlik}, {birlik}")

har_xil = (yuzlik != onlik and onlik != birlik and yuzlik != birlik)
print(f"20. Barcha raqamlar har xil → {har_xil}")

tartibda = (yuzlik < onlik < birlik)
print(f"21. Ketma-ket o'suvchi → {tartibda}")

oshuvchi_yoki_kamayuvchi = (yuzlik < onlik < birlik) or (yuzlik > onlik > birlik)
print(f"22. O'suvchi yoki kamayuvchi → {oshuvchi_yoki_kamayuvchi}")

palindrom = (yuzlik == birlik)
print(f"23. Chapdan o'ngga va o'ngdan chapga o'qiganda teng → {palindrom}\n")

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

diskriminant = b**2 - 4*a*c
haqiqiy_ildiz_bormi = (diskriminant >= 0)
print(f"D = {diskriminant}")
print(f"24. Haqiqiy ildiz(lar) bormi? → {haqiqiy_ildiz_bormi}\n")

x2 = float(input("x2 = "))
y2 = float(input("y2 = "))

def chorak_top(x, y):
    if x > 0 and y > 0: return 1
    if x < 0 and y > 0: return 2
    if x < 0 and y < 0: return 3
    if x > 0 and y < 0: return 4
    return 0  # o'qda

chorak1 = chorak_top(x, y)
chorak2 = chorak_top(x2, y2)

bir_chorakda = (chorak1 == chorak2 and chorak1 != 0)
print(f"1-nuqta {chorak1}-chorakda, 2-nuqta {chorak2}-chorakda")
print(f"29. Ikkala nuqta bir chorakdami? → {bir_chorakda}")

print(" Barcha masalalar tugadi ")

a = int(input("a tomoni = "))
b = int(input("b tomoni = "))
c = int(input("c tomoni = "))
teng_tomonli = (a == b == c)
print(f"30. Teng tomonli → {teng_tomonli}\n")

teng_yonli = (a == b or b == c or a == c)
print(f"31. Teng yonli → {teng_yonli}\n")

uchburchak_sharti = (a + b > c) and (a + c > b) and (b + c > a)
if uchburchak_sharti:
    tomonlar = sorted([a, b, c])
    togri_burchakli = (tomonlar[2]**2 == tomonlar[0]**2 + tomonlar[1]**2)
else:
    togri_burchakli = False

print(f"32. To'g'ri burchakli → {togri_burchakli}\n")


yasash_mumkin = (a + b > c) and (a + c > b) and (b + c > a)
print(f"33. Uchburchak yasash mumkin → {yasash_mumkin}\n")


x = int(input("x (ustun) = "))
y = int(input("y (qator) = "))

maydon_qora = ((x + y) % 2 == 1)
print(f"34. ({x},{y}) maydon qora → {maydon_qora}\n")


x1 = int(input("1-maydon x1 = "))
y1 = int(input("1-maydon y1 = "))
x2 = int(input("2-maydon x2 = "))
y2 = int(input("2-maydon y2 = "))

rang1_qora = (x1 + y1) % 2 == 1
rang2_qora = (x2 + y2) % 2 == 1
bir_xil_rang = (rang1_qora == rang2_qora)
print(f"35. Bir xil rangda → {bir_xil_rang}\n")

ruh_ota_oladi = (x1 == x2 or y1 == y2)
print(f"36. Ruh bir yurishda o'ta oladi → {ruh_ota_oladi}\n")

shoh_masofa_x = abs(x1 - x2)
shoh_masofa_y = abs(y1 - y2)
shoh_ota_oladi = (shoh_masofa_x <= 1 and shoh_masofa_y <= 1) and (x1 != x2 or y1 != y2)
print(f"37. Shoh bir yurishda o'ta oladi → {shoh_ota_oladi}\n")

fil_ota_oladi = (abs(x1 - x2) == abs(y1 - y2)) and (x1 != x2)
print(f"38. Fil bir yurishda o'ta oladi → {fil_ota_oladi}\n")

farzin_ota_oladi = (x1 == x2 or y1 == y2 or abs(x1-x2) == abs(y1-y2)) and (x1 != x2 or y1 != y2)
print(f"39. Farzin bir yurishda o'ta oladi → {farzin_ota_oladi}\n")

farzin_ota_oladi = (x1 == x2 or y1 == y2 or abs(x1-x2) == abs(y1-y2)) and (x1 != x2 or y1 != y2)
print(f"39. Farzin bir yurishda o'ta oladi → {farzin_ota_oladi}\n")