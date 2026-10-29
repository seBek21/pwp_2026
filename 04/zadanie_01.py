"""
### Zadanie 1 — Rekurencyjna analiza zagnieżdżonych danych

Dane pomiarowe zapisano jako listę o zmiennej głębokości zagnieżdżenia:

```python
dane = [4, [7, [2, 9]], [], [-3, [5]], 6]
```

1. Napisz rekurencyjną funkcję `splaszcz(dane)`, zwracającą nową, płaską listę liczb w pierwotnej kolejności. Obsłuż także puste listy i nie zmieniaj danych źródłowych.
2. Napisz rekurencyjną funkcję `glebokosc(dane)`. Przyjmij, że pusta lista i lista samych liczb mają głębokość 1; każda lista wewnętrzna zwiększa głębokość o 1. Przykładowo `[1, [2]]` ma głębokość 2.
3. Dla spłaszczonych danych wyznacz liczbę pomiarów, sumę, średnią, minimum i maksimum. Zakładamy, że cały zestaw zawiera co najmniej jedną liczbę.
4. Listą składaną wybierz dodatnie pomiary i oblicz ich kwadraty.
5. Zapisz wyniki do `raport_zagniezdzenia.txt`. W komentarzu wskaż warunki bazowe obu funkcji i wyjaśnij, dlaczego kończą działanie.

**Kontrola:** płaska lista to `[4, 7, 2, 9, -3, 5, 6]`, suma wynosi `30`, a głębokość `3`. Sprawdź też `splaszcz([])` i `glebokosc([])`.

"""

# Tutaj wpisz swoje rozwiązanie.
