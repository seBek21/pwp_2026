# Ćwiczenie 03 — Zadanie 5 — Własna ruletka z saldem i historią gry
#
# Zbuduj konsolową ruletkę europejską z polami od `0` do `36`. Gracz zaczyna z saldem `1000`
# wirtualnych żetonów i może rozegrać wiele rund.
#
# **Kolory pól:**
#
# - `0` — zielony;
# - czerwone pola:
#
#   czerwone = {
#       1, 3, 5, 7, 9, 12, 14, 16, 18,
#       19, 21, 23, 25, 27, 30, 32, 34, 36
#   }
#
# - pozostałe liczby z zakresu `1–36` — czarne.
#
# Kolorów nie wyznaczaj na podstawie parzystości — np. `12` jest czerwone, a `11` czarne.
#
# **Dostępne zakłady:**
#
# | Typ zakładu | Dozwolone typowanie | Warunek wygranej | Wypłata po wygranej |
# |---|---|---|---:|
# | `liczba` | liczba całkowita `0–36` | dokładne trafienie liczby | `36 * stawka` |
# | `kolor` | `czerwony` lub `czarny` | trafienie koloru | `2 * stawka` |
# | `parzystosc` | `parzyste` lub `nieparzyste` | trafienie parzystości liczby z zakresu
# `1–36` | `2 * stawka` |
#
# W jednej rundzie gracz wybiera **jeden** typ zakładu i jedno typowanie. Dla wyniku `0`
# wszystkie zakłady na kolor i parzystość przegrywają. Na zero można postawić przez zakład
# typu `liczba`.
#
# **Rozliczanie salda:** najpierw odejmij stawkę, a po losowaniu dodaj wypłatę. Przy
# przegranej wypłata wynosi `0`. Wypłata obejmuje zwrot postawionej stawki.
#
# saldo_po = saldo_przed - stawka + wyplata
#
# Przykład dla salda `1000` i stawki `10`:
#
# - trafienie liczby: `1000 - 10 + 360 = 1350`;
# - trafienie koloru: `1000 - 10 + 20 = 1010`;
# - przegrana: `1000 - 10 + 0 = 990`.
#
# **Wymagania:**
#
# 1. Zdefiniuj funkcję `kolor_liczby(n)`, która dla numeru pola z zakresu `0–36` zwraca
# `zielony`, `czerwony` albo `czarny`.
# 2. Zdefiniuj funkcję `oblicz_wyplate(typ_zakladu, typowanie, stawka, wynik)`, która zwraca
# wypłatę. Dla typu `liczba` typowanie jest liczbą całkowitą; dla pozostałych typów —
# napisem z tabeli.
# 3. Zdefiniuj funkcję `ruletka()`, która prowadzi grę w pętli `while`. Przed rundą pokaż
# saldo i pobierz rodzaj zakładu. Wpisanie `koniec` zamiast rodzaju zakładu ma kończyć
# sesję.
# 4. Pobierz typowanie i stawkę. Załóż, że gracz wybiera zakłady i typowania z tabeli oraz
# podaje dodatnią całkowitą stawkę nieprzekraczającą salda. Odpowiedzi tekstowe sprowadź do
# małych liter i usuń skrajne spacje.
# 5. Odejmij stawkę i wylosuj jeden wynik przez `random.randint(0, 36)`. W każdej rozegranej
# rundzie wykonuj dokładnie jedno losowanie.
# 6. Wyświetl wylosowaną liczbę, jej kolor, wynik zakładu, wypłatę i nowe saldo. Grę zakończ
# po wpisaniu `koniec` albo po wyczerpaniu żetonów. Nie dodawaj uzupełniania salda.
# 7. Na początku sesji utwórz plik `historia_ruletki.tsv` w trybie `w` i zapisz nagłówki:
# `czas`, `runda`, `typ`, `typowanie`, `stawka`, `wynik`, `kolor`, `wyplata`, `saldo`. Po
# każdej rozegranej rundzie dopisz jeden wiersz. Numeruj rundy od `1`.
# 8. Na końcu wyświetl i zapisz do `podsumowanie_ruletki.txt`: liczbę rozegranych rund,
# liczbę wygranych i przegranych, procent wygranych, saldo końcowe, bilans względem
# początkowych `1000` żetonów i czas sesji. Czas mierz przez `time.perf_counter()` od
# pierwszego pytania o rodzaj zakładu do zakończenia gry — obejmuje również namysł gracza.
# 9. Uwzględnij zakończenie sesji przed pierwszym losowaniem: liczba rund i procent
# wygranych wynoszą wtedy `0`, a saldo pozostaje równe `1000`.
#
# **Sprawdź funkcje niezależnie od losowań:**
#
# kolor_liczby(0)  # "zielony"
# kolor_liczby(12)  # "czerwony"
# kolor_liczby(11)  # "czarny"
#
# oblicz_wyplate("liczba", 7, 10, 7)  # 360
# oblicz_wyplate("liczba", 0, 10, 0)  # 360
# oblicz_wyplate("kolor", "czarny", 10, 11)  # 20
# oblicz_wyplate("kolor", "czerwony", 10, 11)  # 0
# oblicz_wyplate("parzystosc", "parzyste", 10, 12)  # 20
# oblicz_wyplate("parzystosc", "parzyste", 10, 0)  # 0
#
# Sprawdź także stawkę równą całemu saldu i zakończenie gry bez rozegrania rundy. Nie
# zmieniaj zasad rozliczania po zobaczeniu wylosowanego wyniku.

# Rozwiązanie:

