"""
### Zadanie 5 — Kopie danych i scenariusze modyfikacji

Przygotuj funkcję zwracającą za każdym wywołaniem świeże dane:

```python
[
    {"nazwa": "A", "pomiary": [10, 12, 14]},
    {"nazwa": "B", "pomiary": [20, 22, 24]},
]
```

1. W trzech niezależnych doświadczeniach utwórz `oryginal` i `wariant` przez: przypisanie, `copy.copy()` oraz `copy.deepcopy()`.
2. W każdym wariancie kolejno: zmień nazwę pierwszej próbki na `A_mod`, zwiększ jej pierwszy pomiar o 100, dopisz próbkę C z pomiarami `[30, 32, 34]`. Po każdej operacji pokaż obie struktury.
3. Dla każdego doświadczenia sprawdź `is` dla list zewnętrznych, pierwszych słowników i ich list pomiarów. Wyjaśnij, które modyfikacje przeniosły się na oryginał.
4. W osobnym doświadczeniu utwórz przez `deepcopy()` dwa niezależne scenariusze z tego samego oryginału. W pierwszym zwiększ wszystkie pomiary o 10%, w drugim odejmij 2 od każdego pomiaru. Do przeliczenia list wykorzystaj listy składane.
5. Za pomocą `zip()` zestaw odpowiadające sobie próbki oryginału i obu scenariuszy. Dla każdej wypisz trzy średnie. Oryginał ma pozostać bez zmian.
6. Zapisz obserwacje i tabelę średnich do `raport_kopie.txt`.

**Kontrola:** średnie oryginału to `12` i `22`, scenariusza +10%: `13.2` i `24.2`, scenariusza −2: `10` i `20`. W kopii płytkiej dopisanie próbki C nie wydłuża oryginału, ale modyfikacje współdzielonego słownika i jego pomiarów są w nim widoczne.

"""

# Tutaj wpisz swoje rozwiązanie.
