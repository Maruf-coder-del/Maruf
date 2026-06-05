# === 1-MISOL: Eng oddiy print ===
print("Assalomu alaykum, dunyo!")

# === 2-MISOL: Bir nechta narsani chop etish ===
print("Python", "juda", "zo'r", "til!")

# === 3-MISOL: Raqamlar bilan ===
print(2024)
print(15 + 25)

# === 4-MISOL: separator (ajratuvchi) parametri ===
print("Olma", "Banan", "Apelsin", sep=" | ")
# Natija: Olma | Banan | Apelsin

# === 5-MISOL: end parametri (qator oxiridagi belgi) ===
print("Birinchhi qator", end=" ---> ")
print("Ikkinchi qator")
# Natija: Birinchi qator ---> Ikkinchi qator

# === 6-MISOL: Yangi qator (newline) ===
print("Yuqoridagi qator\nPastdagi qator")

# === 7-MISOL: Tab (bo'shliq) ===
print("Ism:\tAnvar")
print("Yosh:\t25")


# API server logini chiqarish (keyinchalik shunday yozamiz!)
def log_message(level: str, message: str, user_id: int | None = None):
    """
    Server loglarini chiroyli formatda chiqarish.
    Real loyihalarda loglar faylga yoziladi,
    lekin hozircha print() bilan o'rganamiz.
    """
    prefix = f"[{level.upper()}]"
    time_now = "2026-05-20 22:25:00" # Hozircha qo'lda, keyin datetime o'rganamiz
    
    if user_id:
        print(f"{time_now} {prefix} User({user_id}): {message}")
    else:
        print(f"{time_now} {prefix} SYSTEM: {message}")
        
# Ishlatish
log_message("info", "Server ishga tushdi")
log_message("warning", "Xotira 80% to'ldi")
log_message("error", "Bazaga ulanishda xatolik!", user_id=42)        


# Bu bir qatorli izoh. Python bu qatorni o'qimaydi.

"""
Bu ko'p qatorli izoh (docstring).
Funksiya yoki modul haqida
batafsil ma'lumot berish uchun ishlatiladi.
"""

# Izohlar NIMA UCHUN kerak?
# 1. Kodni tushuntirish
# 2. Keyinchalik o'zimga eslatma
# 3. Jamoadoshlar tushunadi
# 4. Professional kod shunday yoziladi!


# === 1-MISOL: Asosiy o'zgaruvchilar ===
ism = "Anvar"
yosh = 25
boyi = 1.75
talaba_mi = True

print("Ism:", ism)
print("Yosh:", yosh)
print("Bo'yi:", boyi)
print("Talaba:", talaba_mi)

# === 2-MISOL: O'zgaruvchilarni qayta belgilash ===
ball = 80
print("Dastlabki ball:", ball)

ball = 95 # Yangi qiymat berdik
print("Yangi ball:", ball)

ball = ball + 5 # 95 + 5 = 100
print("Qo'shilgandan keyin:", ball)

# === 3-MISOL: Bir nechta o'zgaruvchini bir qatorda ===
a, b, c = 10, 20, 30
print(a, b, c) # 10 20 30

# === 4-MISOL: O'zgaruvchilarni almashinuvi (Pythoncha sehr) ===
x = "olma"
y = "banan"
print("Oldin:", x, y) 

x, y = y, x # Bir qatorda almashtirish!
print("Keyin:", x, y) # banan olma

# === 5-MISOL: O'zgaruvchi nomlash qoidalari ===
# To'g'ri ✅
foydalanuvchi_ismi = "Laylo" # snake_case (Python standarti)
maxBall = 100 # camelCase (Python da kam)
MAKSIMUM_URINISH = 3 # UPPER_CASE (o'zgarmas qiymatlar)
_user = "ichki" # _ bilan boshlansa "protected"
user_2 ="ikkinchi" # raqam oxirida bo'lishi mumkin

# Noto'g'ri ❌ (sinab ko'rish, xatolik beradi)
# 2user = "xato" # raqam bilan boshlanmaydi!
# user-name = "xato" # defis qo'yilmaydi!
# class = "xato" # Pythonning kalit so'zi!
# my var = "xato" # bo'shliq qo'yilmaydi!


# Foydalanuvchi ma'lumotlarini saqlash
# (keyinchalik bunday ma'lumotlar bazadan keladi)
user_data = {
    "id": 1001,
    "username": "anvar_dev",
    "email": "anvar_dev@example.com",
    "is_active": True,
    "login_attempts": 0
}

# Login qilish funksiyasi (soddalashtirilgan)
MAX_LOGIN_ATTEMPTS = 5
current_attempts = user_data["login_attempts"]
can_login = current_attempts < MAX_LOGIN_ATTEMPTS

print(f"Foydalanuvchi: {user_data['username']}")
print(f"Kirish mumkin: {can_login}")
print(f"Qolgan urinishlar: {MAX_LOGIN_ATTEMPTS - current_attempts}")


# === type() funksiyasi - turni aniqlash ===
print(type(42)) # <class 'int'>
print(type(3.14)) # <class 'float'>
print(type("hello")) # <class 'str'>
print(type(True)) # <class 'bool'>
print(type(None)) # <class 'NoneType'>

