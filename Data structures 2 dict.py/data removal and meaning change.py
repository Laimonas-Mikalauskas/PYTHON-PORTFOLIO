# duomenų keitimas žodyne
del auto["eco2000"]
print(auto)

auto.pop("interior")
print(auto)

# raktų pervadinimas per reikšmės perkėlimą į naują raktą
auto["gas_engine"] = auto.pop("engine")
print(auto)

auto["year"] = 2001
print(auto)

auto["year"] += 10
print(auto)

auto["colors"].append("yellow")
print(auto)