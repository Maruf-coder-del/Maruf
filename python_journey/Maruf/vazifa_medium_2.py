# Vazifa: Quyidagi ma'lumotlarni chiroyli qilib chiqaring
mahsulot = "iPhone 15 Pro"
narx = 1299.99
miqdor = 3
chegirma_foiz = 10

# Hisob-kitob:
jami_narx = narx * miqdor
chegirma = jami_narx * (chegirma_foiz / 100)
tolov = jami_narx - chegirma
print("="*40)
print("CHEK")
print("="*40)
print(f"Mahsulot: {mahsulot}")
print(f"Narx: {narx}")
print(f"Miqdor: {miqdor}")
print(f"Chegirma {chegirma_foiz}%")
print("-"*40)
print(f"Jami: ${tolov:.2f}")
print("="*40)