# === int - butun sonlar ===
yosh = 25
temperatura = -5
aholi_soni = 35_000_000 # _ belgi raqamlarni o'qish uchun, e'tiborsiz
katta_son = 2**10 # 1024 (2 ning 10-darajasi)

# Arifmetik amallar
print(10 + 3) # 13 (qo'shish)
print(10 - 3) # 7 (ayirish)
print(10 * 3) # 30 (ko'paytirish)
print(10 / 3) # 3.333... (bo'lish - natija float!)
print(10 // 3) # 3 (butun bo'lish)
print(10 % 3) # 1 (qoldiq)
print(10 ** 3) # 1000 (darajaga ko'tarish)

# === float - haqiqiy sonlar ===
narx = 99.99
pi = 3.14159
foiz = 18.5

# Float bilan hisob-kitoblar
print(0.1 + 0.2) # 0.30000000000000004 (e'tibor berish kerak!)
print(round(0.1 + 0.2, 2)) # 0.3 (to'g'ri yaxlitlash)

# === str - matnlar ===
ism = "Aziza"
familya = 'Karimova' # ' yoki " farqi yo'q"

# Matnlarni qo'shish (concatenation)
toliq_ism = ism + " " + familya
print(toliq_ism) # Aziza Karimova

# Matnni ko'paytirish
print("Ha" * 3) # HaHaHa 
print("-" * 20) # --------------------

# Matn uzunligi
print(len(toliq_ism)) # 14

# === bool - mantiqiy qiymatlar ===
is_online = True
has_permission = False

print(10 > 5) # True
print(10 < 5) # False
print(10 == 10) # True (tengmi?)
print(10 != 5) # True (teng emasmi?)

# === None - bo'sh qiymat ===
# "Hali qiymat berilmagan" degani
natija = None
print(natija) # None
print(type(None)) # <class 'NoneType'>


# Mahsulot ma'lumotlarini validatsiya qilish (tekshirish)
# FastAPI da men shunday validatsiya qilishim kerak!

def validate_product(name: str, price: float, quanity: int) -> bool:
    """
    Mahsulot ma'lumotlarini tekshirish.
    
    Args:
        name: Mahsulot nomi (str)
        price: Narxi (float)
        quantity: Soni (int)
        
    Returns:
        bool: Agar hammasi to'g'ri bo'lsa True    
    """
    # Nom bo'sh emasligin tekshirish
    if not name or not name.strip():
        print(f"Xatolik: Mahsulot nomi bo'sh bo'lishi mumkin emas!")
        return False
    
    # Narx musbatligini tekshirish
    if price <= 0:
        print(f"Xatolik: Narx musbat bo'lishi kerak! Berilgan: {price}")
        return False
    
    # Soni butun va nomanfiy bo'lishini tekshirish
    if quanity < 0:
        print(f"Xatolik: Soni manfiy bo'lishi mumkin emas! Berilgan: {quanity}")
        return False
    
    # Ma'lumot turlarini tekshirish
    if not isinstance(name, str):
        print(f"Xatolik: Nom matn (str) bo'lishi kerak! Turi: {type(name)}")
        return False
    
    if not isinstance(price, (int, float)):
        print(f"Xatolik: Narx son (int/float) bo'lishi kerak! Turi: {type(price)}")
        return False
    
    print(f"✅ Mahsulot '{name}' muvaffaqiyatli tekshirildi!")
    return True

# Test
print(validate_product("iPhone 15", 999.99, 50)) # True
print(validate_product("", 100.0, 10)) # False
print(validate_product("Noutbuk", -500, 5)) # False


# === 1-XATO: NameError (nom topilmadi) ===
# print(foydalanuvchi)
# NameError: name 'foydalanuvchi' is not defined
# Sabab: o'zgaruvchi hali yaratilmagan!

# To'g'irlash:
foydalanuvchi = "Anvar"
print(foydalanuvchi) # Endi ishlaydi

# === 2-XATO: TypeError (tur xatosi) ===
# natija = "yosh: " + 25
# TypeError: can only concatenate str (not "int") to str
# Sabab: matn va sonni + bilan qo'shib bo'lmaydi!

# To'g'irlash (3 xil usul):
natija1 = "yosh: " + str(25) # Sonni matnga o'tkazish
natija2 = f"yosh: {25}"      # f-string (eng zo'r usul!)
natija3 = "yosh:", 25        # Vergul bilan (print da ishlaydi)

# === 3-XATO: IndentationError (chekinish xatosi) ===
# if True:
# print("Salom")
# IndentationError: expected an indented block
# Sabab: if dan keyin 4 bo'shliq (yoki TAB) kerak!

# To'g'irlash:
if True:
    print("Salom") # 4 bo'shliq bilan
    
# === 4-XATO: SytaxError ===
# print("Salom)
# SyntaxError: unterminated string literal
# Sabab: qo'shtirnoq yopilmagan!

# To'g'irlash:
print("Salom")

# === 5-XATO: ZeroDivisionError ===
# print(10 / 0)
# ZeroDivisionError: division by zero
# Sabab: 0 ga bo'lish matematikada ham mumkin emas!

# To'g'irlash (himoya):
boluvchi = 0
if boluvchi != 0:
    print(10 / boluvchi)
else:
    print("0 ga bo'lib bo'lmaudi!")     