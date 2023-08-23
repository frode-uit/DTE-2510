#TS
# Exercise: fn_name_shape.py
# Topics: if / else / relational
#
# Skriv et program som bestemmer navnet på en geometrisk figur
# ut fra antall sider.
# Les antall sider fra brukeren og skriv deretter ut navnet på 
# den aktuelle geometriske figuren
# Programmet ditt skal støtte former med alt fra 3
# opp til (og inkludert) 6 sider.
# Hvis et antall sider utenfor dette området gis som input
# skal programmet  gi en passende feilmelding og avslutte
# TE

sides = int(input("Antall sider i figuren: "))
if sides > 6 or sides < 3:
    print("Feil antall sider, må være <=6 eller <=3")
    quit()
print("Figuren er et ", end="")
if sides == 3:
    print("triangel")
elif sides == 4:
    print("rektangel")
elif sides == 4:
    print("rektangel")
elif sides == 5:
    print("pentagon")
elif sides == 6:
    print("hexagon")