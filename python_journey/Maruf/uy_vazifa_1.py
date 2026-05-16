#  Ma'lumotlar
t_yil, t_oy, t_kun = 2008, 1, 24
h_yil, h_oy, h_kun = 2026, 5, 16

# Yil va oy farqini kunlarga aylantiramiz
yillar_kuni = (h_yil - t_yil) * 365
oylar_kuni = (h_oy - t_oy) * 30
kunlar_farqi = h_kun - t_kun

# Agar kun manfiy bo'lsa, bir oy (30 kun) qarz olamiz
if kunlar_farqi < 0:
    oylar_kuni -= 30
    kunlar_farqi += 30
    
    yashagan_kunlar = yillar_kuni + oylar_kuni + kunlar_farqi
    print(f"Siz taxminan {yashagan_kunlar} kundan beri yashayapsiz!")