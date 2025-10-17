# f-stringai formatuoti stringai, galintys priimti į
# stringą bet kokius duomenis
month = "sausis"
day = 31
ftext = f"Mėnesis yra {month}, diena {day}d."
print(ftext)  # Mėnesis yra sausis, diena 31d.
ftext = f"Mėnesis yra {month}, diena {day - 1}d."
print(ftext)  # Mėnesis yra sausis, diena 30d.