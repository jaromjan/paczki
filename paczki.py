# Drugi program - ladowaczka paczek
# Tworzymy szablon do wypisywania
szablon = "\nIlość elementów {}\n" \
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
separator_zawartosci = ''
puste_w_paczce = 0
# Pobieramy dane o ilosci elementow
zakres = int(input("Podaj ile elementów chcesz wysłać <int> (< 0): "))
for x in range(zakres):
    # Pobieramy i sprawdzamy podane wagi w petli
    waga = int(input("Podaj wagę elementu <int> (1 - 10): "))
    while waga < 1 or waga > 10:
            print("Podaj liczbę całkowitą z zakresu 1 - 10")
            waga = 0
            waga = int(input("Podaj wagę elementu <int> (1 - 10): "))
# Zliczamy wprowadzane wagi elementów
    waga_sum = waga_sum + waga
# Przygotowujemy dane do wyswietlenia zebranych wartosci
    if podsumowanie == '' or waga == 0:
        separator = ''
    else:
        separator = " + "
    podsumowanie_old = str(podsumowanie)
    podsumowanie = str(podsumowanie) + separator + str(waga)
    podsumowanie_all = str(podsumowanie_all) + separator + str(waga)
    suma_wyslane = suma_wyslane + waga
# Przygotowujemy paczki
    while waga_sum > 20:
        # Wyliczamy wage paczki  po przekroczeniu 20kg
        waga_paczki = waga_sum - waga
# Numerujemy paczki
        il_paczek += 1
# Liczymy puste kg w paczce i zbieramy do wyswietlenia
        puste_w_paczce = 20 - waga_paczki
        suma_puste = suma_puste + puste_w_paczce
# Przypisujemy element, ktory sie nie zmiescil dla kolejnej paczki
        podsumowanie = waga
        waga_sum = waga_sum - waga_paczki
# Szukamy najbardziej pustej paczki
        if waga_maks_pusta < puste_w_paczce:
            waga_maks_pusta = puste_w_paczce
            nr_maks_pusta = il_paczek
# Zbieramy zawartosc poszczegolnych paczek
        if not zawartosc_paczek:
            separator_zawartosci = ''
        else:
            separator_zawartosci = " , "
        zawartosc_paczek = zawartosc_paczek + separator_zawartosci + podsumowanie_old
# Konczymy wprowadzanie - jesli cos zostało wysylamy ostatnia paczka
    if x + 1 == zakres:
            if waga_sum:
                il_paczek = il_paczek + 1
                puste_w_paczce = 20 - waga_sum
                suma_puste = suma_puste + puste_w_paczce
                if waga_maks_pusta < puste_w_paczce:
                    waga_maks_pusta = puste_w_paczce
                    nr_maks_pusta = il_paczek
                if not zawartosc_paczek:
                    separator_zawartosci = ''
                else:
                    separator_zawartosci = " , "
                zawartosc_paczek = zawartosc_paczek + separator_zawartosci + str(podsumowanie)
            break
# Wypisujemy podsumowanie
komunikat = szablon.format(zakres, podsumowanie_all, il_paczek, zawartosc_paczek, suma_wyslane, suma_puste,
                           nr_maks_pusta, waga_maks_pusta)
if zakres == 0:
    komunikat = "Podano błedną ilość elementów wymagana liczba całkowita większa od zera - koniec programu"
print(komunikat)
