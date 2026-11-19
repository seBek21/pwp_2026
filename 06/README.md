# Ćwiczenie 6 — Wyrażenia regularne w Pythonie

## Cel ćwiczeń

Celem ćwiczeń jest poznanie wyrażeń regularnych oraz ich wykorzystanie do wyszukiwania, sprawdzania, wydobywania i przekształcania danych tekstowych. Szczególną uwagę poświęcimy grupom, odwołaniom wstecznym, flagom oraz dopasowaniom nakładającym się na siebie.

Po zakończeniu ćwiczeń student powinien potrafić samodzielnie zaprojektować wzorzec, wyjaśnić znaczenie jego elementów, odczytać wynik dopasowania i wykorzystać go w programie przetwarzającym pliki.

**Wymagania wstępne:** napisy i ich metody, listy, krotki, słowniki, zbiory, instrukcje warunkowe, pętle, funkcje, praca z plikami i obsługa wyjątków. W przykładach powracają poznane wcześniej moduły `os`, `datetime`, `math`, `random` i `time`.


---

## 1. Czym jest wyrażenie regularne?

Wyrażenie regularne, nazywane również **regexem**, jest wzorcem opisującym budowę tekstu. Zamiast wymieniać wszystkie dopuszczalne napisy, zapisujemy regułę ich tworzenia.

Przykładowo kod `ABC-123` można opisać jako:

- trzy wielkie litery alfabetu łacińskiego;
- myślnik;
- trzy cyfry od `0` do `9`.

W Pythonie odpowiada temu wzorzec:

```python
import re

wzorzec = r"[A-Z]{3}-[0-9]{3}"

for kod in ["ABC-123", "XYZ-007", "AB-123", "ABC-1234"]:
    print(kod, bool(re.fullmatch(wzorzec, kod)))
```

Wynik:

```text
ABC-123 True
XYZ-007 True
AB-123 False
ABC-1234 False
```

Moduł `re` należy do biblioteki standardowej. Nie trzeba go instalować.

Regexy przydają się m.in. do:

- sprawdzania formatu identyfikatorów i nazw plików;
- wydobywania pól z wierszy raportu;
- wyszukiwania dat, liczb i adresów w tekście;
- odnajdywania motywów w sekwencjach;
- zastępowania fragmentów tekstu według wspólnej reguły.

Jeżeli szukasz jednego dosłownego fragmentu lub dzielisz napis według jednego stałego separatora, często wystarczą `in`, `startswith()`, `endswith()`, `split()` albo `replace()`. Regex jest przydatny, gdy reguła obejmuje kilka wariantów budowy tekstu.

---

## 2. Napisy surowe i znaki specjalne

### 2.1. Dwie warstwy interpretacji

Wzorzec jest napisem Pythona, który następnie odczytuje silnik wyrażeń regularnych. Ukośnik odwrotny `\` ma znaczenie na obu tych etapach.

Przykładowo `\b` oznacza w regexie granicę słowa, ale w zwykłym napisie Pythona `"\b"` jest znakiem cofnięcia kursora. Dlatego wzorce zapisujemy zwykle jako **napisy surowe**, z prefiksem `r`:

```python
import re

tekst = "kot i kotek"

print(re.findall(r"\bkot\b", tekst))  # ['kot']
print(repr("\b"))                    # '\x08'
print(repr(r"\b"))                   # '\\b'
```

Zapis `r"\b"` przekazuje do `re` ukośnik i literę `b`, które silnik interpretuje jako granicę słowa.

**Prefiks `r` dotyczy napisu Pythona. Nie wyłącza składni regexów.** Wzorzec `r"\n"` nadal dopasowuje znak nowej linii, ponieważ znaczenie `\n` odczytuje moduł `re`.

Napisu surowego nie można zakończyć pojedynczym, nieparzystym ukośnikiem odwrotnym bezpośrednio przed zamykającym cudzysłowem. W przykładach wzorców nie będziemy potrzebować takiego zapisu.

### 2.2. Kiedy znak jest dosłowny?

Litery i cyfry zazwyczaj dopasowują same siebie. Znaki o specjalnym znaczeniu obejmują:

```text
. ^ $ * + ? { } [ ] \ | ( )
```

Aby dopasować taki znak dosłownie, najczęściej poprzedzamy go `\`:

```python
import re

print(bool(re.fullmatch(r"plik\.txt", "plik.txt")))   # True
print(bool(re.fullmatch(r"plik\.txt", "plikXtxt")))  # False
print(bool(re.fullmatch(r"\(ABC\)", "(ABC)")))       # True
print(bool(re.fullmatch(r"A\+B", "A+B")))            # True
```

Wzorzec `r"plik.txt"` oznaczałby `plik`, dowolny znak inny niż nowa linia i `txt`. Kropka bez ukośnika nie oznacza dosłownej kropki.

Jeżeli cały fragment pochodzi ze zmiennej i ma zostać potraktowany dosłownie, skorzystaj z `re.escape()` — omówimy to w części 14.

---

## 3. Podstawowe sposoby dopasowania

### 3.1. `search()`, `match()` i `fullmatch()`

Te funkcje odpowiadają na różne pytania:

| Funkcja | Pytanie |
|---|---|
| `re.search(wzorzec, tekst)` | Czy pasujący fragment występuje gdziekolwiek w tekście? |
| `re.match(wzorzec, tekst)` | Czy dopasowanie rozpoczyna się na początku tekstu? |
| `re.fullmatch(wzorzec, tekst)` | Czy cały tekst, od początku do końca, pasuje do wzorca? |

```python
import re

wzorzec = r"[0-9]+"

for tekst in ["123", "123abc", "abc123"]:
    print(
        tekst,
        bool(re.search(wzorzec, tekst)),
        bool(re.match(wzorzec, tekst)),
        bool(re.fullmatch(wzorzec, tekst)),
    )
```

Wynik:

```text
123 True True True
123abc True True False
abc123 True False False
```

`match()` nie wymaga dopasowania całego napisu: dla `123abc` dopasuje fragment `123`.

**Do sprawdzania formatu całej wartości używaj zwykle `fullmatch()`.** Samo znalezienie poprawnego fragmentu nie oznacza, że poprawny jest cały wiersz.

### 3.2. Co zwraca funkcja?

Udane dopasowanie daje obiekt `Match`. Brak dopasowania daje `None`.

```python
import re

wynik = re.search(r"[0-9]+", "Numer: 42")

if wynik is not None:
    print(wynik.group())  # 42
else:
    print("Nie znaleziono liczby")
```

Można również napisać `if wynik:`. Nie należy wywoływać `wynik.group()`, dopóki nie sprawdzimy, czy dopasowanie istnieje.

`Match` nie jest zwykłym napisem. Oprócz dopasowanego tekstu przechowuje m.in. grupy oraz położenie dopasowania w oryginalnym napisie.

---

## 4. Klasy znaków i skróty

### 4.1. Własne klasy znaków

Nawiasy kwadratowe opisują **jeden znak należący do wskazanego zbioru**.

| Wzorzec | Znaczenie |
|---|---|
| `[abc]` | Jeden znak: `a`, `b` albo `c` |
| `[0-9]` | Jedna cyfra ASCII |
| `[A-Z]` | Jedna wielka litera od `A` do `Z` |
| `[a-zA-Z]` | Jedna mała lub wielka litera z tych zakresów |
| `[ACGT]` | Jeden z czterech wskazanych znaków |
| `[^ACGT]` | Jeden znak inny niż `A`, `C`, `G` i `T` |
| `[.,;]` | Jedna kropka, przecinek albo średnik |
| `[ \t]` | Jedna spacja albo tabulator |

Klasa `[ATG]` nie dopasowuje całego napisu `ATG`. Dopasowuje pojedyncze `A`, `T` lub `G`. Cały napis `ATG` opisujemy po prostu wzorcem `ATG`.

```python
import re

tekst = "A T G ATG"
print(re.findall(r"[ATG]", tekst))  # ['A', 'T', 'G', 'A', 'T', 'G']
print(re.findall(r"ATG", tekst))    # ['ATG']
```

Ważne szczegóły:

- `^` oznacza negację klasy tylko na jej początku, np. `[^0-9]`.
- Myślnik między znakami wyznacza zakres. Dosłowny myślnik można zapisać jako `\-` albo umieścić na początku lub końcu klasy.
- Kropka wewnątrz klasy jest dosłowną kropką: `[.]` i `\.` dopasowują kropkę.
- Zakres `[A-z]` obejmuje również znaki znajdujące się pomiędzy `Z` i `a`, np. `_`. Do liter łacińskich używaj `[A-Za-z]`.
- Negacja klasy nie ogranicza się do liter. `[^P]` może dopasować także cyfrę, spację lub nową linię. Przy analizie sekwencji najpierw sprawdzamy jej alfabet.

### 4.2. Skrócone klasy

| Wzorzec | Znaczenie dla zwykłego napisu `str` |
|---|---|
| `\d` | Jedna cyfra dziesiętna, także spoza ASCII |
| `\D` | Znak, który nie należy do `\d` |
| `\w` | Znak alfanumeryczny Unicode albo `_` |
| `\W` | Znak, który nie należy do `\w` |
| `\s` | Biały znak, np. spacja, tabulator lub nowa linia |
| `\S` | Znak, który nie należy do `\s` |
| `.` | Dowolny znak poza `\n`, chyba że włączono `re.DOTALL` |

`\w` nie oznacza wyłącznie liter, a `\s` nie oznacza wyłącznie spacji.

```python
import re

print(re.findall(r"\w+", "żółw_2 i kot"))  # ['żółw_2', 'i', 'kot']
print(bool(re.fullmatch(r"\d+", "١٢٣")))  # True
print(bool(re.fullmatch(r"[0-9]+", "١٢٣")))  # False

