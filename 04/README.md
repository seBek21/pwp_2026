# Ćwiczenie 4 — Rekurencja, przetwarzanie kolekcji, `sys` i kopiowanie danych

## Cel ćwiczeń

Celem ćwiczeń jest poznanie rekurencji oraz wygodnych sposobów przetwarzania kolekcji. Nauczysz się stosować wyrażenia lambda, listy składane, `map()`, `filter()` i `zip()`, przekazywać argumenty programu z terminala oraz odróżniać przypisanie od kopiowania danych.

W zadaniach wykorzystasz również funkcje, warunki, pętle, pliki tekstowe i pomiar czasu poznane na poprzednich zajęciach.

## Zakres materiału

- rekurencja: wywołanie własnej funkcji, warunek bazowy i przekazywanie wyniku;
- porównanie rekurencji z iteracją;
- przetwarzanie zagnieżdżonych list;
- wyrażenia lambda i funkcje przekazywane jako argumenty;
- sortowanie według własnego klucza;
- listy składane: przekształcanie, filtrowanie i zagnieżdżanie;
- `map()`, `filter()` i `zip()`;
- jednorazowe zużywanie iteratorów;
- moduł `sys`: `argv`, `getsizeof()` i `getrecursionlimit()`;
- przypisanie, kopia płytka i kopia głęboka;
- moduł `copy`, porównania `==` i `is`.

**Wymagania wstępne:** materiał ćwiczeń 1–3, w szczególności funkcje z `return`, pętle, warunki, napisy, listy, krotki, słowniki, `with open()` oraz `time.perf_counter()`.

---

## 1. Rekurencja

### 1.1. Funkcja wywołująca samą siebie

Rekurencja polega na rozwiązaniu problemu przez wywołanie tej samej funkcji dla prostszego przypadku.

Każde takie rozwiązanie powinno określać:

1. **warunek bazowy** — przypadek, w którym wynik można podać bez dalszych wywołań;
2. **krok rekurencyjny** — wywołanie funkcji dla mniejszego lub prostszego problemu;
3. sposób wykorzystania wyniku zwróconego przez to wywołanie.

Przykład obliczający potęgę liczby `2` dla nieujemnego całkowitego `n`:

```python
def potega_dwojki(n):
    if n == 0:
        return 1
    return 2 * potega_dwojki(n - 1)


print(potega_dwojki(3))  # 8
```

Nie korzystamy tutaj z gotowego operatora `**`, aby zobaczyć działanie rekurencji.

Dla `n = 3` zależności wyglądają następująco:

```text
potega_dwojki(3) = 2 * potega_dwojki(2)
potega_dwojki(2) = 2 * potega_dwojki(1)
potega_dwojki(1) = 2 * potega_dwojki(0)
potega_dwojki(0) = 1
```

Po osiągnięciu przypadku bazowego wyniki wracają do wcześniejszych wywołań: `1`, następnie `2`, `4` i `8`.

### 1.2. `return` i osobne wywołania

Każde wywołanie funkcji ma własne zmienne lokalne. Wywołanie dla `n = 3` czeka na wynik wywołania dla `n = 2`, zamiast zastępować je jednym wspólnym zestawem zmiennych.

Wyrażenie:

```python
return 2 * potega_dwojki(n - 1)
```

wykorzystuje wynik kolejnego wywołania i przekazuje obliczoną wartość dalej. Samo wywołanie funkcji bez wykorzystania jej wyniku nie zastępuje `return`.

**Do sprawdzenia:** jak zmieni się wynik funkcji, jeżeli w przypadku bazowym zwrócisz `0` zamiast `1`?

### 1.3. Rekurencja a iteracja

Ten sam problem można rozwiązać pętlą:

```python
def potega_dwojki_iter(n):
    wynik = 1
    for _ in range(n):
        wynik *= 2
    return wynik


print(potega_dwojki_iter(3))  # 8
```

Znak `_` jest zwykłą nazwą zmiennej. Używamy go, gdy wartość licznika nie jest potrzebna.

Rekurencja może dobrze oddawać strukturę zagnieżdżonych danych. Pętla jest zwykle prostsza przy zwykłym zliczaniu lub sumowaniu. Sama zamiana pętli na rekurencję nie gwarantuje przyspieszenia programu.

