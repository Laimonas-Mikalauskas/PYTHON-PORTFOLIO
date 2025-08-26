def zaidejo_info(func):
    def info(vardas, taskai, kamuoliai):
        print("Ryto žaidėjo statistika")
        func(vardas, taskai, kamuoliai)
    return info

@zaidejo_info
def statistika(vardas, taskai, kamuoliai):
    print(f"{vardas}: {taskai} taškai, {kamuoliai} atkovoti kamuoliai")

statistika("Margiris Normantas", 18, 6)