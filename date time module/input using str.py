# ĮVESTIS
# sukursime savo ivesties formatą, naudojant kaukes - formato apibrėžimui
# ir str - įvesčiai
# .strptime - metodas naudoja kaukes, duomenų atpažinimui - https://strftime.org/
ivestis = "2020-02-11"
my_datetime = datetime.datetime.strptime(ivestis, "%Y-%m-%d")
print(my_datetime)

ivestis = "2020.02.15, 10:11:59"
my_datetime = datetime.datetime.strptime(ivestis, "%Y.%m.%d, %H:%M:%S")
print(my_datetime)