months = ['sausis', 'vasaris', 'kovas', 'balandis', 'gegužė', 'birželis']

# indeksavimas
print(months[0])  # sausis
print(months[-1])  # birželis

# sliceinimas
print(months[1:4])  # ['vasaris', 'kovas', 'balandis']
print(months[1:3 + 1])  # ['vasaris', 'kovas', 'balandis']
print(months[1:])  # ['vasaris', 'kovas', 'balandis', 'gegužė', 'birželis']
print(months[:5])  # ['sausis', 'vasaris', 'kovas', 'balandis', 'gegužė']

# žingsniai
print(months[::3])  # kas trečias - ['sausis', 'balandis']
print(months[::-1])  # atvirkščiai - ['birželis', 'gegužė', 'balandis', 'kovas', 'vasaris', 'sausis']
print(months[::-2])  # atvirkščiai kas antrą - ['birželis', 'balandis', 'vasaris']

# papildomos operacijos po 1 elemento ištraukimo
# gavę stringą pagal indeksą liste, papildomai indeksuojam stringą,
# ištraukiam iš stringo 1 indeksu esantį simbolį
print(
    months[0][1]  # a
)

# suvykdom stringui vieną iš stringų metodų
print(
    months[1].upper()  # VASARIS
)