# Asosiy operatorlar
a = 10
b = 3

print(a + b) # 13 - qo'shish
print(a - b) # 7 - ayrish
print(a * b) # 30 - ko'paytirish
print(a / b) # 3.3333... - bo'lish (har doim float qaytaradi)
print(a // b) # 3 - butun qismga bo'lish (floor division)
print(a % b) # 1 - qoldiq (modulo)
print(a ** b) # 1000 - darajaga ko'tarish (10 ning 3-darajasi)


# Son juftmi yoki toqmi?
son = 17
qoldiq = son % 2 # 2 ga bo'lgandagi qoldiq

# Agar qoldiq 0 bo'lsa - juft, 1 bo'lsa - toq
print(f"{son} soni - {'juft' if qoldiq == 0 else 'toq'}")


# 100 ta mahsulotni 30 tadan qilib ko'rsatamiz
jami_mahsulot = 100
sahifa_hajmi = 30

sahifalar_soni = jami_mahsulot // sahifa_hajmi # 3 ta to'liq sahifa
oxirgi_sahifadagilar = jami_mahsulot % sahifa_hajmi # 10 ta mahsulot

print(f"Jami sahifalar: {sahifalar_soni if oxirgi_sahifadagilar == 0 else sahifalar_soni + 1}")
print(f"Oxirgi sahifada: {oxirgi_sahifadagilar if oxirgi_sahifadagilar != 0 else sahifa_hajmi} ta")


x= 5
y = 10

print(x == y) # False - tengmi?
print(x != y) # True - teng emasmi?
print(x > y) # False - kattami?
print(x < y) # True - kichikmi?
print(x >= 5) # True - katta yoki tengmi?
print(y <=10) # True - kichik yoki tengmi?

# String bilan ham ishlaydi!
print("olma" == "olma") # True
print("Olma" == "olma") # False (katta harf muhim!)
print("a" < "b") # True (alfavit tartibida)

# BU XATO - taqqoslash (=) emas, o'zlashtirish (=)
# if x = 5: # SyntaxError!
 #   print("x 5 ga teng")
    
# TO'G'RI -qo'shaloq tenglik (==)
# if x == 5:
 #   print("x 5 ga teng")    
 
 
kiritilgan_parol = "12345"
asl_parol = "12345"

# Strip() - boshidagi va oxiridagi bo'liqlarni olib tashlaymiz
if kiritilgan_parol.strip()  == asl_parol:
    print("Xush kelibsiz!")
else:
    print("Parol noto'g'ri!")
    
    
# And - hamma shart True bo'lishi kerak
yosh = 20
talaba = True

print(yosh >= 18 and talaba == True) # True - (Ikkalasi ham to'g'ri)
print(yosh >= 18 and talaba == False) #False - (biri no'to'g'ri)

# Or - kamida bitta shart True bo'lsa kifoya
dam_olish_kuni = True
kasalmisiz = False

print(dam_olish_kuni or kasalmisiz) # True - (dam olish kuni)
print(not dam_olish_kuni) # False - (teskari)


# Foydalanuvchi tizimga kirish uchun:
# 1. Email tasdiqlangan bo'lishi KERAK (AND)
# 2. Parol to'g'ri bolishi kerak (AND)

email_tasdiqlangan = True
parol_tugri = True
akkaunt_bloklanmagan = True

kirish_mumkin = email_tasdiqlangan and parol_tugri and akkaunt_bloklanmagan

# Admin yoki moderator bo'lsa, bloklangan akkaunt bilan ham kira oladi
admin_mi = True

kirish_mumkin = (email_tasdiqlangan and parol_tugri and akkaunt_bloklanmagan) or admin_mi
print(f"Tizimga kirish mumkinmi? {'Ha' if kirish_mumkin else 'yo`q'}")


pi = 3.14159265359
narx = 59990.5

# .Nf - N xonagacha yaxlitlash
print(f"Pi ning qiymati: {pi:.2f}") # 3.14
print(f"Pi ning qiymati: {pi:.4f}") #3.1416 

