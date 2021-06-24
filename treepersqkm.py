#Problem Statement:
#treepersqkm is a dictionary showing the tree number of countries per square kilometer for random countries with sizeable population numbers. 
#Write a function named "moretrees" that returns a list of country names with less than 20000 trees per square kilometer. 
#treepersqkm = {"Finland":90652, "Taiwan": 69593, "Japan": 49894, "Russia": 41396, "Brazil": 39542, "India": 11109, "Denmark": 6129, "Syria": 534, "Saudi Arabia": 1}

#Solution:
def moretrees():
    for key, value in treepersqkm.items():
        if value<=20000:
            print(key,'-',value)

treepersqkm = {"Finland": 90652, "Taiwan": 69593, "Japan": 49894, "Russia": 41396, "Brazil": 39542, "India": 11109, "Denmark": 6129, "Syria": 534, "Saudi Arabia": 1}

print("\n\nCountries with less than 20,000 trees per sq.km.:")
moretrees()