print(re.split(r"\s+", "A\tB\nC"))       # ['A', 'B', 'C']
print(re.split(r"[ \t]+", "A\tB\nC"))   # ['A', 'B\nC']
```

W formacie danych wymagającym dokładnie cyfr `0–9` wygodnie używać `[0-9]`. Przy dopasowaniu separatorów wewnątrz jednego wiersza często lepsze jest `[ \t]+` niż `\s+`.

Flaga `re.ASCII` ogranicza m.in. `\d`, `\w`, `\s` i granice słów do reguł ASCII.

---

## 5. Powtórzenia, zachłanność i alternatywy

### 5.1. Kwantyfikatory

Kwantyfikator określa liczbę powtórzeń **bezpośrednio poprzedzającego elementu**. Tym elementem może być znak, klasa znaków albo cała grupa.

| Zapis | Liczba powtórzeń |
|---|---|
| `a*` | Zero lub więcej |
| `a+` | Co najmniej jedno |
| `a?` | Zero albo jedno |
| `a{3}` | Dokładnie trzy |
| `a{2,5}` | Od dwóch do pięciu |
| `a{2,}` | Co najmniej dwa |
| `a{0,3}` | Od zera do trzech |

Porównaj wzorce wywodzące się z prostych przykładów:

| Wzorzec | Przykłady pasujące w całości | Przykład niepasujący w całości |
|---|---|---|
| `ab*c` | `ac`, `abc`, `abbbc` | `abb` |
| `ab+c` | `abc`, `abbbc` | `ac` |
| `ab?c` | `ac`, `abc` | `abbc` |
| `ab{3}c` | `abbbc` | `abbc` |
| `ab{2,4}c` | `abbc`, `abbbc`, `abbbbc` | `abc` |
| `a.*c` | `ac`, `aXYZc` | `aXYZ` |
| `a.+c` | `aXc`, `aXYZc` | `ac` |
| `a.?c` | `ac`, `aXc` | `aXYc` |
| `a.{3}c` | `aXYZc` | `aXYc` |

Porównaj także `ab+` z `(?:ab)+`:

```python
import re

print(bool(re.fullmatch(r"ab+", "abbb")))      # True
print(bool(re.fullmatch(r"ab+", "abab")))      # False
print(bool(re.fullmatch(r"(?:ab)+", "abab")))  # True
```

W pierwszym wzorcu powtarzamy tylko `b`. W drugim powtarzamy cały fragment `ab`. Zapis `(?:...)` jest grupą nieprzechwytującą — wrócimy do niego w części 7.

### 5.2. Zachłanność

Kwantyfikatory są domyślnie **zachłanne**: próbują objąć możliwie długi fragment, przy którym reszta wzorca nadal może się dopasować.

```python
import re

tekst = 'opis="pierwszy" oraz opis="drugi"'

print(re.findall(r'".*"', tekst))   # ['"pierwszy" oraz opis="drugi"']
print(re.findall(r'".*?"', tekst))  # ['"pierwszy"', '"drugi"']
```

Dopisanie `?` do kwantyfikatora daje jego wersję **niezachłanną**, która zaczyna od możliwie krótkiego dopasowania:

| Zachłanny | Niezachłanny |
|---|---|
| `*` | `*?` |
| `+` | `+?` |
| `?` | `??` |
| `{m,n}` | `{m,n}?` |

Niezachłanność nie oznacza, że całe dopasowanie zawsze będzie najkrótsze ze wszystkich możliwych. Silnik nadal musi spełnić pozostałe części wzorca.

Jeżeli szukany tekst nie może zawierać cudzysłowu, często czytelniej opisać to bezpośrednio:

```python
import re

tekst = 'opis="pierwszy" oraz opis="drugi"'
print(re.findall(r'"[^"\r\n]*"', tekst))  # ['"pierwszy"', '"drugi"']
```

### 5.3. Alternatywa i jej kolejność

Operator `|` oznacza alternatywę. Wzorzec `kot|pies` dopasowuje `kot` albo `pies`.

```python
import re

print(re.findall(r"kot|pies", "kot, pies i kot"))  # ['kot', 'pies', 'kot']
print(re.search(r"a|ab", "ab").group())            # a
print(re.search(r"ab|a", "ab").group())            # ab
```

Przy danej pozycji alternatywy są sprawdzane od lewej do prawej. Silnik przyjmuje pierwszą gałąź pozwalającą dopasować cały rozpatrywany wzorzec; nie wybiera automatycznie najdłuższej gałęzi.

Nawiasy wyznaczają zakres alternatywy:

```python
import re

for tekst in ["ABC", "XYZ", "ABC-extra", "prefix-XYZ"]:
    print(
        tekst,
        bool(re.search(r"^ABC|XYZ$", tekst)),
        bool(re.search(r"^(?:ABC|XYZ)$", tekst)),
    )
```

Pierwszy wzorzec oznacza „`ABC` na początku albo `XYZ` na końcu”. Drugi wymaga, aby cały napis był równy `ABC` albo `XYZ`. W walidacji całej wartości można też użyć `re.fullmatch(r"ABC|XYZ", tekst)`.

---

## 6. Początek, koniec i granice słów

Niektóre elementy wzorca sprawdzają **pozycję**, zamiast zużywać znak tekstu.

| Zapis | Znaczenie |
|---|---|
| `^` | Początek napisu; przy `re.MULTILINE` także początek każdego wiersza |
| `$` | Koniec napisu lub pozycja przed jego końcowym `\n`; przy `re.MULTILINE` także koniec wiersza |
| `\A` | Początek całego napisu |
| `\Z` | Ścisły koniec całego napisu |
| `\b` | Granica między `\w` i `\W` albo odpowiednia granica napisu |
| `\B` | Pozycja, która nie jest granicą słowa |

`^...$` nie zawsze zachowuje się tak samo jak `fullmatch()`, ponieważ `$` może dopasować pozycję przed końcową nową linią:

```python
import re

tekst = "ABC\n"

print(bool(re.search(r"^ABC$", tekst)))   # True
print(bool(re.fullmatch(r"ABC", tekst)))  # False
print(bool(re.search(r"\AABC\Z", tekst)))  # False
```

Granica słowa nie jest po prostu spacją:

```python
import re

tekst = "kot kotek kot_1 (kot) kot-1"
print(re.findall(r"\bkot\b", tekst))  # ['kot', 'kot', 'kot']
```

`kot_1` nie daje dopasowania, ponieważ `_` oraz `1` należą do `\w`. W `kot-1` granica występuje przed myślnikiem.

Wewnątrz klasy znaków zapis `[\b]` oznacza znak cofnięcia, a nie granicę słowa.

**Do sprawdzenia:** jak zmieni się wynik wyszukiwania cyfr przy wzorcach `[0-9]+`, `\b[0-9]+\b` i `\A[0-9]+\Z` dla tekstu `abc123 45 67xyz`?

---

## 7. Grupy i obiekt Match

### 7.1. Po co tworzymy grupy?

Grupy pełnią dwie podstawowe funkcje:

1. Łączą kilka elementów wzorca w jedną całość, np. na potrzeby powtarzania lub alternatywy.
2. Mogą zapamiętywać dopasowany fragment, aby później odczytać go w programie albo wykorzystać w dalszej części wzorca.

**Grupowanie nie musi oznaczać przechwytywania.** Typ grupy wybieramy zależnie od tego, czy potrzebujemy jej zawartości.

### 7.2. Grupy numerowane: `(...)`

```python
import re

wynik = re.fullmatch(r"([A-Z]{2})-([0-9]{3})", "AB-127")

if wynik:
    print(wynik.group())      # AB-127
    print(wynik.group(0))     # AB-127
    print(wynik.group(1))     # AB
    print(wynik.group(2))     # 127
    print(wynik.group(1, 2))  # ('AB', '127')
    print(wynik.groups())     # ('AB', '127')
```

Grupa `0` to **całe dopasowanie**. Grupy przechwytujące numeruje się od `1`, według kolejności ich nawiasów otwierających we wzorcu.

`group(2)` nadal zwraca napis `"127"`. Jeżeli potrzebna jest liczba, wykonujemy `int(wynik.group(2))`.

### 7.3. Zagnieżdżone grupy

```python
import re

wynik = re.fullmatch(r"((AB)([0-9]{2}))-([a-z]+)", "AB12-kot")

if wynik:
    print(wynik.group(0))  # AB12-kot
    print(wynik.group(1))  # AB12
    print(wynik.group(2))  # AB
    print(wynik.group(3))  # 12
    print(wynik.group(4))  # kot
```

Dodanie nawiasów przechwytujących na początku rozbudowanego wzorca zmienia numery późniejszych grup. W większych wzorcach warto stosować nazwy i grupy nieprzechwytujące.

### 7.4. Grupy nazwane: `(?P<nazwa>...)`

```python
import re

wzorzec = r"(?P<prefiks>[A-Z]{2})-(?P<numer>[0-9]{3})"
wynik = re.fullmatch(wzorzec, "AB-127")

if wynik:
    print(wynik.group("prefiks"))  # AB
    print(wynik.group("numer"))    # 127
    print(wynik.groupdict())       # {'prefiks': 'AB', 'numer': '127'}
    print(wynik.group(1))          # AB
```

Grupa nazwana jest również grupą numerowaną. Można odwoływać się do niej przez nazwę albo numer. W kodzie przetwarzającym dane nazwa zwykle lepiej objaśnia znaczenie pola.

Nazwa musi być poprawną nazwą identyfikatora Pythona. W jednym wzorcu nie można zadeklarować dwóch grup o tej samej nazwie, również w różnych gałęziach alternatywy.

Przy obsłudze dwóch różnych formatów można utworzyć dwa wzorce albo zastosować różne nazwy grup, a następnie ujednolicić wynik w Pythonie.

### 7.5. Grupy nieprzechwytujące: `(?:...)`

```python
import re

