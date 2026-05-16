USD_TO_UZS = 12650 # Konstantalar katta harfda
dollar_miqdori = 157.5
som_miqdori = 1_000_000

# Konvertatsiya
dollar_somda = dollar_miqdori * USD_TO_UZS
som_dollarda = som_miqdori / USD_TO_UZS

print(f"{dollar_miqdori} USD = {dollar_somda:,.2f} UZS")
print(f"{som_miqdori} UZS = {som_dollarda:,.2f} USD". replace(",",""))