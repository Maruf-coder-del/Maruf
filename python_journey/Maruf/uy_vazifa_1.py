# Mening yoshim kerak bo'lgan kod
tugilgan_yil = 2008 # Meni tug'ilgan yilim
tugilgan_oy = 1
tugilgan_kun = 24

hozirgi_yil = 2026
hozirgi_oy = 5
hozirgi_kun = 15

# Hisob-kitob bu yerda
yashagan_kunlar = (hozirgi_yil - tugilgan_yil) * 365 + (hozirgi_oy - tugilgan_oy) * 30 + (tugilgan_kun - hozirgi_kun)

print(f"Siz {yashagan_kunlar} kundan beri yashayapsiz!") 