W tym ćwiczeniu stosuj niewielkie głębokości zagnieżdżenia. Nie zwiększaj limitu rekurencji.

### 1.4. Zagnieżdżone listy i `isinstance()`

Lista może zawierać inne listy:

```python
dane = [4, [7, [2, 9]], 3]

print(isinstance(dane, list))     # True
print(isinstance(dane[0], list))  # False
print(isinstance(dane[1], list))  # True
```

`isinstance(obiekt, list)` sprawdza, czy obiekt jest listą. Dzięki temu można zdecydować, czy analizujemy pojedynczą wartość, czy kolejne zagnieżdżenie.

Przykład zliczający wartości znajdujące się na dowolnym poziomie:

```python
def licz_wartosci(dane):
    licznik = 0
    for element in dane:
        if isinstance(element, list):
            licznik += licz_wartosci(element)
        else:
            licznik += 1
    return licznik


print(licz_wartosci([4, [7, [2, 9]], 3]))  # 5
print(licz_wartosci([]))  # 0
```

Pusta lista wnosi do wyniku zero. Pętla i rekurencja mogą występować w tej samej funkcji: pętla odwiedza elementy danego poziomu, a rekurencja schodzi do kolejnej listy.

### 1.5. Pomocnicza metoda `extend()`

```python
lista = [1, 2]
lista.append([3, 4])
print(lista)  # [1, 2, [3, 4]]

lista = [1, 2]
lista.extend([3, 4])
print(lista)  # [1, 2, 3, 4]
```

`append()` dodaje jeden element, a `extend()` dodaje kolejno elementy przekazanej kolekcji. Obie metody zmieniają istniejącą listę.

---

## 2. Wyrażenia lambda i funkcje jako argumenty

### 2.1. Krótka funkcja jako wyrażenie

```python
def podwoj(x):
    return 2 * x


podwoj_lambda = lambda x: 2 * x

print(podwoj(6))         # 12
print(podwoj_lambda(6))  # 12
```

Zapis ma postać `lambda parametry: wyrazenie`. Wynik wyrażenia jest zwracany automatycznie. Lambda może mieć kilka parametrów, lecz jej ciało jest pojedynczym wyrażeniem.

```python
polacz = lambda a, b: a + "-" + b
print(polacz("A", "B"))  # A-B
```

Do dłuższych obliczeń, wielu instrukcji lub rozwiązania wymagającego opisu używaj zwykłego `def`. Przypisanie lambdy do nazwy służy tutaj porównaniu zapisu; w praktyce lambda jest szczególnie przydatna jako krótki argument innej funkcji.

### 2.2. Przekazanie funkcji a jej wywołanie

```python
def zwieksz(x):
    return x + 1


funkcja = zwieksz
wynik = zwieksz(4)

print(funkcja(10))  # 11
print(wynik)       # 5
```

`zwieksz` oznacza samą funkcję, natomiast `zwieksz(4)` oznacza wynik jej wywołania. Ta różnica będzie potrzebna w `map()`, `filter()` i sortowaniu.

### 2.3. Sortowanie według własnego klucza

```python
probki = [("A", 12), ("B", 5), ("C", 20)]

rosnaco = sorted(probki, key=lambda rekord: rekord[1])
malejaco = sorted(probki, key=lambda rekord: rekord[1], reverse=True)

print(rosnaco)   # [('B', 5), ('A', 12), ('C', 20)]
print(malejaco)  # [('C', 20), ('A', 12), ('B', 5)]
```

`key` wskazuje funkcję wyznaczającą wartość używaną do porównywania rekordów. `sorted()` zwraca nową listę; metoda `lista.sort()` zmienia istniejącą listę.

Klucz może być krotką z kilkoma kryteriami:

```python
rekordy = [("B", 10), ("A", 10), ("C", 5)]
wynik = sorted(rekordy, key=lambda r: (-r[1], r[0]))
print(wynik)  # [('A', 10), ('B', 10), ('C', 5)]
```

Najpierw porównywane jest pierwsze kryterium, a przy remisie następne. Znak minus pozwala odwrócić kolejność kryterium liczbowego bez odwracania kolejności nazw.

---

## 3. Listy składane

### 3.1. Przekształcanie elementów

```python
liczby = [1, 2, 3, 4]

kwadraty = []
for liczba in liczby:
    kwadraty.append(liczba ** 2)

kwadraty_skladana = [liczba ** 2 for liczba in liczby]
print(kwadraty_skladana)  # [1, 4, 9, 16]
```

