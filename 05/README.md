# Ćwiczenie 5 — Wyjątki, moduły `os` i `datetime`


## Cel ćwiczeń

Celem ćwiczeń jest obsługa wyjątków, praca z katalogami i ścieżkami za pomocą modułu `os` oraz przetwarzanie dat za pomocą modułu `datetime`. Po zajęciach student powinien potrafić reagować na błędne dane wejściowe, przetwarzać pliki z podanego katalogu, porządkować wydarzenia chronologicznie i obliczać odstępy czasu.

## Zakres materiału

- przechwytywanie wyjątków za pomocą `try` i `except`;
- zgłaszanie wyjątków przez `raise` i definiowanie własnego typu wyjątku;
- operacje na ścieżkach i katalogach za pomocą modułu `os`;
- parsowanie i formatowanie dat oraz obliczanie różnic czasu za pomocą modułu `datetime`.

**Wymagania wstępne** — instrukcje warunkowe, pętle, funkcje, listy, krotki i podstawowe operacje na tekście. Zadania wykorzystują pobieranie danych przez `input()` oraz odczyt i zapis plików tekstowych z ćwiczenia 03.

---

> **Jak korzystać z instrukcji** — uruchamiaj przykłady samodzielnie, zmieniaj dane wejściowe i obserwuj wyniki.

---

## 1. Obsługa wyjątków

### 1.1. `try` i `except`

Jeżeli w bloku `try` pojawi się wyjątek, Python przerywa wykonywanie tego bloku i szuka pasującego `except`. Umieszczaj w `try` operacje, których błędy chcesz przechwycić.

| Wyjątek | Przykładowa przyczyna |
|---|---|
| `ValueError` | Próba wykonania `int("abc")` |
| `TypeError` | Próba dodania liczby do napisu |
| `ZeroDivisionError` | Dzielenie przez zero |
| `FileNotFoundError` | Próba otwarcia nieistniejącego pliku |
| `PermissionError` | Brak uprawnień do odczytu lub zapisu |

**Przykład — konwersja wartości wpisanej przez użytkownika**

```python
tekst = input("Podaj rok: ")

try:
    rok = int(tekst)
except ValueError:
    print("Rok musi być liczbą całkowitą.")
else:
    print(f"Podany rok: {rok}")
```

Blok `else` wykona się po poprawnym zakończeniu bloku `try`. Sprawdź działanie przykładu dla `2026`, `20.5` i pustego napisu.

### 1.2. `raise` i własne wyjątki

Instrukcja `raise` pozwala zgłosić wyjątek, gdy program wykryje niepoprawną wartość. Możesz zgłosić istniejący wyjątek, np. `ValueError`, albo utworzyć własny typ przez dziedziczenie po `Exception`.

**Przykład — sprawdzanie kodu grupy**

```python
class NiepoprawnyKodGrupyError(Exception):
    pass


def sprawdz_kod(kod):
    if kod not in ("A", "B", "C"):
        raise NiepoprawnyKodGrupyError("Kod grupy musi być równy A, B lub C.")
    return kod


try:
    print(sprawdz_kod("D"))
except NiepoprawnyKodGrupyError as blad:
    print(blad)
```

---

## 2. Ścieżki, katalogi i pliki

### 2.1. Operacje na katalogach — moduł `os`

| Konstrukcja | Działanie |
|---|---|
| `os.getcwd()` | Zwraca bieżący katalog roboczy |
| `os.listdir(katalog)` | Zwraca nazwy elementów katalogu |
| `os.path.join(katalog, nazwa)` | Składa ścieżkę z podanych fragmentów |
| `os.path.isfile(sciezka)` | Sprawdza, czy ścieżka prowadzi do pliku |
| `os.makedirs(katalog, exist_ok=True)` | Tworzy katalog wraz z brakującymi katalogami nadrzędnymi i akceptuje istniejący katalog |

**Przykład — wyszukiwanie plików tekstowych w bieżącym katalogu**

