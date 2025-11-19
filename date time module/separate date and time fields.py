# datetime.datetime objektas turi savybes(laukus)
# į kuriuos galima kreiptis, jie saugo atskiras datos-laiko
# sudedamąsias dalis(keisis vis išnaujo paleidus, nes ėmėm šio momento datą laiką)
res_year = dt_res.year
print(res_year)  # 2024
print(type(res_year))  # <class 'int'>

print(dt_res.month)
print(dt_res.day)
print(dt_res.hour)
print(dt_res.minute)
print(dt_res.second)
print(dt_res.microsecond)