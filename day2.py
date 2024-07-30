print("Selamat datang di tip calculator! <3")
total = float(input("Berapa total billnya? $"))
tip = int(input("Mau kasih persenan berapa ni? 10%/12%/15%?\n"))
orang = int(input("Ada berapa orang untuk split bill?"))
dibayar = ((tip / 100) * total) + total
pembagian = dibayar / orang
hasil = round(pembagian, 2)
hasil = "{:.2f}".format(hasil) # ini supaya 0 dibelakang koma itu terbaca
print("Yang harus dibayar pe orang adalah",hasil)