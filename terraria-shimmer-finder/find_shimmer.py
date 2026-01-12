from guide_name import wybierz_imie

def main():
    c = wybierz_imie()
    jaki_swiat_i_jngl(c)

def jaki_swiat_i_jngl(znana):
    swiat = int(input("Określ wielkość świata:\n0: Mały\n1: Średni\n2: Duży\n"))
    jngl = int(input("Wybierz czy dżungla jest po: \n0: Lewej\n1: Prawej\n"))

    # Wielkość świata:    mały          średni         duży
    wielkosc_swiata = [[3800, 3276], [6000, 4992], [8000, 6552]]
    wybrana = wielkosc_swiata[swiat][jngl]
    del wielkosc_swiata[swiat][jngl]
    odrzucona = wielkosc_swiata[swiat][0]
    
    if wybrana > odrzucona:
        wynik = wybrana - ((wybrana-odrzucona) * znana)
        return print(f"Smimmer jest wskazanie kompasa {int(wynik)} w lewo, czyli {int(wynik/2)} kroków.")
    else:
        wynik = wybrana + ((odrzucona-wybrana) * znana)
        return print(f"Smimmer jest wskazanie kompasa {int(wynik)} w prawo, czyli {int(wynik/2)} kroków.")

main()