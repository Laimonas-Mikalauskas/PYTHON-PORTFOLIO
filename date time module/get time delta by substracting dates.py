dabar = datetime.datetime.today()
mileniumas = datetime.datetime(2000, 1, 1)

# padarius atimtį datos-laiko iš datos-laiko, gaunamas kitas objektas
# laiko skirtumo(laiko tarpo) objektas datetime.timedelta
skirtumas = dabar - mileniumas
print(skirtumas)
print(type(skirtumas))  # <class 'datetime.timedelta'>