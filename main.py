print "Hello it's l2craft\nAuthor: elshurito\n\n"
SpiritOrePrice = 440.0
DcryPrice = 602
Dgloves=22990
NumDGloves=0
NumSpiritOre=0

BSSD=0

print "input Spirit Ore Price\nSpirit Ore default price = ",SpiritOrePrice
#SpiritOrePrice = (input ())/1.0

print "input Dcry Price\nDcry default price = ",DcryPrice
#DcryPrice = (input ())/1.0

adena = (input ("input adena "))/1.0
startadena=adena
Dcry = (input ("input number of Dcry " ))/1.0
SpiritOre = (input ("input number of SpiritOre " ))/1.0

if (Dcry >= 2) and (SpiritOre >=8):
    while (Dcry >= 2) and (SpiritOre >=8):
        Dcry=Dcry-2
        SpiritOre=SpiritOre-8
        BSSD=BSSD+100


if (Dcry < 2) and (SpiritOre >= 8):
    while (SpiritOre >=8) and (adena > Dgloves):
        if adena >= Dgloves:
            adena=adena-Dgloves
            NumDGloves=NumDGloves+1
            Dcry=Dcry+38
            while (Dcry >=2) and (SpiritOre >=8):
                Dcry=Dcry-2
                SpiritOre=SpiritOre-8
                BSSD=BSSD+100
        else:
            break


if (Dcry >= 2) and (SpiritOre <8):
    while (Dcry >=2) and (adena >= ((8-SpiritOre) * SpiritOrePrice)):
        if adena >= ((8-SpiritOre)*SpiritOrePrice):
            Dcry=Dcry-2
            adena=adena-(8-SpiritOre)*SpiritOrePrice
            NumSpiritOre=NumSpiritOre+(8-SpiritOre)
            SpiritOre=0
            BSSD=BSSD+100
        else:
            break

while (adena > (Dgloves+8*19*SpiritOrePrice)):
    adena=adena-(Dgloves+8*19*SpiritOrePrice)
    NumDGloves=NumDGloves+1
    NumSpiritOre=NumSpiritOre+8*19
    Dcry=Dcry+38
    SpiritOre=SpiritOre+8*19
    while (Dcry >= 2) and (SpiritOre >= 8):
        Dcry=Dcry-2
        SpiritOre=SpiritOre-8
        BSSD=BSSD+100


while (adena > Dgloves):
    Dcry=Dcry+38
    adena=adena-Dgloves
    NumDGloves=NumDGloves+1
    while (adena >= SpiritOrePrice*8) and (Dcry >= 2):
        adena=adena-SpiritOrePrice*8
        NumSpiritOre=NumSpiritOre+8
        Dcry=Dcry-2
        BSSD=BSSD+100







print "total Blesed Spiritshot D grade = ",BSSD
print "free adena = ",adena
print "SpiritOre need = ",NumSpiritOre
print "DGloves need = ",NumDGloves
print "- - - - - -- - - - - - - - - - - - - - - - - - - - - -"
print "free Dcry = ",Dcry
print "free SpiritOre = ",SpiritOre
print "- - - - - -- - - - - - - - - - - - - - - - - - - - - -"
price = input ("prise BSSD ")/1.0

print "- - - - - -- - - - - - - - - - - - - - - - - - - - - -"
print "total adena = ",BSSD*price+adena
print "profit = ",BSSD*price-startadena+adena
raw_input ("press any key")