wzorzec = r"(?:PL|DE)-(?P<numer>[0-9]{3})"
wynik = re.fullmatch(wzorzec, "PL-123")

if wynik:
    print(wynik.groups())     # ('123',)
    print(wynik.groupdict())  # {'numer': '123'}
```

Fragment `PL|DE` jest zgrupowany, ale nie zostaje zapisany jako oddzielna grupa. Dzięki temu grupa `numer` ma numer `1`.

Używaj `(?:...)`, gdy nawiasy służą jedynie do zbudowania struktury wzorca. Używaj `(...)` lub `(?P<nazwa>...)`, gdy potrzebujesz dopasowanego fragmentu.

### 7.6. Grupy opcjonalne i puste dopasowania

```python
import re

wzorzec = r"(?P<nazwa>[A-Z]+)(?:-(?P<wersja>[0-9]+))?"

for tekst in ["ABC", "ABC-12"]:
    wynik = re.fullmatch(wzorzec, tekst)
    if wynik:
        print(wynik.groupdict())
```

Wynik:

```text
{'nazwa': 'ABC', 'wersja': None}
{'nazwa': 'ABC', 'wersja': '12'}
```

Jeżeli opcjonalna grupa nie uczestniczyła w dopasowaniu, `group()` zwraca dla niej `None`. To inna sytuacja niż dopasowanie pustego napisu `""` przez grupę taką jak `([0-9]*)`.

Można określić wartość zastępczą: `wynik.groups(default="brak")` albo `wynik.groupdict(default="brak")`.

### 7.7. Powtarzana grupa nie przechowuje historii

```python
import re

wynik = re.fullmatch(r"([A-Z][0-9])+", "A1B2C3")

if wynik:
    print(wynik.group(0))  # A1B2C3
    print(wynik.group(1))  # C3

print(re.findall(r"[A-Z][0-9]", "A1B2C3"))  # ['A1', 'B2', 'C3']
```

Wielokrotnie użyta grupa udostępnia ostatnio przechwycony fragment. Aby zebrać wszystkie powtarzające się elementy, wykonaj oddzielne wyszukiwanie przez `findall()` lub `finditer()`.

### 7.8. Położenie dopasowania

```python
import re

tekst = "Kod: AB-127."
wynik = re.search(r"(?P<prefiks>[A-Z]{2})-(?P<numer>[0-9]{3})", tekst)

if wynik:
    print(wynik.start())          # 5
    print(wynik.end())            # 11
    print(wynik.span())           # (5, 11)
    print(wynik.span("numer"))   # (8, 11)
    print(tekst[wynik.start():wynik.end()])  # AB-127
```

Indeksy są liczone od `0`. Początek należy do dopasowania, a koniec wskazuje pierwszy znak **za dopasowaniem**. Jest to taka sama konwencja jak w wycinkach `tekst[start:koniec]`.

Dla grupy opcjonalnej, która nie uczestniczyła w dopasowaniu, `span(nazwa)` zwraca `(-1, -1)`.

---

## 8. Odwołania wsteczne

### 8.1. Powtórzenie tego samego tekstu

Odwołanie wsteczne wymaga ponownego wystąpienia tekstu przechwyconego wcześniej przez grupę. To mocniejszy warunek niż powtórzenie samego wzorca.

```python
import re

print(bool(re.fullmatch(r"([A-Z])[A-Z]", "AB")))  # True
print(bool(re.fullmatch(r"([A-Z])\1", "AB")))     # False
print(bool(re.fullmatch(r"([A-Z])\1", "AA")))     # True
```

Pierwszy wzorzec dopuszcza dwie dowolne wielkie litery. Drugi wymaga dwukrotnego wystąpienia **tej samej** litery.

### 8.2. Numery i nazwy

We wzorcu można użyć:

- `\1`, `\2`, … — odwołania przez numer;
- `(?P=nazwa)` — odwołania przez nazwę.

```python
import re

tekst = "To to jest jest przykład."
wzorzec = r"\b(?P<slowo>\w+)\s+(?P=slowo)\b"

for wynik in re.finditer(wzorzec, tekst, flags=re.IGNORECASE):
    print(wynik.group(0), "->", wynik.group("slowo"))
```

Wynik:

```text
To to -> To
jest jest -> jest
```

Flaga `re.IGNORECASE` wpływa również na porównanie w odwołaniu wstecznym. Bez tej flagi `To` oraz `to` byłyby różnymi fragmentami.

### 8.3. Ten sam separator

```python
import re

wzorzec = (
    r"(?P<rok>[0-9]{4})(?P<separator>[-/.])"
    r"(?P<miesiac>[0-9]{2})(?P=separator)(?P<dzien>[0-9]{2})"
)

for tekst in ["2026-11-19", "2026/11/19", "2026.11.19", "2026-11/19"]:
    print(tekst, bool(re.fullmatch(wzorzec, tekst)))
```

Trzy pierwsze wartości pasują, a ostatnia nie. Samo dwukrotne użycie `[-/.]` dopuściłoby różne separatory. Odwołanie `(?P=separator)` wymaga tego samego znaku.

Wzorzec sprawdza zapis daty. Nie potwierdza, że podana data istnieje w kalendarzu.

### 8.4. Ten sam znak otwierający i zamykający

```python
import re

wzorzec = r'''(?P<cytat>["'])(?P<tresc>[^"'\r\n]*)(?P=cytat)'''

for tekst in ['"kot"', "'pies'", "\"kot'"]:
    wynik = re.fullmatch(wzorzec, tekst)
    print(tekst, wynik.group("tresc") if wynik else "BŁĄD")
```

W tym formacie treść nie zawiera żadnych cudzysłowów ani apostrofów. Grupa `cytat` zapamiętuje rodzaj otwarcia, a odwołanie wsteczne wymaga takiego samego zamknięcia.

**Nie pomyl zapisów:** `(?P<nazwa>...)` tworzy grupę, natomiast `(?P=nazwa)` odwołuje się do już przechwyconej zawartości.

---

## 9. Wszystkie dopasowania

### 9.1. `findall()` i wpływ grup

`findall()` zwraca listę. Zawartość tej listy zależy od liczby grup przechwytujących:

| Liczba grup przechwytujących | Elementy wyniku |
|---:|---|
| 0 | Całe dopasowania jako napisy |
| 1 | Zawartość tej jednej grupy jako napisy |
| 2 lub więcej | Krotki zawierające wartości grup |

```python
import re

tekst = "AB-12 CD-34"

print(re.findall(r"[A-Z]{2}-[0-9]{2}", tekst))
# ['AB-12', 'CD-34']

print(re.findall(r"([A-Z]{2})-[0-9]{2}", tekst))
# ['AB', 'CD']

print(re.findall(r"([A-Z]{2})-([0-9]{2})", tekst))
# [('AB', '12'), ('CD', '34')]

print(re.findall(r"(?:[A-Z]{2})-[0-9]{2}", tekst))
# ['AB-12', 'CD-34']
```

Grupy nazwane także wpływają na postać wyniku `findall()`. Funkcja nie zwraca słowników z nazwami grup.

Dla grupy opcjonalnej, która nie uczestniczyła w dopasowaniu, `findall()` umieszcza pusty napis. Różni się to od `Match.group()`, które w tej sytuacji zwraca `None`.

### 9.2. `finditer()`

`finditer()` udostępnia kolejne obiekty `Match`. Wybierz tę funkcję, gdy potrzebujesz jednocześnie grup i pozycji dopasowań.

```python
import re

tekst = "AB-12 CD-34"
wzorzec = r"(?P<kod>[A-Z]{2})-(?P<numer>[0-9]{2})"

for wynik in re.finditer(wzorzec, tekst):
    print(wynik.groupdict(), wynik.span())
```

Wynik:

```text
{'kod': 'AB', 'numer': '12'} (0, 5)
{'kod': 'CD', 'numer': '34'} (6, 11)
```

Obie funkcje standardowo zwracają dopasowania **nienakładające się**. Po znalezieniu niepustego dopasowania zwykłe wyszukiwanie przechodzi za jego koniec. Sposób odnajdywania nakładających się fragmentów poznamy w części 13.

### 9.3. Dopasowanie pustego napisu

Wzorce zawierające `*` lub `?` mogą pasować również bez zużycia znaku:

```python
import re

print(re.findall(r"[0-9]*", "a12b"))  # ['', '12', '', '']
print(re.findall(r"[0-9]+", "a12b"))  # ['12']
```

Pusty wynik pojedynczego dopasowania nie jest tym samym co brak dopasowania. Jeżeli interesują Cię wyłącznie niepuste liczby, użyj `+`.

---

## 10. Dzielenie i zamiana tekstu

### 10.1. `re.split()`

Funkcja dzieli napis w miejscach dopasowanych przez wzorzec separatora:

```python
import re

tekst = "Ala, Jan; Ewa | Piotr"
print(re.split(r"\s*[,;|]\s*", tekst))
# ['Ala', 'Jan', 'Ewa', 'Piotr']

print(re.split(r"[,;]", "A,B;C", maxsplit=1))
# ['A', 'B;C']
```

W klasie `[,;|]` pionowa kreska jest dosłownym separatorem, a nie operatorem alternatywy.

Jeżeli wzorzec separatora ma grupę przechwytującą, jej zawartość również trafia do listy:

```python
import re

print(re.split(r"([,;])", "A,B;C"))    # ['A', ',', 'B', ';', 'C']
print(re.split(r"(?:[,;])", "A,B;C"))  # ['A', 'B', 'C']
```

Separatory na początku i końcu napisu mogą dać puste elementy wynikowej listy. Usuwaj je tylko wtedy, gdy rzeczywiście nie niosą informacji w danym formacie.

### 10.2. `re.sub()`

`sub()` zastępuje dopasowane fragmenty i zwraca **nowy napis**. Nie zmienia oryginalnej zmiennej automatycznie.

```python
import re

