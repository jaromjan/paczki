# Drugi program - ładowaczka paczek

# Tworzymy szablon do wypisywania
szablon = "Ilość elementów {}\n" \
          "Wagi elementów: {}\n" \
          "\n" \
          "Podsumowanie:\n" \
          "\n" \
          "Wysłano {} paczek ({})\n" \
          "Razem wysłano {}kg\n" \
          "Suma pustych kilogramów {}kg\n" \
          "Najwięcej pustych kilogramów ma paczka {} ({}kg)\n"

# Deklarujemy zmienne
podsumowanie_all = ''
il_paczek = 0
zawartosc_paczek = ''
suma_wyslane = 0
suma_puste = 0
nr_maks_pusta = 0
waga_maks_pusta = 0
waga_sum = 0
podsumowanie = ''
podsumowanie_old = ''
separator = ''
puste_w_paczce = 0

# Pobieramy dane ilość elementów
zakres = int(input("Podaj ile elementów chcesz wysłać <int>: "))
for x in range(zakres):
# Pobieramy i sprawdzamy podane wagi w pętli
    waga = int(input("Podaj wagę elementu <int> (1-10): "))
    while waga < 1 or waga > 10:
            print("Podaj liczbę całkowitą z zakresu 1 - 10")
            waga = 0
            waga = int(input("Podaj wagę elementu: "))
# Zliczamy wprowadzane wagi elementów
    waga_sum = waga_sum + waga
# Przygotowujemy dane do wyświetlenia zebranych wartości
    if podsumowanie == '' or waga == 0:
        separator = ''
    else:
        separator = " + "
    podsumowanie_old = podsumowanie
    podsumowanie = str(podsumowanie) + separator + str(waga)
    podsumowanie_all = str(podsumowanie_all) + separator + str(waga)
    suma_wyslane = suma_wyslane + waga
# Przygotowujemy paczki


    while waga_sum > 20:
# Wyliczamy wagę paczki  po przekroczeniu 20kg
        waga_paczki = waga_sum - waga
# Numerujemy paczki
        il_paczek += 1
# Liczymy puste kg w paczce i zbieramy do wyświetlenia
        puste_w_paczce = 20 - waga_paczki
        suma_puste = suma_puste + puste_w_paczce
# Przypisujemy element , który się nie zmieścił dla kolejnej paczki
        podsumowanie  = waga
        waga_sum = waga_sum - waga_paczki
# Szukamy najbardziej pustej paczki
        if waga_maks_pusta <= puste_w_paczce:
            waga_maks_pusta = puste_w_paczce
            nr_maks_pusta = il_paczek
# Zbieramy zawartość poszczególnych paczek
        zawartosc_paczek = zawartosc_paczek + " , " + podsumowanie_old
# Kontrolne , potem wywal
        print(f"Wysłano paczke nr {il_paczek} o wadze:",waga_paczki, "kg(",podsumowanie_old,"), pustych kg:", puste_w_paczce)
        print(podsumowanie_old)
# TODO dokończ ostatnią paczkę i wyskoczenie po błędzie z wysłaniem ostatniej paczki + doliczenie do zestawienia

        if not waga:
            print("Wprowadzono pustą wartość przerwanie wprowadzania")
            if waga_sum:
                print(f"Wysłano paczke nr {il_paczek + 1} o wadze:",waga_sum,"kg(",podsumowanie_old,"), pustych kg:", 20 - waga_sum)
            break



komunikat = szablon.format(zakres, podsumowanie_all, il_paczek, zawartosc_paczek, suma_wyslane, suma_puste, nr_maks_pusta, waga_maks_pusta)
if zakres == 0:
    komunikat = "Podano błedną ilość elementów - podaj wartość całkowitą większą od zera"

print(komunikat)

"""

waga_sum = 0
waga_pom = 0
il_paczek = 0
waga_paczki = 0
puste_kg = 0
podsumowanie = ''
podsumowanie_all = ''
podsumowanie_old = ''
separator = ''
zakres = int(input("Podaj ile elementów chcesz wysłać <int>: "))
for x in range(zakres):
    waga = input("Podaj wagę elementu: ")

    if not waga and int():
            waga = 0
    else:
            waga = int(waga)
    waga_pom = waga
    waga_sum = waga_sum + waga

    print(waga_sum)

    if podsumowanie == '' or waga == 0:
        separator = ''
    else:
        separator = " + "
    podsumowanie_old = podsumowanie
    podsumowanie = str(podsumowanie) + separator + str(waga)

    while waga_sum > 20:
        waga_paczki = waga_sum - waga
        il_paczek += 1
        podsumowanie  = waga
        print(f"Wysłano paczke nr {il_paczek} o wadze:",waga_paczki, "kg(",podsumowanie_old,"), pustych kg:", 20 - waga_paczki)
        print(podsumowanie_old)
        waga_sum = waga_sum - waga_paczki

    if not waga:
        print("Wprowadzono pustą wartość przerwanie wprowadzania")
        if waga_sum:
            print(f"Wysłano paczke nr {il_paczek + 1} o wadze:",waga_sum,"kg(",podsumowanie_old,"), pustych kg:", 20 - waga_sum)
        break
"""


