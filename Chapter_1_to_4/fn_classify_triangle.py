#TS
# Exercise: fn_classify_triangle.py
# Topics: if / else / relational
#
# Skriv et program som finner ut hvilken _type_ et triangel er:
# Hvis alle sider er like lange er det et equilateral triangel
# Hvis to av sidene er like lange er det et isosceles triangel
# Hvis ingen sider er lik med en annen er det et scalene triangel,
# men kun hvis det er slik at de to katetrene summert ikke er mindre
# eller lik hypotenusen, da er det ikke et triangel
# Les 3 sider (float) fra brukeren og skriv deretter ut navnet på 
# det aktuelle triangelet
# Vi antar at det ikke gis inn negative tall, så du behøver ikke
# å skrive kode for å takle det
#
# Eksempel på kjøring (1):
# Length of side 1: 1
# Length of side 2: 2
# Length of side 3: 3
# The given values do not represent a triangle
# 
# Eksempel på kjøring (2):
# Length of side 1: 3
# Length of side 2: 3
# Length of side 3: 3
# The triangle's type is equilateral
#TE

side1 = float(input("Length of side 1: "))
side2 = float(input("Length of side 2: "))
side3 = float(input("Length of side 3: "))

if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
    print("The given values do not represent a triangle")
    quit()
if side1 == side2 and side2 == side3: # == er transitiv...
    tri_type = "equilateral"
elif side1 == side2 or side2 == side3 or side3 == side1:
    tri_type = "isosceles"
else:
    tri_type = "scalene"

print(f"The triangle's type is {tri_type}")