# Ćwiczenie 1 — Podstawy języka Python

## 1. Cel ćwiczenia

Celem pierwszego ćwiczenia jest poznanie podstawowych elementów języka Python, które będą wykorzystywane podczas kolejnych zajęć z bioinformatyki.

W trakcie ćwiczenia poznasz:

- podstawowe typy danych,
- sposób tworzenia i przypisywania zmiennych,
- operacje na liczbach,
- operacje na danych tekstowych,
- operatory przypisania,
- operatory porównania,
- operatory logiczne,
- listy,
- krotki,
- zbiory,
- słowniki,
- podstawowe funkcje i metody wbudowane w Pythona.

W zadaniach wykorzystamy również przykłady związane z analizą sekwencji biologicznych.

---

# 2. Uruchamianie programów w Pythonie

Kod Pythona można wykonywać między innymi w:

- interpreterze Pythona,
- Jupyter Notebook,
- JupyterLab,
- środowisku programistycznym (IDE),
- bezpośrednio z pliku `.py`.

W tym ćwiczeniu rozwiązania należy umieszczać w dostarczonych plikach `.py`.

Przykładowy plik:

```text
zadanie_01.py
```

można uruchomić z terminala poleceniem:

```bash
python3 zadanie_01.py
```

Jeżeli w systemie polecenie `python` wskazuje na Pythona 3, można również użyć:

```bash
python zadanie_01.py
```

---

# 3. Zmienne i typy danych

W Pythonie zmienną tworzymy poprzez przypisanie do niej wartości:

```python
x = 10
y = 3.1415
tekst = "Hello World!"
```

Python automatycznie rozpoznaje typ przechowywanej wartości.

W materiale do ćwiczenia przedstawiono między innymi następujące grupy typów danych:

| Kategoria | Typ | Przykład |
|---|---|---|
| numeryczne | `int` | `10` |
| numeryczne | `float` | `3.1415` |
| numeryczne | `complex` | `3 + 5j` |
| tekstowe | `str` | `"Hello World!"` |
| sekwencyjne | `list` | `[1, 2, 3]` |
| sekwencyjne | `tuple` | `(1, 2, 3)` |
| sekwencyjne | `range` | `range(10)` |
| mapujące | `dict` | `{"a": 1}` |
| zbiory | `set` | `{1, 2, 3}` |
| logiczne | `bool` | `True` / `False` |

Przykłady:

```python
x = 10
y = 3.1415
z = 3 + 5j

tekst = "Hello World!"

lista = [1, 2, 3.1415, "kot"]
krotka = (5, 7, "pies")
```

## 3.1. Adnotacje typów

Python pozwala również zapisać oczekiwany typ zmiennej:

```python
x: int = 10
y: float = 3.14
imie: str = "Ala"
lista: list[int] = [1, 2, 3]
```

Adnotacja typu nie oznacza jednak, że Python automatycznie przekonwertuje wartość do wskazanego typu.

Przykładowo warto zastanowić się, co stanie się w przypadku:

```python
x: int = 3.33
```

---

# 4. Operacje na liczbach

Python umożliwia wykonywanie podstawowych operacji matematycznych.

## 4.1. Dodawanie i odejmowanie

```python
x = 5
y = 10

z = x + y
print(z)
```

Wynik:

```text
15
```

Analogicznie działa odejmowanie:

```python
z = y - x
```

---

## 4.2. Mnożenie i dzielenie

Mnożenie wykonujemy za pomocą `*`:

```python
x = 5
y = 10

z = x * y
```

Dzielenie wykonujemy za pomocą `/`:

```python
z = y / x
```

Dzielenie operatorem `/` zwraca wynik typu zmiennoprzecinkowego.

---

## 4.3. Dzielenie całkowite

Operator:

```python
//
```

wykonuje dzielenie całkowite.

Przykład:

```python
10 // 3
```

---

## 4.4. Reszta z dzielenia

Operator:

```python
%
```

zwraca resztę z dzielenia.

Przykład:

```python
10 % 3
```

---

## 4.5. Potęgowanie

Do potęgowania służy operator:

```python
**
```

Przykład:

```python
x = 5
y = 10

print(x ** y)
```

---

## 4.6. Zaokrąglanie

Do zaokrąglania można wykorzystać funkcję `round()`:

```python
round(3.7)
```

wynik:

```text
4
```

---

# 5. Kolejność wykonywania działań

Python przestrzega kolejności działań matematycznych.

Przy bardziej złożonych wyrażeniach warto stosować nawiasy, aby jednoznacznie określić kolejność obliczeń:

```python
wynik = (a + b) * c
```

W szczególności należy pamiętać, że:

```python
10**2
```

oznacza potęgowanie, a:

```python
10^2
```

nie jest w Pythonie zapisem potęgowania.

---

# 6. Operacje przypisania

Podstawowym operatorem przypisania jest:

```python
=
```

Przykład:

```python
x = 10
```

Python udostępnia również skrócone operatory przypisania.

| Operator | Odpowiednik |
|---|---|
| `=` | przypisanie |
| `+=` | `x = x + ...` |
| `-=` | `x = x - ...` |
| `*=` | `x = x * ...` |
| `/=` | `x = x / ...` |
| `**=` | `x = x ** ...` |

Przykład:

```python
x = 10

x += 5
x -= 3
x *= 2
x /= 4
x **= 2
```

Operatory tego typu są szczególnie przydatne wtedy, gdy kolejne operacje mają modyfikować wcześniej obliczoną wartość.

---

# 7. Dane tekstowe — `str`

Tekst w Pythonie przechowywany jest jako typ:

```python
str
```

Przykład:

```python
tekst = "trzy python trzy najlepszy"
```

## 7.1. Długość tekstu

Do określenia liczby znaków służy:

```python
len(tekst)
```

---

## 7.2. Indeksowanie

Do odwołania się do konkretnego znaku używamy indeksu.

Pierwszy znak ma indeks `0`:

```python
tekst[0]
```

Ostatni znak można pobrać za pomocą indeksu `-1`:

```python
tekst[-1]
```

Przykład:

```python
tekst = "Python"

tekst[0]
```

zwraca:

```text
'P'
```

---

## 7.3. Wielkie i małe litery

Do zmiany wielkości liter służą między innymi:

```python
tekst.upper()
```

oraz:

```python
tekst.lower()
```

---

## 7.4. Dzielenie tekstu

Metoda:

```python
split()
```

dzieli tekst na fragmenty.

Przykład:

```python
tekst = "trzy python trzy najlepszy"

tekst.split()
```

wynik:

```python
['trzy', 'python', 'trzy', 'najlepszy']
```

Warto zwrócić uwagę, że wynik `split()` jest listą.

---

## 7.5. Zamiana znaków

Do zastępowania fragmentów tekstu służy:

```python
replace()
```

Przykład:

```python
tekst.replace("t", "w")
```

---

## 7.6. Liczenie wystąpień

Metoda:

```python
count()
```

pozwala sprawdzić, ile razy dany znak lub fragment występuje w tekście.

Przykład:

```python
tekst.count("t")
```

---

## 7.7. Łączenie tekstów

Teksty można łączyć za pomocą operatora `+`:

```python
tekst_1 = "trzy"
tekst_2 = "python"

tekst_1 + tekst_2
```

Wynik:

```text
'trzypython'
```

---

# 8. Sekwencje biologiczne jako dane tekstowe

Sekwencja DNA może być w Pythonie reprezentowana jako zwykły tekst:

```python
seq = "AGGTCTCAGGCGCTATCA"
```

Dzięki temu możemy stosować do niej operacje poznane w poprzedniej sekcji.

Przykładowo:

```python
seq.count("A")
```

pozwala policzyć wystąpienia adeniny.

Możemy również zastępować znaki:

```python
seq.replace("T", "U")
```

W ten sposób możemy potraktować sekwencję DNA jako punkt wyjścia do prostych operacji bioinformatycznych.

---

# 9. Operatory porównania

Operatory porównania pozwalają sprawdzić relację pomiędzy wartościami.

| Operator | Znaczenie |
|---|---|
| `==` | równe |
| `!=` | różne |
| `>` | większe |
| `<` | mniejsze |
| `>=` | większe lub równe |
| `<=` | mniejsze lub równe |

Przykłady:

```python
4 == 3
```

wynik:

```text
False
```

oraz:

```python
4 != 3
```

wynik:

```text
True
```

Możemy również wykonywać bardziej złożone porównania:

```python
2 + 3 >= 5
```

Wynikiem operacji porównania jest wartość logiczna:

```python
True
```

lub:

```python
False
```

### Uwaga dotycząca liczb zmiennoprzecinkowych

W Pythonie warto sprawdzić zachowanie wyrażenia:

```python
1 / 10 + 1 / 10 + 1 / 10 == 3 / 10
```

Jest to dobry przykład pokazujący, że bezpośrednie porównywanie wyników obliczeń zmiennoprzecinkowych może prowadzić do nieintuicyjnych rezultatów.

---

# 10. Operatory logiczne

Operatory logiczne pozwalają łączyć warunki.

Podstawowe operatory to:

- `and` — koniunkcja,
- `or` — alternatywa,
- `not` — negacja.

Przykład:

```python
a = True
b = False

a and b
```

wynik:

```text
False
```

Przykład:

```python
a and True
```

zwróci:

```text
True
```

Operatory logiczne można łączyć z operatorami porównania.

Przykład:

```python
x > 0 and x < 10
```

---

# 11. Listy — `list`

Lista jest uporządkowanym zbiorem elementów.

Przykład:

```python
lista = [1, 3, 10, "python", (3.14, 0.5)]
```

Lista może zawierać elementy różnych typów.

## 11.1. Długość listy

```python
len(lista)
```

---

## 11.2. Dostęp do elementów

Tak samo jak w przypadku tekstu, indeksowanie zaczyna się od `0`:

```python
lista[0]
```

Pierwszy element ma indeks `0`.

---

## 11.3. Usuwanie elementu

Metoda:

```python
pop()
```

usuwa element z listy.

Przykład:

```python
lista.pop(0)
```

---

## 11.4. Dodawanie elementu

Do dodawania elementów służy:

```python
append()
```

Przykład:

```python
lista.append(12)
```

---

## 11.5. Zmiana elementu

Element listy można zastąpić poprzez przypisanie:

```python
lista[0] = 100
```

---

## 11.6. Sortowanie

Listę można posortować za pomocą:

```python
lista.sort()
```

Możliwe jest również sortowanie według długości elementów tekstowych:

```python
lista.sort(key=len)
```

---

## 11.7. `dir()`

W Pythonie przydatną funkcją jest:

```python
dir(obiekt)
```

Pozwala ona podejrzeć dostępne atrybuty i metody danego obiektu.

Przykład:

```python
dir(lista)
```

Jest to szczególnie przydatne podczas nauki nowych typów danych i sprawdzania, jakie operacje można na nich wykonać.

---

# 12. Krotki — `tuple`

Krotka przypomina listę, ale jest zapisywana w nawiasach okrągłych:

```python
krotka = (1, 2, 3)
```

Jedną z istotnych różnic pomiędzy listą i krotką jest możliwość modyfikowania zawartości.

W przypadku listy możemy wykonać:

```python
lista.append(12)
lista.pop(0)
```

Natomiast dla krotki:

```python
krotka.pop(0)
krotka.append(12)
```

takie operacje nie są dostępne.

Warto samodzielnie sprawdzić, jaki błąd pojawi się po wykonaniu powyższych instrukcji.

---

# 13. Zbiory — `set`

Zbiór zapisujemy za pomocą nawiasów klamrowych:

```python
zbior_A = {1, 4, 6, 7}
zbior_B = {1, 2, 3, 6}
```

Zbiory są przydatne między innymi wtedy, gdy interesują nas unikalne wartości.

## 13.1. Suma zbiorów

Do połączenia elementów dwóch zbiorów można wykorzystać:

```python
zbior_A.union(zbior_B)
```

---

## 13.2. Usuwanie powtórzeń

Jednym z praktycznych zastosowań zbiorów jest usuwanie duplikatów z listy.

Przykładowo:

```python
lista_A = [1, 1, 1, 2, 2, 3]
```

możemy przekształcić w zbiór:

```python
zbior_A = set(lista_A)
```

a następnie ponownie w listę:

```python
lista_B = list(zbior_A)
```

W ten sposób uzyskujemy listę zawierającą unikalne elementy.

Warto zwrócić uwagę, że po takim przekształceniu nie należy traktować kolejności elementów jako istotnej właściwości zbioru.

---

# 14. Słowniki — `dict`

Słownik przechowuje dane w postaci par:

```text
klucz → wartość
```

Przykład:

```python
slownik = {
    "a": 1,
    "b": 2,
    "c": 4
}
```

W tym przypadku:

- `"a"`, `"b"`, `"c"` są kluczami,
- `1`, `2`, `4` są wartościami.

---

## 14.1. Klucze słownika

Klucze można pobrać za pomocą:

```python
slownik.keys()
```

---

## 14.2. Tworzenie słownika z dwóch list

W materiale pokazano również wykorzystanie `zip()` do połączenia dwóch list:

```python
lista_a = [1, 2, 3, 4]
lista_b = ["a", "b", "c", "d"]

slownik = dict(zip(lista_a, lista_b))
```

Otrzymamy:

```python
{
    1: "a",
    2: "b",
    3: "c",
    4: "d"
}
```

Ten sposób będzie szczególnie przydatny w zadaniu dotyczącym częstości występowania nukleotydów.

---

# 15. Funkcje i metody używane w ćwiczeniu

W pierwszym ćwiczeniu warto znać co najmniej następujące konstrukcje:

### Funkcje

```python
len()
print()
round()
list()
set()
dict()
zip()
dir()
help()
```

### Metody tekstowe

```python
.upper()
.lower()
.split()
.replace()
.count()
```

### Metody list

```python
.append()
.pop()
.sort()
```

### Metody zbiorów

```python
.union()
```

### Metody słowników

```python
.keys()
```

Nie trzeba zapamiętywać wszystkich metod Pythona. Ważne jest rozpoznanie, **jakiego typu danych używamy i jakie operacje są dla niego dostępne**.

---

# 16. Zadania

W każdym zadaniu rozwiązanie należy umieścić w odpowiednim pliku `.py`.

## Zadanie 1 — obliczenia matematyczne

Wyznacz wartość wyrażenia:

\[
10^2 + \frac{136}{4.15}\cdot\sqrt{2}
\]

Wynik zapisz do zmiennej:

```python
x
```

---

## Zadanie 2 — BMI

Oblicz wskaźnik BMI osoby, której:

- masa wynosi `139 kg`,
- wzrost wynosi `211 cm`.

Wynik zapisz do zmiennej:

```python
BMI
```

Pamiętaj o odpowiednim przeliczeniu jednostek wzrostu.

---

## Zadanie 3 — DNA → RNA

Zdefiniuj sekwencję:

```python
seq = "AGGTCTCAGGCGCTATCA"
```

Następnie:

1. zamień wszystkie tyminy (`T`) na uracyle (`U`),
2. sprawdź, ile uracyli znajduje się w otrzymanej sekwencji.

Do rozwiązania wykorzystaj operacje na tekstach poznane w ćwiczeniu.

---

## Zadanie 4 — porównanie wyrażeń

Dla:

```text
x = 3
```

sprawdź, czy wyrażenie:

\[
x^{14} + 5x - 145
\]

jest większe od:

\[
x^{12} + 10x - 221
\]

Wynik porównania powinien być wartością logiczną:

```python
True
```

lub:

```python
False
```

---

## Zadanie 5 — analiza sekwencji

Dla sekwencji:

```python
seq = "AGGTCTCAGGCGCTATCA"
```

wykonaj trzy operacje:

1. utwórz listę, w której każdy element będzie pojedynczym nukleotydem,
2. utwórz listę zawierającą wyłącznie unikalne nukleotydy,
3. utwórz słownik, w którym:
   - kluczem będzie nukleotyd,
   - wartością będzie liczba jego wystąpień w sekwencji.

W zadaniu wykorzystaj poznane typy danych:

- `str`,
- `list`,
- `set`,
- `dict`.

---

# 17. Punktacja

Ćwiczenie składa się z **5 zadań**.

| Zadanie | Punkty |
|---|---:|
| Zadanie 1 | 1 |
| Zadanie 2 | 1 |
| Zadanie 3 | 1 |
| Zadanie 4 | 1 |
| Zadanie 5 | 1 |
| **Razem** | **5** |

Każde zadanie jest oceniane pod kątem poprawności rozwiązania oraz wykorzystania odpowiednich konstrukcji języka Python.

---

# 18. Dobre praktyki

Podczas rozwiązywania zadań:

- używaj czytelnych nazw zmiennych,
- zachowuj wcięcia i czytelne formatowanie kodu,
- nie umieszczaj wszystkich rozwiązań w jednym pliku,
- nie zmieniaj nazw plików zadań,
- nie usuwaj treści poleceń umieszczonych w plikach,
- jeżeli rozwiązanie wymaga kilku kroków, rozbij je na czytelne instrukcje,
- sprawdzaj wynik działania programu przed oddaniem zadania.

---

# 20. Podsumowanie

Po wykonaniu ćwiczenia powinieneś potrafić:

- tworzyć zmienne i przypisywać im wartości,
- rozpoznawać podstawowe typy danych,
- wykonywać podstawowe działania matematyczne,
- korzystać z operatorów `//`, `%` i `**`,
- wykonywać operacje na tekstach,
- indeksować teksty i listy,
- korzystać z metod takich jak `replace()`, `count()`, `append()` i `pop()`,
- wykonywać porównania za pomocą `==`, `!=`, `>`, `<`, `>=`, `<=`,
- stosować `and`, `or` i `not`,
- rozumieć różnicę pomiędzy listą, krotką, zbiorem i słownikiem,
- usuwać duplikaty za pomocą zbioru,
- tworzyć słowniki,
- wykorzystywać podstawowe konstrukcje Pythona do prostych operacji na sekwencjach biologicznych.

To zestaw podstawowych narzędzi, na których będą opierały się kolejne ćwiczenia.