Lista składana ma postać `[wyrazenie for element in kolekcja]`. Tworzy nową listę wyników.

### 3.2. Filtrowanie elementów

```python
liczby = [-3, 0, 4, 7, -1]
dodatnie = [x for x in liczby if x > 0]
print(dodatnie)  # [4, 7]
```

Warunek umieszczony po `for` decyduje, czy element znajdzie się w wyniku.

### 3.3. Wybór wartości przez `if`–`else`

```python
liczby = [-3, 0, 4, 7, -1]
etykiety = ["dodatnia" if x > 0 else "niedodatnia" for x in liczby]
print(etykiety)
```

Tutaj powstaje wynik dla każdego elementu. `if`–`else` jest częścią wyrażenia przed `for`, więc wybiera wartość zamiast odrzucać element.

### 3.4. Dwie pętle w liście składanej

```python
wiersze = [[1, 2], [3], [4, 5]]
plaska = [x for wiersz in wiersze for x in wiersz]
print(plaska)  # [1, 2, 3, 4, 5]
```

Kolejność nagłówków `for` jest taka sama jak w zwykłych zagnieżdżonych pętlach. Ten zapis obsługuje jeden znany poziom list wewnętrznych. Przy zmiennej głębokości zagnieżdżenia potrzebne jest inne rozwiązanie, np. rekurencja.

---

## 4. `map()`, `filter()` i `zip()`

### 4.1. `map()` — przekształcenie każdego elementu

```python
teksty = ["12", "7", "25"]
liczby = list(map(int, teksty))
print(liczby)  # [12, 7, 25]

wynik = list(map(lambda x: x / 10, liczby))
print(wynik)  # [1.2, 0.7, 2.5]
```

Pierwszym argumentem jest funkcja, a kolejnym przetwarzana kolekcja. `map()` może też przekazywać funkcji elementy kilku kolekcji:

```python
a = [1, 2, 3]
b = [10, 20, 30]
print(list(map(lambda x, y: x + y, a, b)))  # [11, 22, 33]
```

### 4.2. `filter()` — wybór elementów

```python
liczby = [2, 5, 8, 11, 14]
wynik = list(filter(lambda x: x % 2 == 0, liczby))
print(wynik)  # [2, 8, 14]
```

Przekazana funkcja zwraca informację, czy element ma zostać zachowany. `filter()` zwraca wybrane elementy, bez ich przekształcania.

### 4.3. `zip()` — łączenie odpowiadających sobie pozycji

```python
nazwy = ["A", "B", "C"]
wyniki = [12, 7, 18]

pary = list(zip(nazwy, wyniki))
print(pary)  # [('A', 12), ('B', 7), ('C', 18)]

for nazwa, wynik in zip(nazwy, wyniki):
    print(nazwa, wynik)
```

`zip()` może łączyć także trzy lub więcej kolekcji. Domyślnie kończy pracę wraz z najkrótszą z nich:

```python
print(list(zip([1, 2, 3], [10, 20])))  # [(1, 10), (2, 20)]
```

Przy łączeniu serii pomiarów ważna jest zgodność ich kolejności.

### 4.4. Iteratory i ich zużywanie

`map()`, `filter()` i `zip()` udostępniają wyniki jako iteratory. Kolejne wartości są pobierane w trakcie przechodzenia po nich. Jeżeli chcesz zachować wszystkie wyniki, utwórz listę.

```python
przeliczone = map(lambda x: x * 3, [1, 2, 3])

pierwszy_odczyt = list(przeliczone)
drugi_odczyt = list(przeliczone)

print(pierwszy_odczyt)  # [3, 6, 9]
print(drugi_odczyt)    # []
```

Przypisanie do zmiennej nie zamienia iteratora w listę. Po jego zużyciu trzeba utworzyć nowy iterator albo korzystać z wcześniej zapisanej listy.

### 4.5. To samo przetwarzanie w dwóch zapisach

```python
dane = [1, 2, 3, 4, 5]

wynik_map = list(map(lambda x: x ** 2, filter(lambda x: x > 2, dane)))
wynik_skladana = [x ** 2 for x in dane if x > 2]

print(wynik_map)       # [9, 16, 25]
print(wynik_skladana)  # [9, 16, 25]
```

Nie trzeba zapisywać całego programu w jednej linijce. W bardziej złożonej analizie nazwij wyniki kolejnych etapów, aby dało się je sprawdzić osobno.

---

## 5. Moduł `sys`

### 5.1. Argumenty programu — `sys.argv`

Poniższy przykład zapisz w osobnym pliku `przyklad_argumenty.py`:

```python
import sys

tekst = sys.argv[1]
ile = int(sys.argv[2])
print(tekst * ile)
```

Uruchomienie:

```bash
python3 przyklad_argumenty.py AT 3
```

Wynik: `ATATAT`. Element `sys.argv[0]` zawiera nazwę skryptu, a następne elementy — argumenty użytkownika. Argumenty są napisami, podobnie jak wynik `input()`.

### 5.2. Rozmiar obiektu — `sys.getsizeof()`

```python
import sys

liczby = [10, 20, 30]
print(sys.getsizeof(liczby))
print(sys.getsizeof(tuple(liczby)))
```

Wynik jest podany w bajtach i zależy od środowiska. Dla listy pomiar obejmuje sam kontener, a nie łączny rozmiar wszystkich obiektów, do których odsyła. Mały rozmiar iteratora nie oznacza, że obliczono i zapisano już wszystkie jego wyniki.

### 5.3. Limit rekurencji

```python
import sys

print(sys.getrecursionlimit())
```

Funkcja odczytuje limit głębokości stosu interpretera. Pracuj z małymi przykładami; w tych zadaniach pozostaw limit bez zmian.

---

## 6. Przypisanie i kopiowanie danych

### 6.1. Dwie nazwy tego samego obiektu

```python
a = [1, 2, 3]
b = a
b.append(4)

print(a)       # [1, 2, 3, 4]
print(b)       # [1, 2, 3, 4]
print(a is b)  # True
```

Przypisanie `b = a` nie tworzy kopii. Obie nazwy wskazują ten sam obiekt. `==` porównuje wartości, a `is` — tożsamość obiektów.

### 6.2. Kopia płytka

```python
import copy

a = [1, [2, 3]]
b = copy.copy(a)

b[0] = 10
b[1][0] = 20

print(a)            # [1, [20, 3]]
print(b)            # [10, [20, 3]]
print(a is b)       # False
print(a[1] is b[1]) # True
```

Nowa jest zewnętrzna lista, ale jej elementy pozostają odwołaniami do tych samych obiektów. Kopię płytką listy można też utworzyć przez `a.copy()` albo `a[:]`.

### 6.3. Kopia głęboka

```python
import copy

a = [1, [2, 3]]
b = copy.deepcopy(a)
b[1][0] = 20

print(a)            # [1, [2, 3]]
print(b)            # [1, [20, 3]]
print(a is b)       # False
print(a[1] is b[1]) # False
```

Kopia głęboka odtwarza także zagnieżdżone listy i słowniki. W pokazanym przykładzie modyfikacja wewnętrznej listy kopii pozostawia oryginał bez zmian.

| Operacja | Nowa zewnętrzna lista | Osobna zagnieżdżona lista z przykładu |
|---|---|---|
| `b = a` | nie | nie |
| `b = a.copy()` | tak | nie |
| `b = copy.deepcopy(a)` | tak | tak |

### 6.4. Osobne wiersze macierzy

```python
macierz = [[0, 0]] * 3
macierz[0][0] = 9
print(macierz)  # [[9, 0], [9, 0], [9, 0]]

macierz = [[0, 0] for _ in range(3)]
macierz[0][0] = 9
print(macierz)  # [[9, 0], [0, 0], [0, 0]]
```

Mnożenie listy powiela odwołania. W drugim zapisie nowy wiersz jest tworzony w każdej iteracji. `deepcopy()` zachowuje wewnętrzne współdzielenie: skopiowanie pierwszej macierzy nie rozdzieli jej trzech odwołań na trzy niezależne wiersze.

---

## 7. Zadania do wykonania

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


### Zadanie 2 — Filtrowanie i ranking sekwencji DNA

Plik `dane/sekwencje.txt` zawiera w każdym wierszu identyfikator i niepustą sekwencję DNA, rozdzielone spacją. Sekwencje zawierają wyłącznie wielkie litery A, T, G, C.

