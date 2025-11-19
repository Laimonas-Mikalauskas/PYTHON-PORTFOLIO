# laiko skirtumo objektą mes galim pridėti arba atimti iš datos laiko,
# gaudami kitą datetime objektą
# skaičiavimams dažniausiai patogiau sudaryti naują timedelta objektą,
# iškvietus jo klasę
skirtumas = datetime.timedelta(hours=1000)
print(skirtumas)
res = dabar + skirtumas
print(res)

skirtumas = datetime.timedelta(days=1000, hours=100, minutes=100)
print(skirtumas)
res = dabar - skirtumas
print(res)