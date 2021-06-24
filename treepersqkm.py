def moretrees():
    for key, value in treepersqkm.items():
        if value<=20000:
            print(key,'-',value)

treepersqkm = {"Finland": 90652, "Taiwan": 69593, "Japan": 49894, "Russia": 41396, "Brazil": 39542, "India": 11109, "Denmark": 6129, "Syria": 534, "Saudi Arabia": 1}

print("\n\nCountries with less than 20,000 trees per sq.km.:")
moretrees()
