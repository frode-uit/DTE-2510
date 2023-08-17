#TS
# Exercise: fn_calculate_age
#
# Lag et program som leser ditt navn og årstall født, samt dette år
# Deretter skriver ut ditt navn og hvor gammel du er
# Skriv to varianter, med og uten bruk av f-string

# Eksempel på kjøring:
# Hva er ditt navn?: Frode
# År født: 1970
# Dette år: 2023
# Hei Frode, du er 53 år
#TE

name = input("Hva er ditt navn?")
year_born = int(input("År født:"))
year_now = int(input("Dette år:"))
age = year_now - year_born
print("Hei ", name, ", du er ", age, " år", sep="")
# med f-string
print(f'Hei {name}, du er {age} år')