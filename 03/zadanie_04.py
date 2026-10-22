# Ćwiczenie 03 — Zadanie 4 — Minutnik interwałowy z dziennikiem
#
# Napisz program, który przeprowadza serię odcinków pracy i przerw, odlicza pozostały czas i
# zapisuje przebieg sesji do pliku.
#
# **Wymagania:**
#
# 1. Pobierz dodatnią liczbę odcinków pracy, czas jednego odcinka oraz czas przerwy. Oba
# czasy użytkownik podaje w formacie `HH:MM:SS`.
# 2. Zdefiniuj funkcję `czas_na_sekundy(tekst)`, która zwraca łączną liczbę sekund. Załóż,
# że zapis zawiera dokładnie trzy liczby całkowite: nieujemne godziny oraz minuty i sekundy
# z przedziału `0–59`. Dopuszczalne są np. `00:01:05` i `0:1:5`.
# 3. Przyjmij, że czas pracy jest większy od zera, a czas przerwy jest nieujemny.
# 4. Zdefiniuj funkcję `formatuj_czas(sekundy)`, która zwraca napis z godzinami, minutami i
# sekundami, np. `65` → `00:01:05`.
# 5. Zdefiniuj funkcję `odliczaj(sekundy, opis)`, która wyświetla opis etapu oraz pozostały
# czas, aktualizuje go mniej więcej co sekundę i kończy komunikatem `Czas minął!`. Zastosuj
# `while` oraz `time.sleep()`.
# 6. Wyznacz moment końca etapu przez `time.perf_counter()` i obliczaj pozostały czas na
# podstawie aktualnego odczytu. Do prezentacji zaokrąglaj dodatnią liczbę sekund w górę
# przez `math.ceil()`. Zakończenie odliczania ma zależeć od zegara, a nie wyłącznie od
# liczby wykonanych wywołań `sleep(1)`.
# 7. Pomiędzy kolejnymi odcinkami pracy uruchamiaj przerwę. Po ostatnim odcinku nie dodawaj
# przerwy; przerwę o długości zero pomijaj.
# 8. Do pliku `dziennik_minutnika.txt` dopisuj w trybie `a`: początek sesji z datą,
# parametry, początek i koniec każdego wykonanego etapu oraz planowany i rzeczywisty czas
# całej sesji. Rzeczywisty czas mierz od początku pierwszego odliczania do końca ostatniego,
# z pominięciem wcześniejszego wprowadzania danych.
#
# **Sprawdź:** dla `2` odcinków pracy po `00:00:03` i przerwy `00:00:02` kolejność to:
#
# Praca 1 → 3 sekundy
# Przerwa 1 → 2 sekundy
# Praca 2 → 3 sekundy
#
# Planowany czas wynosi `8` sekund; rzeczywisty może być nieco dłuższy. Sprawdź także sesję
# z jednym odcinkiem pracy oraz sesję z zerowym czasem przerwy.
#
# **Wskazówka:** obliczenia czasu wykonuj w sekundach. Na format `HH:MM:SS` przeliczaj wynik
# dopiero podczas wyświetlania.

# Rozwiązanie:

