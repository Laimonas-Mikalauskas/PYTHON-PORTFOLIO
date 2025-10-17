# keletos žodynų sujungimas
bonus_info = {"engine": 2, "interior": "leather"}
auto.update(bonus_info)
print(auto)  # {'make': 'BMW', 'model': 'x5', 'colors': ['red', 'white', 'black'], 'engine': 2, 'interior': 'leather'}

auto.update({"year": 2000, "eco2000": True})
print(auto)  # {'make': 'BMW', 'model': 'x5', 'colors': ['red', 'white', 'black'], 'engine': 2, 'interior': 'leather', 'year': 2000, 'eco2000': True}