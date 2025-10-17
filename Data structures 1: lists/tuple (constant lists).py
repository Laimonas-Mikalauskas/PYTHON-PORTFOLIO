# data type - tuple, list where changes are not allowed

months = ('january', 'february', 'march', 'april', 'may', 'june', 'january')

print(type(months))  # <class 'tuple'>

for elem in months:
    print(elem)  # january ..

# index is possible
print(months[0])  # january

# slice
print(months[1:])  # ('february', 'march', 'april', 'may', 'june', 'january')

# operations of change is impossible (CRASH)
# del months[0]
# months[0] = "december"

# only 2 methods are possible, they are working with lists also
# .index() - returns index of element
print(months.index("may"))  # 4

# .count() - count the repeating of elements by meaning
print(months.count("january"))  # 2

# add to tuple by rewriting the original
months = months + ("november", "december")
print(months)  # ('january', 'february', 'march', 'april', 'may', 'june', 'january', 'november', 'december')