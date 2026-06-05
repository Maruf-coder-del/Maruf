# Matematik hisob-kitoblar:
# Do'konda mahsulot narxi $120.50.
# 15%  chegirma va 12% soliq hisoblash.
#
# 1. Chegirma miqdori ($ da)
# 2. Chegirmadan keyingi narx
# 3. Soliq miqdori
# 4. Yakuniy narx
#
# Har bir qadamni alohida o'zgaruvchida saqlash.
# round() dan foydalanish.

narx = 120.50
chegirma = narx * 0.15
narx_chegirma = narx - chegirma
soliq = narx_chegirma * 0.12
yakuniy_narx = narx_chegirma + soliq
print(f"Chegirma miqdori: ${chegirma:.2f}")
print(f"Chegirmadan keyingi narx: ${narx_chegirma:.2f}")
print(f"Soliq miqdori: ${soliq:.2f}")
print(f"Yakuniy narx: ${yakuniy_narx:.2f}")