1. Wczytaj rekordy i dla każdego oblicz długość, liczbę tymin oraz procent GC.
2. Za pomocą `filter()` i lambdy pozostaw sekwencje o długości co najmniej 8 i GC od 40% do 60% włącznie.
3. Posortuj wybrane rekordy przez `sorted()` i lambdę: malejąco według GC, przy remisie rosnąco według identyfikatora. Sortuj na niezaokrąglonych wartościach.
4. Dla wszystkich sekwencji uzyskaj listę liczb tymin na dwa sposoby: `map()` z lambdą oraz listą składaną. Porównaj wyniki.
5. Zapisz ranking do `ranking_dna.txt`: identyfikator, sekwencja, długość, liczba T i GC z dwoma miejscami po przecinku. Jeżeli nie wybrano rekordów, zapisz informację o pustym rankingu.

**Kontrola:** wybrane rekordy w kolejności to `S03`, `S05`, `S01`, `S06`. Lista liczb tymin dla całego pliku to `[2, 4, 2, 0, 0, 3]`.


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


### Zadanie 4 — Czas, rozmiar kolekcji i iteratory

Porównaj obliczanie kwadratów liczb parzystych od 0 do `n - 1` trzema sposobami: pętlą z `append()`, listą składaną oraz `map()` z lambdą na wyniku `filter()` z lambdą.

1. Pobierz `n` i liczbę powtórzeń z `sys.argv`, np. `python3 zadanie_04.py 100000 5`. Obie wartości są dodatnimi liczbami całkowitymi.
2. Zdefiniuj osobną funkcję dla każdego sposobu. Każda ma otrzymywać ten sam obiekt `range(n)` i zwracać gotową listę. Sprawdź zgodność wyników operatorem `==`.
3. Zmierz czas każdej funkcji przez `time.perf_counter()` w zadanej liczbie powtórzeń. W wariancie `map()` pomiar musi obejmować również utworzenie listy. Podaj minimum i średnią; nie mierz wyświetlania ani zapisu.
4. Dla jednego wyniku utwórz krotkę. Odczytaj `sys.getsizeof()` listy, krotki oraz świeżo utworzonego iteratora `map()` wykonującego te same obliczenia. Opisz, co obejmują te pomiary i dlaczego nie są pomiarem całej pamięci potrzebnej na obliczenia.
5. Ten sam iterator zamień na listę dwukrotnie i wyświetl długości obu wyników. Wyjaśnij obserwację.
6. Zapisz parametry, wyniki pomiarów i krótkie wnioski do `porownanie_metod.txt`. Nie zakładaj z góry, która metoda wygra.

**Kontrola:** dla `n = 10` każda metoda zwraca `[0, 4, 16, 36, 64]`; drugi odczyt tego samego iteratora daje pustą listę.


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


---

## 8. Punktacja

| Zadanie | Punkty |
|---|---:|
| 1 — Rekurencyjna analiza zagnieżdżonych danych | 1 |
| 2 — Filtrowanie i ranking sekwencji DNA | 1 |
| 3 — Porównanie serii pomiarów z terminala | 1 |
| 4 — Czas, rozmiar kolekcji i iteratory | 1 |
| 5 — Kopie danych i scenariusze modyfikacji | 1 |
| **Razem** | **5** |

Oceniane są poprawność wyników, realizacja wymagań dotyczących konstrukcji języka, podział na funkcje oraz poprawny zapis plików. W zadaniach 4 i 5 oceniane jest także wyjaśnienie obserwacji.

---

## 9. Podsumowanie i dokumentacja

Po wykonaniu ćwiczenia powinieneś potrafić stosować rekurencję do zagnieżdżonych danych, wybierać i przekształcać elementy kolekcji, łączyć serie przez `zip()`, pobierać argumenty z terminala oraz dobierać sposób kopiowania danych.

Dokumentacja:

- [Wyrażenia lambda](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions)
- [Listy składane i struktury danych](https://docs.python.org/3/tutorial/datastructures.html)
- [Funkcje wbudowane: `map()`, `filter()`, `zip()`, `isinstance()`](https://docs.python.org/3/library/functions.html)
- [Sortowanie i funkcje klucza](https://docs.python.org/3/howto/sorting.html)
- [`sys`](https://docs.python.org/3/library/sys.html)
- [`copy`](https://docs.python.org/3/library/copy.html)
