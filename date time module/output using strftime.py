# IŠVESTIS,
# taip pačiai sudaroma kaukė, tačiau naudojamas kitas metodas,
# įvesties nepateikiama, naudojamas jau sukurtas datetime objektas
# strftime metodas
print(my_datetime)  # 2020-02-15 10:11:59
print(my_datetime.strftime("%d %m %Y"))  # 15 02 2020
print(my_datetime.strftime("%d %B %Y"))  # 15 February 2020