# Python — ćwiczenia

## Informacje organizacyjne

Kurs obejmuje **10 spotkań ze studentami**:

- 8 regularnych ćwiczeń,
- 1 test praktyczny po czwartym ćwiczeniu,
- 1 test końcowy po ósmym ćwiczeniu.

Zajęcia mają charakter praktyczny. Celem kursu jest opanowanie podstaw języka Python oraz podstawowych konstrukcji programistycznych przydatnych w dalszej pracy z bioinformatyką i analizą danych.

Kurs pozostaje kursem **podstawowym („vanilla Python”)**. W ramach zajęć nie wykorzystujemy Jupyter Notebook ani bibliotek takich jak `numpy`, `pandas`, `matplotlib` itp. Biblioteki te są przedmiotem innych zajęć.

Kod można przygotowywać m.in. w:

- Visual Studio Code,
- PyCharm,
- innym wybranym edytorze/IDE,
- terminalu.

Można pracować na własnym laptopie.

---

# Zasady zaliczenia

## Ćwiczenia

W ramach kursu odbywa się **8 regularnych ćwiczeń**.

Za każde ćwiczenie można uzyskać maksymalnie **5 punktów**.

Łącznie za ćwiczenia:

**8 × 5 = 40 pkt**

Zadania można oddać:

- podczas zajęć,
- po zajęciach,

ale **przed rozpoczęciem kolejnego ćwiczenia**.

Szczegółowe wymagania dotyczące poszczególnych zadań znajdują się w katalogach:

```text
01/
02/
03/
...
08/
```

Nieobecność na zajęciach nie oznacza automatycznie utraty możliwości wykonania zadania. Jeżeli zadanie można wykonać samodzielnie, należy je oddać w terminie określonym dla danego ćwiczenia.

---

## Oddawanie zadań

Rozwiązania zadań należy oddawać w formie repozytorium Git.

### Preferowana forma — prywatne repozytorium

Preferowaną formą oddawania zadań jest **prywatne repozytorium Git**, utworzone w ramach kursu.

Repozytorium powinno zawierać strukturę odpowiadającą poszczególnym ćwiczeniom, np.:

```text
/
├── 01/
│   ├── README.md
│   ├── zadanie_01.py
│   ├── zadanie_02.py
│   ├── zadanie_03.py
│   ├── zadanie_04.py
│   └── zadanie_05.py
├── 02/
│   └── ...
└── ...
```

Do prywatnego repozytorium należy **dodać prowadzącego jako współpracownika (collaborator)**. Dzięki temu prowadzący będzie miał dostęp do rozwiązania i będzie mógł sprawdzić wykonane zadania.

### Zasady

- Repozytorium powinno być **prywatne**.
- Prowadzący powinien zostać dodany jako **collaborator**.
- Rozwiązania powinny znajdować się w odpowiednich plikach `.py`.
- Należy zachować nazwy plików oraz strukturę katalogów przygotowaną dla ćwiczenia.
- Zalecane jest regularne wykonywanie commitów, tak aby historia zmian pokazywała postęp pracy.
- Do oceny brana jest pod uwagę zawartość repozytorium w terminie wskazanym przez prowadzącego.

### Alternatywna forma oddania

Jeżeli utworzenie prywatnego repozytorium lub dodanie prowadzącego jako współpracownika nie jest możliwe, sposób oddania należy ustalić z prowadzącym.

> **Uwaga:** samo przesłanie pojedynczych plików `.py` nie jest preferowaną formą oddawania zadań.

---

# Test praktyczny

Po **czwartym ćwiczeniu** odbywa się pierwszy test praktyczny.

**Maksymalna liczba punktów: 25 pkt**

Test ma sprawdzić podstawowe umiejętności programowania w Pythonie zdobyte podczas pierwszej części kursu.

Test może zawierać m.in.:

- krótkie zadania programistyczne,
- uzupełnianie fragmentów kodu,
- wskazywanie poprawnego rozwiązania,
- analizowanie działania kodu,
- zadania wymagające napisania krótkiego fragmentu programu.

Test może częściowo być wykonywany **na kartce**, bez konieczności napisania kompletnego programu w środowisku programistycznym.

Zakres testu obejmuje materiał z ćwiczeń **01–04**.

---

# Test końcowy

Po **ósmym ćwiczeniu** odbywa się drugi test obejmujący całość materiału.

**Maksymalna liczba punktów: 35 pkt**

Test końcowy jest trudniejszy od pierwszego testu i może wymagać łączenia kilku poznanych wcześniej konstrukcji.

Może obejmować:

- analizę istniejącego kodu,
- poprawianie błędów,
- uzupełnianie kodu,
- napisanie krótkiego programu,
- pracę z plikami,
- funkcje,
- kolekcje,
- obsługę wyjątków,
- wyrażenia regularne,
- podstawy programowania obiektowego.

Zakres obejmuje materiał z **całego kursu**.

---

# Punktacja

| Element | Liczba | Punkty | Łącznie |
|---|---:|---:|---:|
| Ćwiczenia | 8 | 5 pkt | 40 pkt |
| Test praktyczny | 1 | 25 pkt | 25 pkt |
| Test końcowy | 1 | 35 pkt | 35 pkt |
| **Razem** | | | **100 pkt** |

Punkty uzyskane podczas ćwiczeń i testów stanowią podstawę oceny z kursu.

---

# Harmonogram

| Spotkanie | Temat | Punkty |
|---:|---|---:|
| 01 | Podstawy Pythona | 5 |
| 02 | Kolekcje i operacje na danych | 5 |
| 03 | Instrukcje sterujące i funkcje | 5 |
| 04 | Funkcje i przetwarzanie kolekcji | 5 |
| — | **Test praktyczny** | **25** |
| 05 | Pliki, I/O i moduły | 5 |
| 06 | Wyjątki, `os`, `datetime` | 5 |
| 07 | Tekst i wyrażenia regularne | 5 |
| 08 | OOP i powtórzenie | 5 |
| — | **Test końcowy** | **35** |
| | **SUMA** | **100** |

---

# Program ćwiczeń

## 01 — Podstawy języka Python

### Zagadnienia

- uruchamianie programów w Pythonie,
- składnia języka,
- zmienne,
- podstawowe typy danych:
  - `int`,
  - `float`,
  - `str`,
  - `bool`,
- konwersja typów,
- operatory arytmetyczne,
- operatory porównania,
- podstawowe operatory logiczne,
- wyświetlanie informacji za pomocą `print()`,
- pobieranie danych za pomocą `input()`.

### Przykładowe umiejętności

Student powinien potrafić:

- utworzyć zmienną,
- określić typ wartości,
- wykonać podstawowe obliczenia,
- porównać wartości,
- pobrać dane od użytkownika,
- przekonwertować dane wejściowe na odpowiedni typ,
- wyświetlić wynik działania programu.

---

# 02 — Kolekcje i operacje na danych

### Zagadnienia

- napisy (`str`),
- listy (`list`),
- krotki (`tuple`),
- słowniki (`dict`),
- zbiory (`set`),
- indeksowanie,
- wycinanie fragmentów danych,
- dodawanie i usuwanie elementów,
- podstawowe metody kolekcji,
- operatory `in` oraz `not in`,
- mutowalność i niemutowalność podstawowych typów.

### Przykładowe umiejętności

Student powinien potrafić:

- utworzyć i zmodyfikować listę,
- odczytać element kolekcji,
- wyszukać element,
- iterować po podstawowych strukturach danych,
- wykorzystać słownik do przechowywania powiązanych informacji,
- wykonywać podstawowe operacje na napisach.

---

# 03 — Instrukcje sterujące i funkcje

### Zagadnienia

- `if`,
- `elif`,
- `else`,
- zagnieżdżone instrukcje warunkowe,
- pętla `for`,
- pętla `while`,
- `break`,
- `continue`,
- `range()`,
- definiowanie funkcji,
- wywoływanie funkcji,
- argumenty funkcji,
- wartość zwracana przez `return`.

### Przykładowe umiejętności

Student powinien potrafić:

- sterować wykonaniem programu,
- wykonać operację dla wielu elementów,
- zastosować odpowiednią pętlę,
- napisać prostą funkcję,
- przekazać argument do funkcji,
- zwrócić wynik z funkcji.

---

# 04 — Funkcje, kolekcje i przetwarzanie danych

### Zagadnienia

- parametry funkcji,
- parametry opcjonalne,
- zakres zmiennych,
- wartości domyślne,
- funkcje anonimowe,
- `lambda`,
- `map()`,
- `filter()`,
- `zip()`,
- list comprehensions,
- łączenie funkcji i kolekcji,
- bardziej złożone operacje na listach i słownikach.

### Przykładowe umiejętności

Student powinien potrafić:

- tworzyć funkcje przyjmujące wiele parametrów,
- stosować wartości domyślne,
- przetwarzać kolekcje za pomocą funkcji,
- tworzyć listy z wykorzystaniem list comprehensions,
- wykorzystać `lambda`, `map()`, `filter()` i `zip()` w prostych problemach.

---

# 05 — Wejście/wyjście, pliki i moduły

### Zagadnienia

