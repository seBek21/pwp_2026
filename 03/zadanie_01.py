# Ćwiczenie 03 — Zadanie 1 — Raport z pomiarów laboratoryjnych
#
# Napisz program analizujący plik tekstowy zawierający po jednym pomiarze w wierszu. W pliku
# mogą występować także puste wiersze i komentarze zaczynające się od `#`. Załóż, że plik
# zawiera co najmniej jeden pomiar, a każdy wiersz z pomiarem zawiera jedną skończoną
# liczbę.
#
# **Wymagania:**
#
# 1. Pobierz od użytkownika ścieżkę do pliku. Do pierwszej próby użyj `dane/pomiary.txt`.
# 2. Zdefiniuj funkcję `wczytaj_pomiary(nazwa_pliku)`, która zwraca listę pomiarów.
# 3. Po usunięciu skrajnych białych znaków pomijaj puste wiersze i komentarze. Pozostałe
# wiersze przekonwertuj na liczby przez `float()`. Wartości ujemne są dozwolone.
# 4. Zdefiniuj funkcję `statystyki(pomiary)`, która zwraca słownik z liczbą pomiarów,
# minimum, maksimum, średnią arytmetyczną i odchyleniem standardowym populacji.
# 5. Odchylenie policz według wzoru poniżej, używając pętli i `math.sqrt()`.
# 6. Wyświetl podsumowanie i zapisz je do `raport_pomiary.txt` w trybie `w`. Raport ma
# zawierać także datę analizy. Średnią i odchylenie zapisz z sześcioma miejscami po
# przecinku.
#
# **Wzory:** dla `n` pomiarów `x_1, ..., x_n`:
#
# srednia = (x_1 + ... + x_n) / n
# odchylenie = sqrt(((x_1 - srednia)**2 + ... + (x_n - srednia)**2) / n)
#
# Używamy mianownika `n`. Dla pojedynczego pomiaru odchylenie wynosi `0`.
#
# **Sprawdź:** w dołączonym pliku wartości to `10`, `12`, `14`, `16`. Średnia wynosi `13`, a
# odchylenie około `2.236068`. Sprawdź też plik z jednym pomiarem oraz plik z kilkoma takimi
# samymi pomiarami.

# Rozwiązanie:

