# Vazifa: Foydalanuvchi profilini yaratish (hozircha qo'lda kiritamiz)
# Keyingi darsda input() bilan avtomatlashtiramiz

# Foydalanuvchi ma'lumotlari
ism = "Dilshod"
familya = "Karimov"
tugilgan_yil = 1998
joriy_yil = 2026
email = "dilshod@example.com"
telefon = "+998901234567"

# Avtomatik hisoblash
yosh = joriy_yil - tugilgan_yil
username = f"{ism.lower()}.{familya.lower()}"
domen = email.split("@")[1] # Keyinroq o'rganamiz

# Profilni chiqarish
profil = f"""
          FOYDALANUVCHI PROFILI
  Ism: {ism:<24}
  Familya: {familya:<24}
  Yosh: {yosh:<24}
  Username: @{username:<23}
  Email: {email:<24}
  Tel: {telefon:<24}
  Provider: {domen:<24}        
"""
print(profil)