- wejście i wyjście,
- praca z plikami tekstowymi,
- `open()`,
- tryby otwierania plików,
- odczytywanie plików,
- zapisywanie plików,
- `read()`,
- `readline()`,
- `readlines()`,
- iterowanie po pliku,
- instrukcja `with`,
- importowanie modułów,
- moduły:
  - `math`,
  - `random`,
  - `time`,
  - `sys`.

### Przykładowe umiejętności

Student powinien potrafić:

- odczytać dane z pliku,
- zapisać wynik do pliku,
- przetworzyć plik linia po linii,
- wykorzystać podstawowy moduł biblioteki standardowej,
- przekazać argumenty programu przez `sys.argv`.

---

# 06 — Wyjątki, system plików i daty

### Zagadnienia

- błędy i wyjątki,
- `try`,
- `except`,
- `else`,
- `finally`,
- przechwytywanie konkretnych wyjątków,
- tworzenie własnych wyjątków,
- `raise`,
- moduł `os`,
- pliki i katalogi,
- ścieżki,
- podstawowe operacje na systemie plików,
- moduł `datetime`,
- daty i czas.

### Przykładowe umiejętności

Student powinien potrafić:

- rozpoznać podstawowe błędy programu,
- bezpiecznie obsłużyć wyjątek,
- wygenerować własny wyjątek,
- sprawdzić istnienie pliku lub katalogu,
- pracować ze ścieżkami,
- wykonać podstawowe operacje na plikach i katalogach,
- wykonywać proste operacje na datach.

---

# 07 — Przetwarzanie tekstu i wyrażenia regularne

### Zagadnienia

- zaawansowane operacje na napisach,
- wyszukiwanie fragmentów tekstu,
- zamiana fragmentów tekstu,
- podział tekstu,
- składanie tekstu,
- formatowanie napisów,
- moduł `re`,
- wyrażenia regularne,
- wzorce,
- `search()`,
- `match()`,
- `findall()`,
- `sub()`,
- grupy w wyrażeniach regularnych.

### Przykładowe zastosowania

Ćwiczenia powinny wykorzystywać przykłady związane z przetwarzaniem danych biologicznych, np.:

- sekwencje DNA,
- identyfikatory,
- proste formaty danych,
- wyszukiwanie motywów,
- ekstrakcję informacji z tekstu.

Student powinien potrafić wykorzystać wyrażenia regularne do znalezienia i przetworzenia określonych wzorców w tekście.

---

# 08 — Programowanie obiektowe i powtórzenie

### Zagadnienia

- podstawy programowania obiektowego,
- klasy,
- obiekty,
- atrybuty,
- metody,
- `__init__()`,
- `__str__()`,
- enkapsulacja,
- dziedziczenie,
- podstawowe metody specjalne,
- organizacja kodu,
- łączenie poznanych wcześniej konstrukcji.

Ostatnie ćwiczenie powinno również służyć jako **powtórzenie materiału przed testem końcowym**.

### Przykładowe umiejętności

Student powinien potrafić:

- zdefiniować prostą klasę,
- utworzyć obiekt,
- zdefiniować atrybuty i metody,
- wykorzystać konstruktor `__init__()`,
- zdefiniować prostą relację dziedziczenia,
- połączyć OOP z poznanymi wcześniej konstrukcjami języka.

---

# Organizacja katalogów

Każde ćwiczenie znajduje się w osobnym katalogu:

```text
01/
02/
03/
04/
05/
06/
07/
08/
```

Każdy katalog zawiera instrukcję danego ćwiczenia,

```text
01/
├── README.md
├── zadanie_01.py
├── zadanie_02.py
└── dane/
```

W `README.md` danego ćwiczenia znajdują się:

1. temat ćwiczenia,
2. zakres materiału,
3. krótki opis wymaganych zagadnień,
4. zadania do wykonania,
5. liczba punktów za poszczególne zadania,
6. ewentualne zadania dodatkowe.
---

# System punktacji pojedynczego ćwiczenia

Każde ćwiczenie:

**maksymalnie 5 pkt**

Przykładowo:

| Zadanie | Punkty |
|---|---:|
| Zadanie 1 | 1 pkt |
| Zadanie 2 | 1 pkt |
| Zadanie 3 | 1 pkt |
| Zadanie 4 | 1 pkt |
| Zadanie 5 | 1 pkt |
| **Razem** | **5 pkt** |

Liczba i trudność zadań może być różna w zależności od tematu ćwiczenia.

---

# Zadania dodatkowe

Zadania dodatkowe:

- rozszerzają podstawowy problem,
- wymagają samodzielnego myślenia,
- nie są konieczne do zaliczenia podstawowego zakresu ćwiczenia.

---

