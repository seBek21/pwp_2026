"""
### Zadanie 4 — Czas, rozmiar kolekcji i iteratory

Porównaj obliczanie kwadratów liczb parzystych od 0 do `n - 1` trzema sposobami: pętlą z `append()`, listą składaną oraz `map()` z lambdą na wyniku `filter()` z lambdą.

1. Pobierz `n` i liczbę powtórzeń z `sys.argv`, np. `python3 zadanie_04.py 100000 5`. Obie wartości są dodatnimi liczbami całkowitymi.
2. Zdefiniuj osobną funkcję dla każdego sposobu. Każda ma otrzymywać ten sam obiekt `range(n)` i zwracać gotową listę. Sprawdź zgodność wyników operatorem `==`.
3. Zmierz czas każdej funkcji przez `time.perf_counter()` w zadanej liczbie powtórzeń. W wariancie `map()` pomiar musi obejmować również utworzenie listy. Podaj minimum i średnią; nie mierz wyświetlania ani zapisu.
4. Dla jednego wyniku utwórz krotkę. Odczytaj `sys.getsizeof()` listy, krotki oraz świeżo utworzonego iteratora `map()` wykonującego te same obliczenia. Opisz, co obejmują te pomiary i dlaczego nie są pomiarem całej pamięci potrzebnej na obliczenia.
5. Ten sam iterator zamień na listę dwukrotnie i wyświetl długości obu wyników. Wyjaśnij obserwację.
6. Zapisz parametry, wyniki pomiarów i krótkie wnioski do `porownanie_metod.txt`. Nie zakładaj z góry, która metoda wygra.

**Kontrola:** dla `n = 10` każda metoda zwraca `[0, 4, 16, 36, 64]`; drugi odczyt tego samego iteratora daje pustą listę.

"""

# Tutaj wpisz swoje rozwiązanie.
