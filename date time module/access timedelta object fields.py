# SVARBU! timedelta objekto laukai
print(skirtumas.days)  # dienomis
print(skirtumas.seconds)  # valandinė dalis atlikusi nuo dienų
print(skirtumas.seconds / 60 / 60)  # seconds valandomis

# VISOS laiko tarpo sekundės
sekundes = skirtumas.total_seconds()
print(sekundes)