tekst = "ATTTGgccTaC"
wynik = re.sub(r"[a-z]", "", tekst)

print(wynik)  # ATTTGTC
print(tekst)  # ATTTGgccTaC

print(re.sub(r"[0-9]+", "#", "A12 B34 C56", count=2))
# A# B# C56
```

Parametr `count=0`, będący wartością domyślną, oznacza zamianę wszystkich dopasowań.

### 10.3. Grupy w tekście zastępującym

W tekście zastępującym odwołujemy się do grup przez `\g<1>` albo `\g<nazwa>`:

```python
import re

wzorzec = r"(?P<litery>[A-Z]+)-(?P<numer>[0-9]+)"
tekst = "AB-12 CD-34"

print(re.sub(wzorzec, r"\g<numer>:\g<litery>", tekst))
# 12:AB 34:CD
```

Zwróć uwagę na różne konteksty:

| Miejsce | Odwołanie do grupy nazwanej |
|---|---|
| Dalsza część wzorca | `(?P=nazwa)` |
| Odczyt wyniku w Pythonie | `wynik.group("nazwa")` |
| Napis zastępujący w `sub()` | `\g<nazwa>` |

Zapis `\g<1>0` jednoznacznie oznacza zawartość grupy `1` i znak `0`. Samo `\10` oznaczałoby odwołanie do grupy `10`.

### 10.4. Funkcja jako zamiennik

Gdy zamiana wymaga obliczeń albo decyzji, jako drugi argument `sub()` przekazujemy funkcję. Otrzymuje ona obiekt `Match` i zwraca napis zastępujący dopasowanie.

```python
import re

def milisekundy_na_sekundy(wynik):
    liczba = int(wynik.group("czas"))
    return f"{liczba / 1000:.3f} s"

tekst = "Etap A: 250 ms; etap B: 1500 ms."
wzorzec = r"\b(?P<czas>[0-9]+)[ \t]*ms\b"

print(re.sub(wzorzec, milisekundy_na_sekundy, tekst))
# Etap A: 0.250 s; etap B: 1.500 s.
```

Funkcja może korzystać także ze słownika, np. nadającego powtarzającym się identyfikatorom stałe zamienniki. Trzeba wtedy określić, czy wielkość liter wpływa na tożsamość identyfikatora.

Funkcję przekazujemy przez jej nazwę, bez dopisywania `()`: `re.sub(wzorzec, funkcja, tekst)`.

### 10.5. `subn()`

`subn()` działa jak `sub()`, ale zwraca parę: nowy napis i liczbę wykonanych zamian.

```python
import re

wynik, liczba = re.subn(r"[0-9]+", "#", "A12 B34")
print(wynik)   # A# B#
print(liczba)  # 2
```

`re.escape()` służy do budowania **wzorców**, a nie do przygotowania napisu zastępującego. Jeżeli zamiennik ma być potraktowany całkowicie dosłownie, również gdy zawiera ukośniki, można zwrócić go z funkcji przekazanej do `sub()`.

---

## 11. Flagi

Flagi modyfikują sposób interpretacji wzorca.

| Flaga | Skrót | Działanie |
|---|---|---|
| `re.IGNORECASE` | `re.I` | Pomija różnice wielkości liter |
| `re.MULTILINE` | `re.M` | Pozwala `^` i `$` odnosić się do poszczególnych wierszy |
| `re.DOTALL` | `re.S` | Pozwala kropce dopasować także nową linię |
| `re.VERBOSE` | `re.X` | Pozwala rozłożyć wzorzec na wiersze i dodawać komentarze |
| `re.ASCII` | `re.A` | Ogranicza m.in. skrócone klasy znaków do ASCII |

Flagi łączymy operatorem `|`, np. `flags=re.IGNORECASE | re.ASCII`.

### 11.1. Wielkość liter

```python
import re

print(re.findall(r"atg", "ATG atg Atg", flags=re.IGNORECASE))
# ['ATG', 'atg', 'Atg']
```

Wynik zachowuje oryginalną postać fragmentów. Flaga zmienia regułę dopasowania, ale nie przekształca samego tekstu na małe lub wielkie litery.

Przy wymaganiu ścisłego alfabetu ASCII można połączyć `IGNORECASE` z `ASCII`. Ma to znaczenie również dla zakresów takich jak `[A-Z]`, które przy dopasowaniu bez rozróżniania wielkości liter mogą uwzględniać dodatkowe znaki Unicode.

### 11.2. `MULTILINE` a `DOTALL`

```python
import re

tekst = "START\nABC\nSTOP"

print(re.findall(r"^ABC$", tekst))                       # []
print(re.findall(r"^ABC$", tekst, flags=re.MULTILINE))   # ['ABC']
print(bool(re.search(r"START.*STOP", tekst)))            # False
print(bool(re.search(r"START.*STOP", tekst, flags=re.DOTALL)))  # True
```

`MULTILINE` wpływa na kotwice, a `DOTALL` na kropkę. Włączenie jednej flagi nie włącza drugiej. `MULTILINE` nie powoduje też, że `match()` zaczyna wyszukiwać na początku każdego wiersza.

### 11.3. Czytelne wzorce z `VERBOSE`

```python
import re

wzorzec = re.compile(
    r"""
    (?P<prefiks>[A-Z]{2})   # dwie litery
    -                      # separator
    (?P<numer>[0-9]{3})     # trzy cyfry
    (?:\.(?P<typ>txt|dat))? # opcjonalne rozszerzenie
    """,
    flags=re.VERBOSE,
)

wynik = wzorzec.fullmatch("AB-123.txt")
if wynik:
    print(wynik.groupdict())
# {'prefiks': 'AB', 'numer': '123', 'typ': 'txt'}
```

Przy `VERBOSE` białe znaki zapisane poza klasami znaków są zwykle pomijane, a `#` rozpoczyna komentarz do końca wiersza. Dosłowną spację zapisz np. jako `[ ]`, a znak `#` jako `\#` albo `[#]`.

### 11.4. Flagi wewnątrz wzorca

Można włączyć flagę dla całego wzorca, np. `(?i)abc`, albo tylko dla fragmentu, np. `(?i:abc)`:

```python
import re

wzorzec = r"(?i:abc)-[A-Z]{2}"
print(bool(re.fullmatch(wzorzec, "AbC-XY")))  # True
print(bool(re.fullmatch(wzorzec, "AbC-xy")))  # False
```

Zapis `(?i:...)` nie tworzy grupy przechwytującej. Globalne flagi w formie `(?i)` umieszczaj na samym początku wzorca.

---

## 12. Lookahead i lookbehind

### 12.1. Sprawdzanie otoczenia bez jego zużywania

Lookaround to warunek dotyczący tekstu przed lub za aktualną pozycją. Sam warunek **nie zużywa znaków**.

| Konstrukcja | Warunek |
|---|---|
| `X(?=Y)` | Dopasuj `X`, jeżeli bezpośrednio za nim pasuje `Y` |
| `X(?!Y)` | Dopasuj `X`, jeżeli bezpośrednio za nim nie pasuje `Y` |
| `(?<=Y)X` | Dopasuj `X`, jeżeli bezpośrednio przed nim pasuje `Y` |
| `(?<!Y)X` | Dopasuj `X`, jeżeli bezpośrednio przed nim nie pasuje `Y` |

### 12.2. Lookahead dodatni i ujemny

```python
import re

tekst = "12mg 34g 56mg"
print(re.findall(r"[0-9]+(?=mg\b)", tekst))  # ['12', '56']
```

Jednostka `mg` jest sprawdzana, ale nie wchodzi do wyniku.

```python
import re

tekst = "kot kotek kot-1"
print(re.findall(r"kot(?!ek)", tekst))  # ['kot', 'kot']
```

Tutaj odpada `kot` bezpośrednio poprzedzające `ek`. To nie jest ogólne sprawdzenie całego słowa — warunek dotyczy wyłącznie wskazanego dalszego fragmentu.

**Uwaga na cofanie dopasowania:** `[0-9]+(?!mg)` może dopasować `1` w `12mg`, ponieważ po `1` znajduje się `2`, a nie `mg`. Gdy sprawdzasz całe pole, użyj `fullmatch()`. Gdy wyszukujesz tokeny, zaprojektuj także ich granice.

### 12.3. Lookbehind dodatni i ujemny

```python
import re

tekst = "ID=123 REF=456 ID=789"
print(re.findall(r"(?<=ID=)[0-9]+", tekst))  # ['123', '789']

tekst2 = "A12 34 B56"
print(re.findall(r"(?<!\w)[0-9]+(?!\w)", tekst2))  # ['34']
```

W standardowym module `re` lookbehind musi mieć **stałą długość**. `(?<=ID=)` spełnia ten warunek. Konstrukcja taka jak `(?<=ID=\s*)` nie spełnia go, ponieważ `\s*` może mieć różne długości.

W takim przypadku można zwyczajnie dopasować prefiks i przechwycić interesującą część:

```python
import re

tekst = "ID=  123"
wynik = re.search(r"ID=[ \t]*(?P<numer>[0-9]+)", tekst)
if wynik:
    print(wynik.group("numer"))  # 123
```

Lookaround sam w sobie nie tworzy grupy przechwytującej. Można jednak umieścić grupę przechwytującą wewnątrz dodatniego lookaround i odczytać jej zawartość po udanym dopasowaniu.

---

## 13. Dopasowania nakładające się

W napisie `ABABA` fragment `ABA` występuje na pozycjach `0–2` i `2–4`. Zwykłe wyszukiwanie znajduje tylko pierwsze wystąpienie:

```python
import re

tekst = "ABABA"
print(re.findall(r"ABA", tekst))  # ['ABA']
```

Aby sprawdzać możliwość dopasowania od każdej kolejnej pozycji, użyj dodatniego lookahead z grupą przechwytującą:

```python
import re

tekst = "ABABA"
wzorzec = r"(?=(?P<fragment>ABA))"

for wynik in re.finditer(wzorzec, tekst):
    print(
        wynik.group("fragment"),
        wynik.span(0),
        wynik.span("fragment"),
    )
```

Wynik:

```text
ABA (0, 0) (0, 3)
ABA (2, 2) (2, 5)
```

Całe dopasowanie lookahead ma długość `0`, ponieważ warunek nie zużywa znaków. Dopasowany fragment i jego rzeczywiste granice znajdują się w **grupie `fragment`**.

Jeżeli raportujesz pozycje w sekwencji numerowane od `1`, z początkiem i końcem włącznie, przelicz je tak:

```python
import re

tekst = "ABABA"

for wynik in re.finditer(r"(?=(?P<fragment>ABA))", tekst):
    start0, koniec0 = wynik.span("fragment")
    print(start0 + 1, koniec0, wynik.group("fragment"))
```

Wynik to `1 3 ABA` i `3 5 ABA`. Koniec wycinka liczonego od zera ma tę samą wartość liczbową co pozycja ostatniego znaku przy numeracji od jedynki.

**Ważne:** lookahead z zachłannym motywem o zmiennej długości daje standardowo jedno, wybrane przez silnik dopasowanie od danej pozycji. Nie wylicza automatycznie wszystkich możliwych długości motywu rozpoczynającego się w tym samym miejscu.

---

## 14. Kompilowanie i budowanie wzorców

### 14.1. `re.compile()`

Wzorzec używany wielokrotnie można utworzyć raz:

```python
import re

kod = re.compile(r"(?P<litery>[A-Z]{2})-(?P<numer>[0-9]{3})")

for tekst in ["AB-123", "CD-456", "błędny"]:
    wynik = kod.fullmatch(tekst)
    if wynik:
        print(wynik.groupdict())
```

Obiekt `Pattern` udostępnia m.in. metody `search()`, `match()`, `fullmatch()`, `findall()`, `finditer()`, `split()`, `sub()` i `subn()`.

Skompilowany wzorzec porządkuje kod i pozwala nadać nazwę regule. Moduł `re` przechowuje także pamięć podręczną ostatnich wzorców, dlatego samo dodanie `compile()` nie gwarantuje zauważalnego przyspieszenia każdego programu.

### 14.2. Dosłowne dane i `re.escape()`

```python
import re

szukana_nazwa = "wynik(1).txt"
tekst = "Pliki: wynik(1).txt oraz wynik1Xtxt"

wzorzec = re.escape(szukana_nazwa)
print(re.findall(wzorzec, tekst))  # ['wynik(1).txt']
```

Bez `re.escape()` nawiasy i kropka zostałyby potraktowane jako elementy składni regexu.

Przed zbudowaniem wzorca ustal, czy zmienna zawiera **tekst dosłowny**, czy **świadomie podany regex**. `re.escape()` jest odpowiednie tylko w pierwszym przypadku.

### 14.3. Wzorce i f-stringi

Można połączyć napis surowy z f-stringiem:

```python
import re

prefiks = "AB+"
liczba_cyfr = 3
wzorzec = rf"{re.escape(prefiks)}-[0-9]{{{liczba_cyfr}}}"

print(wzorzec)                              # AB\+-[0-9]{3}
print(bool(re.fullmatch(wzorzec, "AB+-123")))  # True
```

Podwojone nawiasy klamrowe `{{` i `}}` stają się dosłownymi klamrami wewnątrz wynikowego napisu. To pozwala utworzyć kwantyfikator `{3}`.

### 14.4. Błąd wzorca a brak dopasowania

Niepoprawna składnia regexu jest czymś innym niż poprawny wzorzec, który nie pasuje do danych:

```python
import re

try:
    wzorzec = re.compile(r"[A-Z")
except re.error as blad:
    print("Niepoprawny wzorzec:", blad)

print(re.fullmatch(r"[A-Z]+", "123"))  # None
```

Niedomknięta klasa znaków powoduje wyjątek `re.error`. Brak dopasowania w drugim przypadku jest zwykłym wynikiem działania funkcji.

---

## 15. Regex i znaczenie danych

### 15.1. Format nie potwierdza poprawności wartości

Wzorzec `[0-9]{4}-[0-9]{2}-[0-9]{2}` dopuszcza zarówno `2026-11-19`, jak i `2026-02-31`. Oba napisy mają odpowiedni kształt, ale tylko pierwszy opisuje rzeczywistą datę.

```python
import re
from datetime import datetime

wzorzec = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}")

for tekst in ["2026-11-19", "2026-02-31", "19.11.2026"]:
    if wzorzec.fullmatch(tekst) is None:
        print(tekst, "-> niepoprawny format")
        continue

    try:
        data = datetime.strptime(tekst, "%Y-%m-%d")
    except ValueError:
        print(tekst, "-> nieistniejąca data")
    else:
        print(tekst, "->", data.strftime("%d.%m.%Y"))
```

Podobnie regex nie sprawdzi sam, czy istnieje znaleziony plik, czy numer próbki należy do danego eksperymentu albo czy pomiar ma sens fizyczny. Odpowiednie warunki sprawdzamy dalej w Pythonie.

### 15.2. Liczby rzeczywiste

W danych może występować znak liczby, część ułamkowa oraz wykładnik:

```python
import re

wzorzec = re.compile(
    r"[+-]?[0-9]+(?:[.,][0-9]+)?(?:[eE][+-]?[0-9]+)?"
)

for tekst in ["12", "-3.5", "+0,25", "1.2e-3", ".5", "2.", "1,2.3"]:
    print(tekst, bool(wzorzec.fullmatch(tekst)))
```

W tym konkretnym formacie:

- część całkowita jest obowiązkowa;
- ułamek, jeżeli występuje, musi mieć co najmniej jedną cyfrę;
- dopuszczamy kropkę albo przecinek;
- wykładnik jest opcjonalny i musi zawierać cyfry.

Dlatego `.5` i `2.` nie pasują, choć `float()` potrafi odczytać takie napisy. Wzorzec opisuje przyjęty format danych, który może być węższy niż możliwości konwersji Pythona.

Przed konwersją przecinek można zamienić na kropkę. Po konwersji warto sprawdzić skończoność liczby, jeżeli wymaga tego zadanie:

```python
import math

tekst = "1e309"
liczba = float(tekst)
print(liczba)                 # inf
print(math.isfinite(liczba))  # False
```

### 15.3. Sprawdzanie całej sekwencji

```python
import re

sekwencja = "ACGTNX"

print(re.findall(r"[ACGT]+", sekwencja))             # ['ACGT']
print(bool(re.fullmatch(r"[ACGT]+", sekwencja)))     # False
```

`findall()` wydobywa poprawne fragmenty i może pominąć niepoprawne znaki. Do sprawdzenia alfabetu **całej** sekwencji potrzebne jest `fullmatch()`.

Usunięcie niepasujących znaków przez `sub()` nie jest sprawdzeniem poprawności. Zmienia dane, dlatego wymaga odrębnego uzasadnienia w specyfikacji programu.

---

## 16. Przykłady z wcześniejszymi modułami

### 16.1. `os`: wybór plików i grupy w nazwie

Poniższy kod przegląda bieżący katalog. Wynik zależy od znajdujących się w nim plików.

```python
import os
import re

wzorzec = re.compile(
    r"pomiar_(?P<data>[0-9]{4}-[0-9]{2}-[0-9]{2})_(?P<seria>[A-Z])\.txt"
)

for nazwa in sorted(os.listdir(".")):
    sciezka = os.path.join(".", nazwa)
    if not os.path.isfile(sciezka):
        continue

    wynik = wzorzec.fullmatch(nazwa)
    if wynik:
        print(nazwa, wynik.group("data"), wynik.group("seria"))
```

Sprawdzenie `os.path.isfile()` odróżnia plik od katalogu, który może mieć podobną nazwę. Regex analizuje jedynie sam napis z nazwą.

### 16.2. Pliki, `enumerate()` i obsługa błędnego wiersza

Przykład tworzy mały plik demonstracyjny `demo_regex/wartosci.txt`, a następnie go odczytuje. Obsługa błędnego wiersza nie przerywa przetwarzania pozostałych danych.

```python
import os
import re

os.makedirs("demo_regex", exist_ok=True)
sciezka = os.path.join("demo_regex", "wartosci.txt")

with open(sciezka, "w", encoding="utf-8") as plik:
    plik.write("A=12\nB=34\nniepoprawny wiersz\nC=56\n")

wzorzec = re.compile(r"(?P<klucz>[A-Z])=(?P<wartosc>[0-9]+)")

with open(sciezka, encoding="utf-8") as plik:
    for nr_wiersza, wiersz in enumerate(plik, start=1):
        tekst = wiersz.rstrip("\r\n")
        wynik = wzorzec.fullmatch(tekst)

        if wynik is None:
            print(f"Wiersz {nr_wiersza}: niepoprawny format")
            continue

        print(wynik.group("klucz"), int(wynik.group("wartosc")))
```

`rstrip("\r\n")` usuwa końce wiersza. `strip()` usunęłoby także spacje i tabulatory na obu końcach tekstu. Wybór zależy od tego, czy format dopuszcza takie znaki.

### 16.3. `datetime`: obliczenia po wydobyciu daty

