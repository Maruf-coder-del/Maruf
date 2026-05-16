# Bu mening hayotimdagi birinchi Python kodi!
# Katta harf bilan boshladim, nuqta-vergul shart emas

print("Assalomu Alaykum, Python olami!") # String - qo'shtirnoq ichida
print('Men backend dasturchi bo`laman!') # Bittalik qo'shtirnoq ham bo'ladi
print(42)                                # Son - qo'shtirnoqsiz
print(3.14)                              # O'nli son ham qo'shtirnoqsiz



# 1. Bir nechta narsani chiqarish (vergul ajratib beradi, orasiga bo'shliq qo'yadi)
ism = "Ali"
yosh = 25
print("Mening ismim", ism, "va yoshim", yosh)

# 2. End parametri - yangi qatorga tushmaslik
print("Bir", end=" -> ")
print("ikki", end=" -> ")
print("Uch")
# Chiqish: Bir -> ikki -> Uch

# 3. Sep parametri - elementlar orasidagi ajratuvchi
print("2024", "01", "15", sep="-") # Sana formati
print("Ali", "Valiyev", sep=", ")  # Ism familya ajratish
# Chiqish:
# 2024-01-15
# Ali, Valiyev

# 4. Escape belgilari (ekranizatsiya)
print("Men \"Python\" o`rganyapman")    # Qo'shtirnoq ichida qo'shtirnoq
print("Birinchi qator\nIkkinchi qator") # Yangi qator
print("Mana bu \tjoy tashlaydi")        # Tab (4 bo'shliq)


print("=" * 50)
print("PYTHON BACKEND DASTURCHILIK KURSI")
print("=" * 50)
print("Ustoz, AI Mentor")
print("Talaba: Men")
print("Boshlanish sanasi: 2026-05-07")
print("Maqsad: 10 oyda kuchli dasturchi bo'lish")
print("=" * 50)



# O'zgaruvchi yaratish (e'lon qilish)
ism = "Dilshod"  # ism nomli qopda "Dilshod" matni
yosh = 23        # yosh nomli qopda 23 soni
talaba_mi = True # talaba_mi qopda True (ha) yoki False (yo'q)
vazn = 72.5      # vazn qopda o'nli son

# O'zgartiruvchilarni ishlatish
print(ism)      # Dilshod
print(yosh + 5) # 28 (hisoblash mumkin)

user_name = "john"          # snake_case - so'zlar orasi pastki chiziq
total_price = 150000
is_active = True
max_retry_count = 3
PI = 3.14159                # Konstantalar KATTA HARF
_backend_url = "http://..." # Ichki o'zgaruvchi pastki chiziq bilan 

#1user = "john"     # Son bilan Boshlamaslik
#user-name = "john" # Defis ishlatilmaslik
#user name = "john" # Bo'shliq ishlatmaslik
#class = "Python"   # Kalit so'zlar ishlatmaslik
#myVariable = 5     # camelCase Python'da ishlatilmaydi (faqat class nomlarida)


# Bir qatorda bir nechta o'zgaruvchi
x, y, z = 10, 20, 30
print(x, y, z) # 10 20 30

# Qiymatlar almashish (boshqa tillarda 3 qator kerak)
a, b = 5, 10
a, b = b, a #Mana! a=10, b=5 bo'ldi
print(f"a={a}, b={b}") # a=10 b=5

# Tuple unpacking
koordinatalar = (41.2995, 69.2401) # Toshkent koordinatalari
lat, lon = koordinatalar
print(f"Toshkent: {lat}°N, {lon}°E")


# 1. Integer (int) - Butun sonlar
yosh = 25
aholi_soni = 35_000_000   # Pastki chiziq o'qish uchun qulaylik (Pythonga ta'siri yo'q)
temperatura = -5
katta_son = 2_147_483_647

# 2. Float - O'nli sonlar
boy = 1.75         # metrda
narx = 99.99
e = 2.71828        # Eyler soni
ilmiy_son = 1.5e-3 # 0.0015

# 3. String (str) - Matn
ism = "Abdulla"
manzil = "Toshkent, Chilonzor"
kop_qatorli = """Bu ko'p qatorli matn"""
f_str = f"Mening ismim {ism}"            # f-string (keyinroq)

# 4. Boolean (bool) - Mantiqiy
aktiv_mi = True
tugadi_mi = False
# True va False KATTA HARF BILAN


qiymat = 42
print(type(qiymat)) # <class 'int'>

qiymat = "42"
print(type(qiymat)) # <class 'str'> - endi matn!

print(type(3.14))   # <class 'float'>
print(type(True))   # <class 'bool'>
print(type(None))   # <class 'NoneType'>

# Stringdan songa
matn_son = "100"
son = int(matn_son) # 100 (integer)
print(son + 50)     # 150

# Butun sondan o'nli songa
butun = 7
onli = float(butun) # 7.0
print(onli / 2)     # 3.5

# Har qanday narsani stringga
son = 123
matn = str(son)        # "123"
print("Raqam:" + matn) # Raqam: 123 - matnlar qo'shildi

# Boolean ga o'tkazish 
print(bool(1))  # True
print(bool(0))  # False
print(bool("")) # False - bo'sh matn
print(bool([])) # False - bo'sh ro'yxat 


# BU XATO!
#matn = "abc"
#son = int(matn) # ValueError: invalid literal for int() with base 10: 'abc'

# To'g'ri ishlash:
matn = "123abc"
if matn.isdigit(): # Tekshirish
    son = int(matn)
else:
    print("Matnda harflar bor!")   
    
    
# 1. SyntaxError - Sintaksis xatosi (noto'g'ri yozuv)
#print("Salom" # Qavs yopilmadi
# Error: SyntaxError: unexpected EOF while parsing

# 2. NameError - Mavjud bo'lmagan nom
#print(x) # x hech qachon yaratilmagan
# Error: NameError: name 'x' is not defined

# 3. TypeError - Noto'g'ri tur
#natija = "5" + 5 # Matnga son qo'shib bo'lmaydi
# Error: TypeError: can only concatenate str (not "int") to str

# 4. ValueError - Noto'g'ri qiymat
#son = int("hello") # Matnni songa aylantirib bo'lmaydi
# Error: ValueError: invalid literal for int()  


# Xato chiqsa, xato xabarini oxiridan boshiga qarab o'qish
#
# Traceback (most recent call last):
#    File "maiin.py", line 5, in <module>
#      natija = son / nol         <-- XATO QAYERDA
# ZeroDivisionError: division by zero    <-- XATO TURI VA SABABI

# Demak:
# - Qayerda? main.py fayli, 5-qatorda
# - Nima xato? ZeroDivisonError
# - Nima uchun? division by zero (nolga bo'lish)   