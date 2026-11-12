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

## **02 — Instrukcje warunkowe, pętle, definiowanie funkcji**

### **Zagadnienia**

- instrukcje warunkowe:
  - `if`,
  - `elif`,
  - `else`,
- zagnieżdżanie instrukcji warunkowych,
- operatory logiczne w warunkach,
- pętle:
  - `for`,
  - `while`,
- funkcja `range()`,
- sterowanie przebiegiem pętli:
  - `break`,
  - `continue`,
- zagnieżdżanie pętli,
- definiowanie funkcji za pomocą `def`,
- parametry i argumenty funkcji,
- zwracanie wartości za pomocą `return`,
- zmienne lokalne i globalne,
- wywoływanie funkcji.

### **Przykładowe umiejętności**

Student powinien potrafić:

- zastosować instrukcję warunkową do podejmowania decyzji w programie,
- tworzyć warunki złożone z wykorzystaniem operatorów logicznych,
- wykorzystać pętlę `for` do wielokrotnego wykonywania instrukcji,
- wykorzystać pętlę `while` do wykonywania instrukcji zależnie od warunku,
- generować sekwencje liczb za pomocą `range()`,
- sterować przebiegiem pętli za pomocą `break` i `continue`,
- definiować i wywoływać własne funkcje,
- przekazywać argumenty do funkcji,
- zwracać wyniki działania funkcji za pomocą `return`,
- rozróżniać zmienne lokalne i globalne,
- łączyć instrukcje warunkowe, pętle i funkcje w jednym programie.

---

## **03 — Wejście/wyjście, pliki tekstowe, `math`, `random`, `time`**

### **Zagadnienia**

- pobieranie danych od użytkownika za pomocą `input()`,
- konwersja i sprawdzanie poprawności danych wejściowych,
- wyświetlanie i formatowanie wyników za pomocą `print()` oraz f-stringów,
- podstawowa obsługa błędnych danych przez `try` i `except`,
- ścieżki względne i katalog roboczy programu,
- otwieranie plików za pomocą `open()` i konstrukcji `with`,
- tryby otwierania plików: odczyt, zapis i dopisywanie,
- kodowanie plików tekstowych — UTF-8,
- odczytywanie całej zawartości pliku i przetwarzanie wiersz po wierszu,
- przetwarzanie tekstu za pomocą `strip()`, `split()` i `join()`,
- numerowanie wierszy za pomocą `enumerate()`,
- zapisywanie wyników i raportów do plików tekstowych,
- importowanie modułów biblioteki standardowej,
- obliczenia matematyczne z wykorzystaniem modułu `math`,
- losowanie liczb i elementów kolekcji za pomocą modułu `random`,
- ustawianie ziarna generatora i powtarzalność losowań,
- pomiar czasu wykonania programu za pomocą `time.perf_counter()`,
- wprowadzanie opóźnień przez `time.sleep()`,
- zapisywanie daty i godziny za pomocą `time.strftime()`.

### **Przykładowe umiejętności**

Student powinien potrafić:

- pobrać dane od użytkownika i sprawdzić ich poprawność,
- przedstawić wyniki w czytelnej, sformatowanej postaci,
- wczytać dane z pliku tekstowego,
- przetwarzać plik wiersz po wierszu i rozdzielać dane na pola,
- rozpoznawać i pomijać niepoprawne dane,
- zapisać wyniki do nowego pliku lub dopisać je do istniejącego,
- wykorzystać moduł `math` do obliczeń matematycznych,
- losować liczby i elementy kolekcji,
- odtworzyć serię losowań przy użyciu tego samego ziarna,
- zmierzyć czas wykonania wybranego fragmentu programu,
- oznaczyć zapisane wyniki datą i godziną,
- łączyć operacje wejścia/wyjścia z warunkami, pętlami, funkcjami i kolekcjami.

---

## **04 — Rekurencja, przetwarzanie kolekcji, `sys` i kopiowanie danych**

### **Zagadnienia**

- rekurencja — wywoływanie funkcji przez samą siebie,
- warunek bazowy i krok rekurencyjny,
- porównanie podejścia rekurencyjnego i iteracyjnego,
- rekurencyjne przetwarzanie zagnieżdżonych list,
- sprawdzanie typu obiektu za pomocą `isinstance()`,
- wyrażenia lambda i przekazywanie funkcji jako argumentów,
- sortowanie za pomocą `sorted()` i parametru `key`,
- sortowanie według kilku kryteriów,
- listy składane — przekształcanie, filtrowanie i zagnieżdżanie,
- przetwarzanie elementów za pomocą `map()`,
- wybieranie elementów za pomocą `filter()`,
- łączenie kolekcji za pomocą `zip()`,
- iteratory i ich jednorazowe zużywanie,
- argumenty programu przekazywane przez `sys.argv`,
- rozmiar obiektów i ograniczenia pomiaru przez `sys.getsizeof()`,
- odczytywanie limitu rekurencji przez `sys.getrecursionlimit()`,
- przypisanie a kopiowanie obiektów,
- porównywanie wartości i tożsamości obiektów — `==` i `is`,
- kopie płytkie i głębokie — `copy.copy()` i `copy.deepcopy()`,
- współdzielenie zagnieżdżonych obiektów i skutki ich modyfikowania.

### **Przykładowe umiejętności**

Student powinien potrafić:

- napisać funkcję rekurencyjną z poprawnym warunkiem zakończenia,
- porównać rekurencyjne i iteracyjne rozwiązanie problemu,
- przetwarzać listy o różnej głębokości zagnieżdżenia,
- wykorzystać lambdę jako argument innej funkcji,
- sortować rekordy według jednego lub kilku kryteriów,
- tworzyć listy składane z przekształcaniem i filtrowaniem elementów,
- zastosować `map()`, `filter()` i `zip()` do przetwarzania danych,
- wyjaśnić, dlaczego ponowny odczyt zużytego iteratora nie daje wyników,
- pobrać argumenty programu z terminala i przekonwertować ich typy,
- porównać czas wykonania różnych sposobów przetwarzania kolekcji,
- odczytać rozmiar obiektu i wyjaśnić ograniczenia takiego pomiaru,
- rozróżnić przypisanie, kopię płytką i kopię głęboką,
- przewidzieć wpływ modyfikacji zagnieżdżonych danych na ich kopie,
- tworzyć niezależne warianty danych za pomocą `deepcopy()`,
- łączyć poznane konstrukcje z funkcjami, plikami tekstowymi i raportowaniem wyników.

---

## **05 — Wyjątki, moduły `os` i `datetime`**

### **Zagadnienia**

- przechwytywanie wyjątków przez `try` i `except`, zgłaszanie wyjątków przez `raise` i definiowanie własnego typu wyjątku,
- obsługa ścieżek i katalogów za pomocą modułu `os`,
- parsowanie i formatowanie dat oraz obliczanie różnic czasu za pomocą modułu `datetime`,
- zastosowanie operacji na plikach tekstowych do analizy plików FASTA.

### Przykładowe umiejętności

Student powinien potrafić:

- obsłużyć błędne dane wejściowe i brak katalogu,
- przejść po plikach FASTA w podanym katalogu i zapisać raport dla każdej sekwencji,
- uporządkować wydarzenia chronologicznie i obliczyć liczbę dni do terminu.

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