```python
import re
from datetime import datetime

tekst = "Rozpoczęcie: 2026-11-19 10:00"
wynik = re.search(
    r"(?P<data>[0-9]{4}-[0-9]{2}-[0-9]{2})[ ]"
    r"(?P<godzina>[0-9]{2}:[0-9]{2})",
    tekst,
)

if wynik:
    zapis = wynik.group("data") + " " + wynik.group("godzina")
    poczatek = datetime.strptime(zapis, "%Y-%m-%d %H:%M")
    koniec = datetime(2026, 11, 19, 11, 30)
    print((koniec - poczatek).total_seconds() / 60)  # 90.0
```

### 16.4. `random` i `time`: generowanie danych do sprawdzenia

```python
import random
import re
import time

random.seed(42)
dane = [f"ID-{random.randint(0, 999):03d}" for _ in range(1000)]
dane.extend(["ID-12", "ID-ABC", "prefix-ID-123"])
wzorzec = re.compile(r"ID-[0-9]{3}")

start = time.perf_counter()
poprawne = [tekst for tekst in dane if wzorzec.fullmatch(tekst)]
czas = time.perf_counter() - start

print(len(poprawne))       # 1000
print(f"Czas: {czas:.6f} s")
```

Ziarno generatora pomaga odtworzyć dane wejściowe. Czas wykonania może się zmieniać między uruchomieniami; tak mały przykład służy do przypomnienia pomiaru czasu, a nie do porównywania wydajności komputerów.

---

## 17. Konstrukcje rozszerzające

Ta część uzupełnia przegląd składni grup. **Nie jest wymagana do rozwiązania zadań na punkty.**

### 17.1. Warunek zależny od udziału grupy

Konstrukcja `(?(id)tak|nie)` wybiera gałąź zależnie od tego, czy wskazana grupa uczestniczyła w dopasowaniu. `id` może być numerem albo nazwą grupy.

```python
import re

wzorzec = r"(?P<otwarcie>\()?[0-9]+(?(otwarcie)\))"

for tekst in ["123", "(123)", "(123", "123)"]:
    print(tekst, bool(re.fullmatch(wzorzec, tekst)))
```

Wynik to kolejno `True`, `True`, `False`, `False`. Jeżeli przechwycono nawias otwierający, wzorzec wymaga także zamykającego. Pusta gałąź „nie” jest tutaj pominięta.

Warunek dotyczy udziału grupy w dopasowaniu. Nie jest dowolnym warunkiem Pythona ani porównaniem liczbowej wartości grupy.

### 17.2. Cofanie dopasowania

Silnik może cofać wcześniejsze wybory, jeżeli dalsza część wzorca nie pasuje. Na przykład w `a+a` pierwsze `a+` musi zostawić jedno `a` dla końcowego elementu.

Unikaj niepotrzebnie zagnieżdżonych powtórzeń, takich jak `(a+)+`, szczególnie dla długich tekstów, które ostatecznie nie pasują. W wielu przypadkach wystarczy prostsze `a+`.

Najpierw opisz strukturę danych możliwie konkretnie: użyj ograniczonej klasy znaków, jawnego separatora i odpowiedniej liczby powtórzeń.

### 17.3. Zestawienie rodzajów nawiasów

| Konstrukcja | Rola | Tworzy grupę przechwytującą? |
|---|---|---|
| `(...)` | Grupowanie i przechwycenie | Tak |
| `(?P<nazwa>...)` | Grupowanie i przechwycenie pod nazwą | Tak |
| `(?:...)` | Samo grupowanie | Nie |
| `(?P=nazwa)` | Odwołanie do przechwyconego tekstu | Nie |
| `(?=...)`, `(?!...)` | Sprawdzenie dalszego tekstu | Nie, ale wnętrze może zawierać grupy |
| `(?<=...)`, `(?<!...)` | Sprawdzenie poprzedzającego tekstu | Nie, ale wnętrze może zawierać grupy |
| `(?i:...)` | Lokalna zmiana flag | Nie |
| `(?#komentarz)` | Komentarz we wzorcu | Nie |
| `(?(id)tak\|nie)` | Wybór zależny od udziału grupy | Nie, ale gałęzie mogą zawierać grupy |
| `(?>...)` | Grupowanie atomowe, Python 3.11+ | Nie |

---

## 18. Zadania do oddania

## Zadanie — Analizator motywów w sekwencjach białkowych — 5 pkt

Napisz program, który odczytuje plik wielosekwencyjny FASTA, sprawdza poprawność rekordów i wyszukuje motywy białkowe za pomocą wyrażeń regularnych. Program ma odnajdywać również trafienia nakładające się, raportować ich pozycje i otoczenie, obliczać pokrycie sekwencji oraz zapisywać wybrane i zamaskowane białka.

Pracujesz nad **jednym programem `zadanie_01.py`**. Poszczególne części poniżej są etapami tego samego zadania, za które łącznie można uzyskać **5 pkt**.

### A. Organizacja programu i dane wejściowe

- Korzystaj z biblioteki standardowej. Głównym narzędziem analizy tekstu ma być `re`.
- Program uruchamiaj poleceniem `python3 zadanie_01.py`, mając katalog `06/` jako bieżący katalog roboczy.
- Przez `input()` pobierz ścieżkę do pliku FASTA. Dla dołączonych danych jest to `dane/sekwencje.fasta`.
- Pobierz także długość kontekstu `k` oraz minimalną liczbę trafień `n`, według której będą wybierane białka. Obie wartości muszą być liczbami całkowitymi nieujemnymi. Puste odpowiedzi oznaczają odpowiednio `k = 2` i `n = 3`. Przy błędnej wartości ponów pytanie.
- Umożliw określenie dodatkowego motywu `M4` według zasad z części D. Obsługa tej możliwości jest wymagana; użytkownik może jednak wybrać analizę bez `M4`.
- Pliki wejściowe pozostaw bez zmian. Wyniki zapisuj w katalogu `wyniki_06/`, tworzonym przez `os.makedirs(..., exist_ok=True)`.
- Pliki tekstowe odczytuj i zapisuj jako UTF-8. W TSV separatorem jest pojedynczy tabulator `\t`, a pierwszy wiersz zawiera nazwy kolumn.
- Wydziel funkcje odpowiadające etapom pracy, np. odczytowi FASTA, przygotowaniu wzorców, wyszukiwaniu trafień, maskowaniu i zapisowi raportów. Uruchomienie programu umieść pod `if __name__ == "__main__":`.
- Obsłuż błędy plikowe, np. `FileNotFoundError`, `PermissionError` lub inne `OSError`. Wyświetl komunikat wyjaśniający problem.

### B. Odczyt i sprawdzenie FASTA

1. Przed analizą pojedynczego wiersza zastosuj `strip()`. Puste wiersze pomijaj.
2. Nowy rekord rozpoczyna każdy wiersz zaczynający się od `>`. Rekord trwa do następnego takiego wiersza albo do końca pliku. Pamiętaj o przetworzeniu ostatniego rekordu, również gdy plik nie kończy się znakiem nowej linii.
3. Nagłówek ma postać `>SEQddd` albo `>SEQddd opis`, gdzie `ddd` oznacza dokładnie trzy cyfry ASCII. Opis, jeżeli występuje, jest oddzielony od identyfikatora co najmniej jedną spacją lub tabulatorem i jest niepusty.
4. Sprawdź **cały nagłówek** przez `fullmatch()`. Użyj grup nazwanych `id` i `opis`; opis może być grupą opcjonalną. Do zapisu FASTA zachowaj cały nagłówek po usunięciu skrajnych białych znaków.
5. Połącz wiersze sekwencji. Sekwencja musi być niepusta i zawierać wyłącznie 20 standardowych jednoliterowych kodów aminokwasów:

   ```text
   ACDEFGHIKLMNPQRSTVWY
   ```

   Dopuszczaj także małe litery. Sprawdź alfabet **całej sekwencji przez regex**, uwzględniając obie wielkości liter, a następnie przekształć poprawną sekwencję na wielkie litery. Przy `IGNORECASE` zastosuj również `ASCII`.

6. Nie dopuszczaj m.in. `X`, `B`, `Z`, `J`, `O`, `U`, `*`, `-`, cyfr ani spacji wewnątrz wiersza sekwencji. Nie usuwaj takich znaków w celu „naprawienia” rekordu.
7. Identyfikatory zaakceptowanych rekordów muszą być unikalne. Odrzuć późniejszy poprawnie zbudowany rekord o już zaakceptowanym identyfikatorze. Identyfikator z odrzuconego rekordu nie blokuje jego późniejszego poprawnego użycia.
8. Dla błędnego rekordu zapisz jeden błąd według kolejności kontroli: `naglowek`, `pusta_sekwencja`, `alfabet`, `duplikat`. Następnie przejdź do kolejnego rekordu. Po niepoprawnym nagłówku pomiń jego sekwencję do następnego wiersza `>`.
9. Licznik rekordów obejmuje także rekordy niepoprawne. Zapamiętaj fizyczny numer wiersza nagłówka, z uwzględnieniem pustych wierszy. Odrzuconych rekordów nie uwzględniaj w wyszukiwaniu ani statystykach sekwencji.
10. Niepusty wiersz przed pierwszym nagłówkiem oznacza błąd struktury całego pliku. Zakończ wtedy analizę z czytelnym komunikatem.

### C. Trzy obowiązkowe motywy

Samodzielnie zapisz regex dla każdego z poniższych motywów dydaktycznych. „Dowolny aminokwas” oznacza dowolny znak z wcześniej sprawdzonego alfabetu białkowego.

| Motyw | Reguła |
|---|---|
| `M1` | Dokładnie 4 aminokwasy: `N`, potem aminokwas inny niż `P`, następnie `S` albo `T`, a na końcu aminokwas inny niż `P` |
| `M2` | `C`, następnie od 2 do 4 dowolnych aminokwasów, a na końcu `C` |
| `M3` | `K` albo `R`, następnie dokładnie 2 dowolne aminokwasy, potem `D` albo `E`, a na końcu **ten sam aminokwas, który rozpoczynał motyw** |

Wymagania dotyczące implementacji:

- Każdy wzorzec ma przechwytywać całe trafienie w grupie nazwanej `motyw`.
- W `M2` przechwyć fragment między skrajnymi `C` w grupie `odstep`.
- W `M3` przechwyć pierwszy aminokwas w grupie `kotwica` i zastosuj **nazwane odwołanie wsteczne** do sprawdzenia ostatniego aminokwasu.
- Motywy analizuj oddzielnymi wzorcami, aby nazwy grup nie kolidowały między motywami.
- Szukaj także trafień **nakładających się**, korzystając z dodatniego lookahead oraz `finditer()`.
- W `M2`, jeśli od tej samej pozycji pasuje kilka długości, zgłoś **wyłącznie najdłuższe** dopuszczalne trafienie. Uwzględnij również trafienia zaczynające się od kolejnych pozycji.
- Analizuj całą połączoną sekwencję, również przez granice wierszy FASTA. Nie stosuj granic słów `\b` do wyszukiwania motywu wewnątrz białka.

| Motyw | Przykłady pasujące w całości | Przykłady niepasujące w całości |
|---|---|---|
| `M1` | `NNST`, `NQST`, `NATA` | `NPSA`, `NATP` |
| `M2` | `CAAC`, `CAAAC`, `CAAAAC` | `CAC`, `CAAAAAC` |
| `M3` | `KAAEK`, `RSTDR` | `KAAER`, `RAADK` |

### D. Dodatkowy motyw użytkownika `M4`

Użytkownik wybiera jeden z trzech trybów: `brak`, `doslowny` lub `regex`. Pusta odpowiedź oznacza `brak`. Dla nieznanego trybu ponów pytanie.

| Tryb | Zachowanie |
|---|---|
| `brak` | Analizuj tylko `M1`, `M2` i `M3` |
| `doslowny` | Pobierz niepusty fragment tekstu i potraktuj wszystkie jego znaki dosłownie, korzystając z `re.escape()` |
| `regex` | Pobierz niepusty wzorzec i potraktuj go jako wyrażenie regularne |

Dla `M4`:

1. Uwzględniaj obie wielkości liter przy użyciu `re.IGNORECASE | re.ASCII`.
2. Użytkownik podaje sam motyw, bez zewnętrznego lookahead i bez grupy obejmującej całe trafienie. Program dodaje te elementy, aby dla `M4` także była dostępna grupa `motyw` i nakładające się trafienia.
3. Nazwa grupy `motyw` jest zarezerwowana przez program. W trybie `regex` odrzuć wzorzec, jeżeli już deklaruje taką grupę. W trybie `doslowny` cały podany tekst pozostaje tekstem dosłownym.
4. Własny regex może zawierać grupy nieprzechwytujące i nazwane oraz nazwane odwołania wsteczne. Dla tego zadania przyjmij, że użytkownik nie stosuje numerowanych odwołań wstecznych ani globalnych flag wewnątrz wzorca. Dodanie zewnętrznej grupy zmieniałoby numery grup, a globalna flaga nie może znajdować się w dowolnym miejscu wzorca. Nie musisz tworzyć osobnego walidatora tych dwóch ograniczeń.
5. Skompiluj przygotowany wzorzec i obsłuż `re.error`. Po błędzie wyświetl komunikat i pozwól ponownie wybrać tryb oraz treść `M4`.
6. Motyw musi dopasowywać co najmniej jeden aminokwas. Odrzuć regex pasujący do pustego napisu. Dodatkowo sprawdzaj długość grupy `motyw` podczas wyszukiwania: wzorzec taki jak `(?=A)` może zwrócić pusty fragment dopiero w otoczeniu konkretnej sekwencji. Jeżeli takie trafienie wystąpi w którymkolwiek zaakceptowanym białku, odrzuć konfigurację `M4`, ponów pytanie i przelicz analizę z poprawną konfiguracją.
7. Brak trafień poprawnego, niepustego wzorca jest zwykłym wynikiem analizy, a nie błędem. Wybrane przez silnik jedno dopasowanie od danej pozycji traktuj jako jedno trafienie; nie wyliczaj wszystkich możliwych wariantów alternatyw i długości.

Przykłady do sprawdzenia:

- `AA` w trybie `doslowny` i `A{2}` w trybie `regex` powinny dawać te same trafienia.
- `A.A` w trybie `doslowny` nie daje trafień w poprawnych sekwencjach z dołączonego pliku, ponieważ nie zawierają one dosłownych kropek. W trybie `regex` kropka ma znaczenie znaku dowolnego.
- `[` w trybie `regex` ma spowodować komunikat o błędnej składni i ponowienie pytania.
- `A*` oraz `(?=A)` w trybie `regex` mają zostać odrzucone jako dopasowujące puste fragmenty.

Gdy użytkownik wybierze `brak`, w raportach liczba trafień `M4` ma wynosić `0`. Nie twórz dla niego zastępczych trafień.

### E. Raport trafień i kontekst aminokwasowy

Zapisz `wyniki_06/motywy.tsv` z kolumnami:

```text
id    typ    start    koniec    fragment    dlugosc_odstepu    kotwica    lewy_kontekst    prawy_kontekst
```

Powyżej pokazano nazwy kolumn; w pliku rozdziel je tabulatorami.

- `typ` to `M1`, `M2`, `M3` albo `M4`.
- Pozycje `start` i `koniec` numeruj od `1`, z obiema pozycjami włącznie.
- Granice obliczaj na podstawie `span("motyw")`, a nie pustego przedziału z `span(0)` lookahead.
- `fragment` to tekst grupy `motyw` w oryginalnej sekwencji po zamianie liter na wielkie.
- `dlugosc_odstepu` podaj tylko dla `M2`, a `kotwica` tylko dla `M3`. W pozostałych przypadkach wpisz `-`, także dla `M4` niezależnie od jego wewnętrznych grup.
- `lewy_kontekst` zawiera maksymalnie `k` aminokwasów bezpośrednio przed trafieniem; `prawy_kontekst` maksymalnie `k` aminokwasów po trafieniu. Sam motyw nie należy do jego kontekstu. Nie uzupełniaj kontekstu poza granicami sekwencji.
- Przy pustym kontekście, także dla `k = 0`, wpisz `-`.
- Zachowaj kolejność zaakceptowanych sekwencji z pliku. W obrębie sekwencji sortuj po `start`, następnie po `typ` w kolejności `M1`, `M2`, `M3`, `M4`, a następnie po `koniec`.
- To samo miejsce dopasowane przez dwa różne typy motywów stanowi dwa trafienia. Dopasowania nakładające się także licz oddzielnie.

### F. Maskowanie i pokrycie sekwencji

Zapisz `wyniki_06/maskowane.fasta`, obejmujący **wszystkie zaakceptowane rekordy**, także bez trafień. Zachowaj ich kolejność oraz nagłówki. Każdą wynikową sekwencję zapisz w jednym wierszu.

Zastąp `X` każdą pozycję należącą do **co najmniej jednego** trafienia dowolnego aktywnego motywu. Długość sekwencji ma pozostać bez zmian. Sekwencje bez trafień zapisz wielkimi literami bez maskowania.

Najpierw znajdź wszystkie trafienia w niezamaskowanej sekwencji. Następnie wyznacz sumę ich przedziałów i wykonaj maskowanie. Pomocny może być zbiór indeksów albo lista wartości logicznych.

**Liczba trafień i liczba objętych nimi pozycji to różne wielkości.** Jeśli dwa motywy się nakładają, wspólne aminokwasy należą do pokrycia tylko raz. Oblicz:

```text
pokrycie_proc = 100 * liczba_zamaskowanych_pozycji / dlugosc_sekwencji
```

Nie wyznaczaj pokrycia przez dodawanie długości trafień.

### G. Podsumowanie białek i wybór sekwencji

Zapisz `wyniki_06/podsumowanie.tsv` z kolumnami:

```text
id    dlugosc    M1    M2    M3    M4    razem    typy_motywow    zamaskowane    pokrycie_proc    wybrana
```

- Uwzględnij każde zaakceptowane białko, także z zerową liczbą trafień.
- `M1`–`M4` oznaczają liczby trafień, `razem` ich sumę, a `typy_motywow` liczbę typów mających co najmniej jedno trafienie.
- `zamaskowane` to liczba różnych pozycji objętych trafieniami.
- `pokrycie_proc` zapisuj z dwoma miejscami po kropce. Do sortowania używaj wartości przed zaokrągleniem.
- `wybrana` ma wartość `tak`, jeśli liczba trafień `razem` jest co najmniej równa `n`, lub `nie` w przeciwnym przypadku.
- Wiersze podsumowania posortuj malejąco według pokrycia, następnie malejąco według liczby trafień, a na końcu rosnąco według identyfikatora.

Zapisz także `wyniki_06/wybrane.fasta`: tylko białka spełniające próg `n`, z **niezamaskowanymi** sekwencjami zapisanymi wielkimi literami, w kolejności z pliku wejściowego. Zachowaj ich nagłówki. Dla `n = 0` wybierane są wszystkie zaakceptowane białka.

Próg wyboru wpływa wyłącznie na `wybrane.fasta` i kolumnę `wybrana`. Wszystkie zaakceptowane białka nadal podlegają wyszukiwaniu, maskowaniu i statystykom.

### H. Błędy, statystyki ogólne i puste wyniki

Zapisz `wyniki_06/bledy_fasta.tsv` z kolumnami `nr_rekordu`, `nr_wiersza`, `id`, `etap`, `powod`. Przy niepoprawnym nagłówku w kolumnie `id` wpisz `-`. Błędy zapisuj w kolejności rekordów wejściowych.

