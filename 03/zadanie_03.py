# Ćwiczenie 03 — Zadanie 3 — Wyznaczanie liczby π metodą Monte Carlo
#
# Napisz program szacujący wartość liczby π przez losowanie punktów. Następnie porównaj
# dokładność i czas obliczeń dla różnych liczb punktów.
#
# Losujemy punkty `(x, y)` równomiernie w kwadracie `[-1, 1] × [-1, 1]`. Punkt leży wewnątrz
# koła jednostkowego lub na jego brzegu, jeżeli:
#
# x**2 + y**2 <= 1
#
# Pole kwadratu wynosi `4`, a pole koła jednostkowego wynosi π. Stąd przybliżenie:
#
# pi_przyblizone = 4 * liczba_punktow_w_kole / liczba_wszystkich_punktow
#
# **Wymagania:**
#
# 1. Pobierz od użytkownika całkowite ziarno generatora oraz dodatnią liczbę całkowitą
# powtórzeń `r`. Na początek przyjmij ziarno `42` i `r = 3`.
# 2. Zdefiniuj funkcję `oszacuj_pi(n)`, która losuje `n` punktów za pomocą
# `random.uniform(-1, 1)` i zwraca przybliżenie π oraz liczbę punktów w kole. Nie przechowuj
# wszystkich współrzędnych — wystarczy licznik trafień.
# 3. Wykonaj po `r` osobnych symulacji dla każdej wartości `n`: `1000`, `10_000`, `100_000`.
# Użyj zagnieżdżonych pętli. Ziarno ustaw raz, przed całą serią.
# 4. Dla każdej symulacji oblicz błąd bezwzględny `abs(pi_przyblizone - math.pi)` oraz
# zmierz czas wykonania samej funkcji `oszacuj_pi()` przez `time.perf_counter()`.
# 5. Zapisz każdą próbę w pliku `wyniki_pi.tsv`, w kolumnach: `ziarno`, `n`, `powtorzenie`,
# `w_kole`, `pi`, `blad`, `czas_s`. Numeruj powtórzenia od `1`. Przybliżenie i błąd zapisuj
# z sześcioma miejscami po przecinku, czas z dziewięcioma.
# 6. Wyświetl i zapisz w `podsumowanie_pi.txt` średnie przybliżenie π, średni błąd
# bezwzględny i średni czas dla każdej wartości `n`. Średni błąd to średnia błędów
# poszczególnych prób, a nie błąd średniego przybliżenia.
# 7. Po wykonaniu programu dopisz do `podsumowanie_pi.txt` 2–3 zdania własnego komentarza:
# jak zwiększenie liczby punktów wpłynęło na dokładność i czas w Twoich wynikach?
#
# **Sprawdź:** dla `r = 3` tabela powinna zawierać `9` wierszy danych. Wynik każdej próby
# musi należeć do przedziału `[0, 4]`. Powtórne uruchomienie z tym samym ziarnem i
# parametrami w tym samym środowisku powinno odtworzyć wyniki liczbowe; czasy mogą się
# różnić.
#
# **Uwaga:** większa liczba punktów nie gwarantuje mniejszego błędu w każdej pojedynczej
# próbie. To metoda losowa. Podczas pomiaru nie wypisuj każdego punktu ani nie stosuj
# `sleep()`.

# Rozwiązanie:

