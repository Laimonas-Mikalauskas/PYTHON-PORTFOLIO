res = person_info["name"]
print(res)   # Albert

print(person_info["surname"])  # Einstein

print(person_info["languages"])  # ['German', 'Latin', 'Italian', 'English']
print(person_info["languages"][1])  # Latin
print(person_info["languages"][2])  # Italian

print(person_info["occupation"])   # {'role': 'Professor', 'workplace': 'Uni of Berlin'}
print(person_info["occupation"]["role"])   # Professor
print(person_info["occupation"]["workplace"])   # Uni of Berlin