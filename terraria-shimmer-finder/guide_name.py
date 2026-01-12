def wybierz_imie():
    slownik_imion = {
        "Joe":0.0000,
        "Connor":0.0278,
        "Tanner":0.0566,
        "Wyatt":0.0833,
        "Cody":0.1111,
        "Levi":0.1389,
        "Luke":0.1667,
        "Jack":0.1944,
        "Scott":0.2222,
        "Logan":0.2500,
        "Cole":0.2778,
        "Asher":0.3056,
        "Bradley":0.3333,
        "Jacob":0.3611,
        "Garrett":0.3889,
        "Dylan":0.4167,
        "Maxwell":0.4444,
        "Steve":0.4722,
        "Brett":0.5000,
        "Andrew":0.5278,
        "Harley":0.5556,
        "Kyle":0.5833,
        "Jake":0.6111,
        "Ryan":0.6389,
        "Jeffrey":0.6667,
        "Seth":0.6944,
        "Marty":0.7222,
        "Brandon":0.7500,
        "Zach":0.7778,
        "Jeff":0.8056,
        "Daniel":0.8333,
        "Trent":0.8611,
        "Kevin":0.8889,
        "Brian":0.9167,
        "Colin":0.9444,
        "Jan":0.9722
    }

    print("(Musi być pierwsze imie jakie otrzyma guide!)")
    x = input("Podaj imię: ").title().strip()

    while x not in slownik_imion:
        print("Guide nie może się tak nazywać.")
        x = input("Podaj poprawne imie: ")
    else:
        return slownik_imion[x]
