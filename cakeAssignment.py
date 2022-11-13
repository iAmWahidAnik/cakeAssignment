#Cake Raw Metarial Price
blackForest = 180
vanillaCake = 150
redVelvet = 220
lemonSpongeCake = 165
chocolateCake = 170

#Transportation Cost
transCost = 150

#Cake + Transportation Cost
blackForestWTC = blackForest+transCost
vanillaCakeWTC = vanillaCake+transCost
redVelvetWTC = redVelvet+transCost
lemonSpongeCakeWTC = lemonSpongeCake+transCost
chocolateCakeWTC = chocolateCake+transCost

#Utility Bill Cost
blackForestUtility = (blackForestWTC *3)/100
vanillaCakeUtility = (vanillaCakeWTC *3)/100
redVelvetUtility = (redVelvetWTC *3)/100
lemonSpongeCakeUtility = (lemonSpongeCakeWTC *3)/100
chocolateCakeUtility = (chocolateCakeWTC *3)/100

#Space Cost
spaceCost = 50

#Sales Cost
salesCost = 60

#Total Invention Cost Count
blackForestTotalI = blackForestWTC+blackForestUtility+spaceCost+salesCost
vanillaCakeTotalI = vanillaCakeWTC+vanillaCakeUtility+spaceCost+salesCost
redVelvetTotalI = redVelvetWTC+redVelvetUtility+spaceCost+salesCost
lemonSpongeCakeTotalI = lemonSpongeCakeWTC+lemonSpongeCakeUtility+spaceCost+salesCost
chocolateCakeTotalI = chocolateCakeWTC+chocolateCakeUtility+spaceCost+salesCost

#Print Total Invention Price
print("blackForest Per Pound Total Invention Price is : ", blackForestTotalI)
print("vanillaCake Per Pound Total Invention Price is : ", vanillaCakeTotalI)
print("redVelvet Per Pound  Total Invention Price is : ", redVelvetTotalI)
print("lemonSpongeCake Per Pound Total Invention Price is : ", lemonSpongeCakeTotalI)
print("chocolateCake Per Pound Total Invention Price is : ", chocolateCakeTotalI)

#Cake Sales Prices
blackForestSP = 780
vanillaCakeSP = 600
redVelvetSP = 800
lemonSpongeCakeSP = 650
chocolateCakeSP = 660

print("blackForest Sale Price Per Pound : ", blackForestSP)
print("vanillaCake Sale Price Per Pound : ", vanillaCakeSP)
print("redVelvet Sale Price Per Pound : ", redVelvetSP)
print("lemonSpongeCake Sale Price Per Pound : ", lemonSpongeCakeSP)
print("chocolateCake Sale Price Per Pound : ", chocolateCakeSP)

#Cake Discount Revinue
DLblackForest = ((750*5)/100)
DLvanillaCake = ((750*5)/100)
DLredVelvet = ((750*5)/100)
DLlemonSpongeCake = ((750*7)/100)
DLchocolateCake = ((750*7)/100)

#Cake Discounted Price
DPblackForest = blackForestSP-DLblackForest
DPvanillaCake = vanillaCakeSP-DLvanillaCake
DPredVelvet = redVelvetSP-DLredVelvet
DPlemonSpongeCake = lemonSpongeCakeSP-DLlemonSpongeCake
DPchocolateCake = chocolateCakeSP-DLchocolateCake

print("blackForest Discounted Sale Price Per Pound : ", DPblackForest)
print("vanillaCake Discounted Sale Price Per Pound : ", DPvanillaCake)
print("redVelvet Discounted Price Sale Per Pound : ", DPredVelvet)
print("lemonSpongeCake Discounted Sale Price Per Pound : ", DPlemonSpongeCake)
print("chocolateCake Discounted Sale Price Per Pound : ", DPchocolateCake)

#Total Revenue From Each Cake Per Pound
TRblackForest = DPblackForest-blackForestTotalI
TRvanillaCake = DPvanillaCake-vanillaCakeTotalI
TRredVelvet = DPredVelvet-redVelvetTotalI
TRlemonSpongeCake = DPlemonSpongeCake-lemonSpongeCakeTotalI
TRchocolateCake = DPchocolateCake-chocolateCakeTotalI

print("Total Profit From blackForest Per Pound :", TRblackForest)
print("Total Profit From vanillaCake Per Pound :", TRvanillaCake)
print("Total Profit From redVelvet Per Pound :", TRredVelvet)
print("Total Profit From lemonSpongeCake Per Pound :", TRlemonSpongeCake)
print("Total Profit From chocolateCake Per Pound :", TRchocolateCake)

#Total Sold Per Cake In Pound
TSblackForest = 5
TSvanillaCake = 7
TSredVelvet = 10
TSlemonSpongeCake = 5
TSchocolateCake =  9

print("Total Sale blackForest In Pound : ", TSblackForest)
print("Total Sale vanillaCake In Pound : ", TSvanillaCake)
print("Total Sale redVelvet In Pound : ", TSredVelvet)
print("Total Sale lemonSpongeCake In Pound : ", TSlemonSpongeCake)
print("Total Sale chocolateCake In Pound : ", TSchocolateCake)

#Total Sale Revenue Aftre Discount
TSRblackForest = TSblackForest*DPblackForest
TSRvanillaCake = TSvanillaCake*DPvanillaCake
TSRredVelvet =  TSredVelvet*DPredVelvet
TSRlemonSpongeCake = TSlemonSpongeCake*DPlemonSpongeCake
TSRchocolateCake = TSchocolateCake*DPchocolateCake

print("blackForest Total Sale Revenue Aftre Discount : ", TSRblackForest)
print("vanillaCake Total Sale Revenue Aftre Discount : ", TSRvanillaCake)
print("redVelve Total Sale Revenue Aftre Discount : ", TSRredVelvet)
print("lemonSpongeCake Total Sale Revenue Aftre Discount : ", TSRlemonSpongeCake)
print("chocolateCake Total Sale Revenue Aftre Discount : ", TSRchocolateCake)

#Total Profit Revenue Income
TPRblackForest = TSblackForest*TRblackForest
TPRvanillaCake = TSvanillaCake*TRvanillaCake
TPRredVelvet = TSredVelvet*TRredVelvet
TPRlemonSpongeCake = TSlemonSpongeCake*TRlemonSpongeCake
TPRchocolateCake = TSchocolateCake*TRchocolateCake

print("Total Profit Revenue blackForest : ", TPRblackForest)
print("Total Profit Revenue vanillaCake : ", TPRvanillaCake)
print("Total Profit Revenue redVelvet : ", TPRredVelvet)
print("Total Profit Revenue lemonSpongeCake : ", TPRlemonSpongeCake)
print("Total Profit Revenue chocolateCake : ", TPRchocolateCake)
