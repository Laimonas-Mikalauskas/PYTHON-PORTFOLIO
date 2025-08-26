def player_info(func):
    def info(*args, **kwargs):
        print("Vilniaus Ryto komandos žaidėjo statistika")
        func(*args, **kwargs)
    return info

def uniform_info(func):
    def uniform(*args, **kwargs):
        print("Vilniaus ryto komandos simbolika")
        func(*args, **kwargs)
    return uniform

@player_info
@uniform_info
def show_info(name, points, balls, colors, logo, city):
    print(f"{name} renka {points} taškų ir atkovoja {balls} kamuolių ir komandos {colors} yra juoda balta raudona. Logotipas yra {logo} iš miesto {city}")

show_info("Margiris Normantas", 16, 6, "black white red", "Vilkas", "Vilnius")