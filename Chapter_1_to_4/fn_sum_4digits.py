#TS
# Exercise: fn_sum_4digits
# 
# Lag et program som tar imot et tall på fire siffer
# Programmet skal summere verdien av de enkelte sifrene
# Hint:
# Bruk modulo operatoren og dele operatoren for å løse oppgaven:
# 1234 % 10 gir 4, og 1234 // 10 gir 123
# bruk % og // annenhver gang for å hente ut alle sifrene
# 
# Eksempel på kjøring:
# 
# Gi inn et tall på fire siffer: 1234
# Summen av sifrene er 10
#TE

tallet = int(input("Gi inn et tall på fire siffer: "))
s4 = tallet % 10
tallet = tallet // 10
s3 = tallet % 10
tallet = tallet // 10
s2 = tallet % 10
s1 = tallet // 10

print("De enkelte sifrene:",s1,s2,s3,s4)
print("Summen av sifrene blir:", s1 + s2 + s3 + s4)