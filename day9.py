#### Auction Bid - Project Day 9
dict_bid = {}
while True :
    print(f"Selamat datang di Lelang Online!")
    nama = (str(input("Siapa nama Anda?")))
    print(nama)
    price = (int(input("Mau menawar berapa?")))
    print(f"{nama} menawar Rp{price}")
    dict_bid[nama] = price
    ask = str(input("Apakah ada orang yang menawar lagi? y/t"))
    if ask == "y" :
        continue
    elif ask == "t":
        break
    else :
        break


keymax = max(zip(dict_bid.values(),dict_bid.keys()))[1]
valuemax = max(zip(dict_bid.values(),dict_bid.keys()))[0]

print(f"Pemenangnya {keymax} dengan harga Rp{valuemax}")
#kalo harga sama di program ini dia menang yang paling akhir nawar