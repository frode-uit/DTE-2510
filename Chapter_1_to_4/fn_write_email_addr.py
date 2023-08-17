#TS
# Exercise: fn_write_email_addr
#
# Lag et program som lager en epost adresse basert på
# 1. fornavnet ditt
# 2. etternavnet ditt
# 3. domenet gmail.com
# Lagre disse i 3 variabler med fornuftige navn, og lag 
# deretter en epost adresse ved hjelp av en f-string
# Programmet ditt trenger ikke å lese noe input fra bruker
# Eksempel på kjøring:
# 
# Fornavn: mittfornavn
# Etternavn: mittetternavn
# Epost adressen blir: mittfornavn.mittetternavn@gmail.com
#TE

first_name = "mittfornavn"
last_name = "mittetternavn"
domain = "gmail.com"
print("Fornavn:", first_name)
print("Etternavn:", last_name)
email_address = f"{first_name}.{last_name}@{domain}"
print("Epost adressen blir:",email_address)