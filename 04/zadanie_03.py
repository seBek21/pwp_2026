"""
### Zadanie 3 — Porównanie serii pomiarów z terminala

Plik `dane/pomiary.txt` ma nagłówek `probka przed po`, a dalej identyfikatory oraz dwa pomiary dodatnie. Napisz program uruchamiany tak:

```bash
python3 zadanie_03.py dane/pomiary.txt 15 raport_pomiary.txt
```

Argumenty oznaczają ścieżkę wejściową, próg bezwzględnej zmiany procentowej i nazwę raportu. Pobierz je z `sys.argv`.

1. Pomiń nagłówek. Utwórz osobne listy identyfikatorów, wartości przed i wartości po; liczby konwertuj z użyciem `map()`.
2. Używając `zip()`, połącz odpowiadające sobie elementy. Dla każdej próbki oblicz różnicę `po - przed` i zmianę procentową `100 * (po - przed) / przed`.
3. Listą składaną wybierz próbki, dla których moduł zmiany procentowej jest co najmniej równy progowi.
4. Posortuj wybrane rekordy malejąco według modułu zmiany procentowej, a przy remisie rosnąco według nazwy.
5. Zapisz raport z wynikami wszystkich próbek, osobnym rankingiem wybranych oraz średnią różnicą dla całego zestawu. Zastosuj dwie cyfry po przecinku. Wyświetl liczbę próbek i liczbę wybranych.

**Kontrola:** dla progu 15 ranking to `P04`, `P02`, `P01`; średnia różnica wynosi `-1.00`. Zakładamy poprawną liczbę argumentów, istniejący niepusty plik i nieujemny próg.

"""

# Tutaj wpisz swoje rozwiązanie.