Na ekranie wypisz:

- liczbę rekordów wszystkich, zaakceptowanych i odrzuconych;
- dla każdego typu `M1`–`M4` łączną liczbę trafień i liczbę białek z co najmniej jednym trafieniem tego typu;
- łączną liczbę trafień i łączną liczbę różnych objętych nimi pozycji, sumowaną osobno po białkach;
- łączne pokrycie zbioru: `100 * suma_zamaskowanych / suma_dlugosci`, z dwoma miejscami po kropce;
- liczbę białek wybranych do `wybrane.fasta`;
- czas wyszukiwania i obliczania statystyk zmierzony przez `time.perf_counter()`, bez czasu oczekiwania na odpowiedzi użytkownika.

Łączne pokrycie nie jest zwykłą średnią procentów pokrycia poszczególnych białek.

Jeżeli plik nie zawiera rekordów albo wszystkie zostaną odrzucone, TSV nadal mają zawierać nagłówki, oba wynikowe pliki FASTA mają być puste, a podsumowanie ma wyjaśniać brak zaakceptowanych sekwencji. Przyjmij wtedy łączne pokrycie `0.00`, bez dzielenia przez zero.

### I. Dane wejściowe: `dane/sekwencje.fasta`

W paczce do ćwiczenia znajduje się gotowy plik. Poniżej podano jego treść. Zachowaj podział pierwszej sekwencji na dwa wiersze oraz pusty wiersz po nagłówku `SEQ007`. Cztery rekordy są celowo niepoprawne.

```text
>SEQ001 dwa nakladajace sie trafienia M1
MNNSTA
CAAACGKAAEK
>SEQ002 motywy M2 i M3
CCAACACRSTDR
>SEQ003 przypadki graniczne M1
NPSANATPNATAC
>SEQ004 brak motywow
MNPQ
>SEQ005 male litery
nqstcggckaaer
>SEQ006 niedozwolony znak
MASTXK
>SEQ002 powtorzony identyfikator
ACDEFG
>SEQ007 pusta sekwencja

>BAD008 niepoprawny identyfikator
MASTK
>SEQ008 ostatni poprawny rekord
ACDEFGHIK
```

### J. Wyniki kontrolne

#### J.1. Analiza bez dodatkowego motywu

Przyjmij `M4 = brak`, `k = 2` i `n = 3`. Dla dołączonego pliku oczekiwane są **10 rekordów: 6 zaakceptowanych i 4 odrzucone**. Zaakceptowane sekwencje mają razem **68 aminokwasów**.

Wiersze `podsumowanie.tsv`, w wymaganej kolejności:

| `id` | `dlugosc` | `M1` | `M2` | `M3` | `M4` | `razem` | `typy_motywow` | `zamaskowane` | `pokrycie_proc` | `wybrana` |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `SEQ002` | 12 | 0 | 2 | 1 | 0 | 3 | 2 | 12 | 100.00 | tak |
| `SEQ001` | 17 | 2 | 1 | 1 | 0 | 4 | 3 | 15 | 88.24 | tak |
| `SEQ005` | 13 | 1 | 1 | 0 | 0 | 2 | 2 | 8 | 61.54 | nie |
| `SEQ003` | 13 | 1 | 0 | 0 | 0 | 1 | 1 | 4 | 30.77 | nie |
| `SEQ004` | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.00 | nie |
| `SEQ008` | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.00 | nie |

Trafienia i ich kontekst:

| `id` | `typ` | `start` | `koniec` | `fragment` | `dlugosc_odstepu` | `kotwica` | `lewy_kontekst` | `prawy_kontekst` |
|---|---|---:|---:|---|---:|---|---|---|
| `SEQ001` | `M1` | 2 | 5 | `NNST` | - | - | `M` | `AC` |
| `SEQ001` | `M1` | 3 | 6 | `NSTA` | - | - | `MN` | `CA` |
| `SEQ001` | `M2` | 7 | 11 | `CAAAC` | 3 | - | `TA` | `GK` |
| `SEQ001` | `M3` | 13 | 17 | `KAAEK` | - | K | `CG` | - |
| `SEQ002` | `M2` | 1 | 5 | `CCAAC` | 3 | - | - | `AC` |
| `SEQ002` | `M2` | 2 | 7 | `CAACAC` | 4 | - | `C` | `RS` |
| `SEQ002` | `M3` | 8 | 12 | `RSTDR` | - | R | `AC` | - |
| `SEQ003` | `M1` | 9 | 12 | `NATA` | - | - | `TP` | `C` |
| `SEQ005` | `M1` | 1 | 4 | `NQST` | - | - | - | `CG` |
| `SEQ005` | `M2` | 5 | 8 | `CGGC` | 2 | - | `ST` | `KA` |

Statystyki ogólne:

| Typ | Liczba trafień | Białka z co najmniej jednym trafieniem |
|---|---:|---:|
| `M1` | 4 | 3 |
| `M2` | 4 | 3 |
| `M3` | 2 | 2 |
| `M4` | 0 | 0 |

Łącznie: **10 trafień**, **39 zamaskowanych pozycji**, **57.35% pokrycia**. Przy progu `n = 3` w `wybrane.fasta` mają znaleźć się kolejno **`SEQ001` i `SEQ002`**.

Pełne sekwencje wynikowe w `maskowane.fasta`:

```text
>SEQ001 dwa nakladajace sie trafienia M1
MXXXXXXXXXXGXXXXX
>SEQ002 motywy M2 i M3
XXXXXXXXXXXX
>SEQ003 przypadki graniczne M1
NPSANATPXXXXC
>SEQ004 brak motywow
MNPQ
>SEQ005 male litery
XXXXXXXXKAAER
>SEQ008 ostatni poprawny rekord
ACDEFGHIK
```

Raport błędów powinien zawierać poniższe rekordy. Treść kolumny `powod` może być własna, ale powinna wyjaśniać problem.

| `nr_rekordu` | `nr_wiersza` | `id` | `etap` |
|---:|---:|---|---|
| 6 | 12 | `SEQ006` | `alfabet` |
| 7 | 14 | `SEQ002` | `duplikat` |
| 8 | 16 | `SEQ007` | `pusta_sekwencja` |
| 9 | 18 | `-` | `naglowek` |

#### J.2. Analiza z dodatkowym motywem

Włącz `M4` jako dosłowne `AA` albo regex `A{2}`. Pozostaw `k = 2` i `n = 3`.

| Sekwencja | Dodatkowe trafienia `M4`, pozycje od 1 | Liczba trafień wszystkich typów | Zamaskowane pozycje |
|---|---|---:|---:|
| `SEQ001` | 8–9, 9–10, 14–15 | 7 | 15 |
| `SEQ002` | 3–4 | 4 | 12 |
| `SEQ003` | brak | 1 | 4 |
| `SEQ004` | brak | 0 | 0 |
| `SEQ005` | 10–11 | 3 | 10 |
| `SEQ008` | brak | 0 | 0 |

`M4` daje **5 trafień w 3 białkach**. Cała analiza ma **15 trafień**, **41 zamaskowanych pozycji** i **60.29% łącznego pokrycia**. Wybrane białka to kolejno **`SEQ001`, `SEQ002`, `SEQ005`**.

Maskowanie `SEQ005` ma wtedy dać `XXXXXXXXKXXER`, a jej pokrycie ma wynosić `76.92`. Pozostałe zamaskowane sekwencje nie zmieniają się.



### Punktacja

| Kryterium | Punkty |
|---|---:|
| Odczyt FASTA, grupy nagłówka, sprawdzenie alfabetu i obsługa błędnych rekordów | 0,75 |
| Poprawne wzorce `M1`–`M3`, wymagane grupy, nazwane odwołanie wsteczne i nakładające się trafienia | 1,25 |
| Obsługa `M4`: tryb dosłowny, `re.escape()`, własny regex i odrzucanie błędnych lub pustych dopasowań | 0,75 |
| Współrzędne trafień i kontekst aminokwasowy | 0,50 |
| Maskowanie sumy przedziałów, pokrycie i statystyki białek | 0,75 |
| Kompletne raporty, kolejność wyników, wybór białek i podsumowanie ogólne | 0,50 |
| Podział na funkcje, obsługa plików, opis własnych prób i odpowiedzi | 0,50 |
| **Razem** | **5,00** |

## 20. Podsumowanie i dokumentacja

### Najważniejsze funkcje

| Potrzeba | Narzędzie |
|---|---|
| Znalezienie pierwszego fragmentu | `search()` |
| Sprawdzenie dopasowania od początku | `match()` |
| Sprawdzenie całej wartości | `fullmatch()` |
| Lista dopasowanych napisów lub grup | `findall()` |
| Kolejne dopasowania z pozycjami i grupami | `finditer()` |
| Podział według wzorca separatora | `split()` |
| Zamiana według wzorca | `sub()` |
| Zamiana i liczba wykonanych zamian | `subn()` |
| Przygotowanie wielokrotnie używanego wzorca | `compile()` |
| Potraktowanie zmiennego tekstu dosłownie we wzorcu | `escape()` |

### Dokumentacja

Dokumentacja Pythona 3.13 opisuje wszystkie konstrukcje wykorzystane w tej instrukcji, w tym dodatki oznaczone jako Python 3.11+:

- [Moduł `re`: składnia, funkcje, obiekty `Pattern` i `Match`](https://docs.python.org/3.13/library/re.html)
- [Regular Expression HOWTO: wprowadzenie i przykłady](https://docs.python.org/3.13/howto/regex.html)
- [Moduł `datetime`](https://docs.python.org/3.13/library/datetime.html)
- [Moduł `os`](https://docs.python.org/3.13/library/os.html)
- [Funkcja `math.isfinite()`](https://docs.python.org/3.13/library/math.html#math.isfinite)

