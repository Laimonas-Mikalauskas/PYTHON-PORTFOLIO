months_str = "sausis vasaris kovas"  # str
print(months_str)  # sausis vasaris kovas  # sausis vasaris kovas

# str metodas .split() - padalina str į listą
# per nurodytą simbolį
months_list = months_str.split(" ")
print(months_list)  # ['sausis', 'vasaris', 'kovas']

# months_list = months_str.split("a")
# print(months_list)  # ['s', 'usis v', 's', 'ris kov', 's']

# str metodas .join() - sujungia stringų dalis į vieną stringą
# naudodamas skirtuką
joined_str = " ".join(months_list)
print(joined_str)  # sausis vasaris kovas

joined_str = "---".join(months_list)
print(joined_str)  # sausis---vasaris---kovas