```python
import os

katalog = os.getcwd()
for nazwa in sorted(os.listdir(katalog)):
    sciezka = os.path.join(katalog, nazwa)
    if os.path.isfile(sciezka) and nazwa.lower().endswith(".txt"):
        print(sciezka)
```

Ścieżka względna, np. `dane/pomiary.txt`, jest interpretowana względem bieżącego katalogu roboczego. Sprawdź `os.getcwd()`, jeżeli skrypt nie znajduje pliku.

### 2.2. Przypomnienie — odczyt i zapis plików tekstowych

Konstrukcja `with open(...)` zamyka plik po wyjściu z bloku. Tryb `"r"` otwiera plik do odczytu, a tryb `"w"` tworzy plik lub zastępuje jego dotychczasową zawartość. Parametr `encoding="utf-8"` określa kodowanie tekstu.

**Przykład — zapis i odczyt dwóch wierszy**

```python
with open("proba.txt", "w", encoding="utf-8") as plik:
    plik.write("Pierwszy wiersz\n")
    plik.write("Drugi wiersz\n")

with open("proba.txt", "r", encoding="utf-8") as plik:
    for wiersz in plik:
        print(wiersz.rstrip("\n"))
```

### 2.3. Format FASTA

W zadaniu przyjmujemy uproszczony FASTA zawierający jeden rekord w każdym pliku. Pierwszy wiersz zaczyna się od `>` i zawiera identyfikator. Sekwencja może zajmować kilka kolejnych wierszy.

```text
>proba_01
ACGT
AAGC
```

Zawartość tego rekordu to sekwencja `ACGTAAGC` o długości `8`. Znaku `>`, identyfikatora i znaków końca wiersza nie wliczamy do długości.

---

## 3. Daty i czas — moduł `datetime`

### 3.1. Parsowanie i formatowanie daty

- `datetime.strptime(tekst, format)` zamienia napis na obiekt `datetime`.
- `data.strftime(format)` tworzy napis na podstawie obiektu `datetime`.
- `datetime.now()` zwraca bieżącą lokalną datę i godzinę.

| Dyrektywa | Znaczenie |
|---|---|
| `%Y` | Rok z czterema cyframi |
| `%m` | Numer miesiąca |
| `%d` | Dzień miesiąca |
| `%H` | Godzina w formacie 24-godzinnym |
| `%M` | Minuta |

**Przykład — zmiana formatu zapisu daty**

```python
from datetime import datetime

termin = datetime.strptime("2027-02-08 09:30", "%Y-%m-%d %H:%M")
print(termin.strftime("%d.%m.%Y %H:%M"))  # 08.02.2027 09:30
```

### 3.2. Różnica między datami

Odejmowanie dwóch obiektów `datetime` daje obiekt `timedelta`. Atrybut `.days` daje liczbę dni zaokrągloną w dół, a metoda `.total_seconds()` uwzględnia cały odstęp czasu, w tym godziny i minuty.

```python
from datetime import datetime

poczatek = datetime(2027, 2, 8, 9, 30)
koniec = datetime(2027, 2, 9, 11, 30)
roznica = koniec - poczatek

print(roznica.days)  # 1
print(roznica.total_seconds() / 3600)  # 26.0
```

Jeśli interesuje Cię liczba dni kalendarzowych, odejmij obiekty `date` uzyskane metodą `.date()`.

---

## 4. Zadania do wykonania


### Zadanie 1 — Pierwiastki równania kwadratowego

Napisz skrypt, który pyta użytkownika o trzy całkowite współczynniki równania $ax^2 + bx + c = 0$.

1. Pobierz współczynniki `a`, `b` i `c` osobnymi wywołaniami `input()` i przekonwertuj je na typ `int`.
2. Dla `a = 0` zgłoś `ZeroDivisionError` i przechwyć go z komunikatem o niepoprawnym współczynniku.
3. Obsłuż `ValueError`, gdy wpisanej wartości nie da się przekonwertować na liczbę całkowitą.
4. W zależności od wartości wyróżnika wypisz dwa pierwiastki rzeczywiste, jeden pierwiastek podwójny albo informację o braku pierwiastków rzeczywistych.

Dla `a = 1`, `b = -3` i `c = 2` skrypt powinien podać pierwiastki `1` i `2`.

### Zadanie 2 — Analiza plików FASTA

Napisz skrypt, który za pomocą `input()` prosi użytkownika o ścieżkę do katalogu z plikami `.fasta`.

1. Odczytaj każdy plik `.fasta` z podanego katalogu. Przyjmij, że poprawny plik zawiera jeden niepusty rekord z sekwencją DNA złożoną z liter `A`, `T`, `C`, `G`. Uwzględnij również małe litery.
2. Oblicz długość sekwencji i liczbę wystąpień każdego z czterech nukleotydów.
3. W katalogu `wyniki/` utwórz osobny raport tekstowy dla każdej sekwencji. Jako nazwy pliku użyj identyfikatora, czyli pierwszego słowa po `>`, z rozszerzeniem `.txt`. Przyjmij, że identyfikatory są unikalne i nadają się na nazwy plików.
4. Obsłuż `FileNotFoundError`, gdy katalog wejściowy nie istnieje. Dla niepoprawnego rekordu zgłoś `ValueError`, wypisz nazwę pliku i przejdź do następnego.

**Przykładowy raport `wyniki/proba_01.txt`**

```text
Długość: 8
A: 3
T: 1
C: 2
G: 2
```

### Zadanie 3 — Kalendarz wydarzeń

Napisz funkcję przyjmującą listę par `(nazwa, data)`. Każda data jest napisem w formacie `RRRR-MM-DD GG:MM`.

```python
wydarzenia = [
    ("Spotkanie", "2027-01-12 19:00"),
    ("Seminarium", "2027-01-09 10:30"),
]
```

1. Zamień napisy na obiekty `datetime` i posortuj wydarzenia rosnąco według daty i godziny.
2. Dla każdego wydarzenia podaj nazwę, sformatowaną datę z godziną i liczbę dni kalendarzowych do terminu.
3. Zaprezentuj działanie funkcji na liście zawierającej co najmniej dwa wydarzenia w kolejności innej niż chronologiczna. Dla minionych terminów możesz dodać komunikat „wydarzenie minęło”.

Przy dacie odniesienia `07.01.2027` przykładowy wynik wygląda tak:

```text
Seminarium — 09.01.2027 10:30 (za 2 dni)
Spotkanie — 12.01.2027 19:00 (za 5 dni)
```

---

## 5. Punktacja

| Zadanie | Co podlega ocenie | Punkty |
|---|---|---:|
| 1 — Pierwiastki równania kwadratowego | Obsługa błędnych danych i poprawny wynik dla każdego przypadku wyróżnika | 1 |
| 2 — Analiza plików FASTA | Przejście po plikach w katalogu, obsługa błędów i zapis raportów z poprawnymi zliczeniami | 2 |
| 3 — Kalendarz wydarzeń | Poprawne parsowanie, sortowanie i formatowanie dat oraz obliczenie liczby dni do terminu | 2 |
| **Razem** | | **5** |

---

## 6. Podsumowanie

Po wykonaniu ćwiczenia powinieneś potrafić:

- przechwycić konkretny wyjątek za pomocą `try` i `except` oraz zgłosić wyjątek przez `raise`,
- zbudować ścieżkę, przejrzeć zawartość katalogu i utworzyć katalog wynikowy za pomocą modułu `os`,
- przetworzyć pliki tekstowe i zapisać osobny raport dla każdego poprawnego rekordu,
- zamienić napis na datę za pomocą `strptime()`, sformatować datę przez `strftime()` i obliczyć liczbę dni między datami.

---

## 7. Dokumentacja

- Przechwytywanie i zgłaszanie wyjątków oraz własne typy wyjątków — [Błędy i wyjątki](https://docs.python.org/3/tutorial/errors.html).
- Odczytywanie zawartości katalogu i tworzenie katalogów — [Moduł `os`](https://docs.python.org/3/library/os.html#files-and-directories).
- Parsowanie, formatowanie i odejmowanie dat — [Moduł `datetime`](https://docs.python.org/3/library/datetime.html).
