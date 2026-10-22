# Ćwiczenie 03 — Zadanie 2 — Analiza białka z pliku FASTA
#
# Rozbuduj analizę sekwencji z poprzednich ćwiczeń: tym razem dane mają pochodzić z pliku
# FASTA, a wynik ma zostać zapisany w tabeli. Wykorzystaj plik `dane/1E7A.fasta` ze starych
# materiałów — zawiera sekwencję albuminy ludzkiej.
#
# Pierwszy niepusty wiersz pliku FASTA jest nagłówkiem zaczynającym się od `>`. Kolejne
# wiersze zawierają fragmenty tej samej sekwencji:
#
# >bialko_kontrolne
# AKAK
# GWY
#
# Sekwencja z tego przykładu to `AKAKGWY`. Nagłówek nie jest jej częścią. Załóż, że plik
# zawiera dokładnie jeden rekord z niepustą sekwencją białkową. W sekwencji występują
# wyłącznie jednoliterowe oznaczenia 20 standardowych aminokwasów; dopuszczalne są wielkie i
# małe litery:
#
# aminokwasy = "ACDEFGHIKLMNPQRSTVWY"
#
# **Wymagania:**
#
# 1. Pobierz od użytkownika ścieżkę do pliku FASTA.
# 2. Zdefiniuj funkcję `wczytaj_fasta(nazwa_pliku)`, która zwraca nagłówek bez znaku `>`
# oraz połączoną sekwencję zapisaną wielkimi literami. Pomijaj puste wiersze i usuwaj
# skrajne białe znaki z każdego wiersza.
# 3. Zdefiniuj funkcję `sklad_aminokwasowy(sekwencja)`, która zwraca słownik z liczbą
# wystąpień każdego z 20 aminokwasów, również tych nieobecnych w sekwencji. Zliczanie
# wykonaj za pomocą pętli.
# 4. Wyświetl nagłówek, długość sekwencji oraz najczęściej występujący aminokwas i liczbę
# jego wystąpień. Przy remisie pokaż wszystkie takie aminokwasy w kolejności alfabetycznej.
# 5. Zapisz plik `sklad_bialka.tsv` w trybie `w`, z nagłówkiem `aminokwas`, `liczba`,
# `procent` i 20 wierszami danych w kolejności alfabetycznej. Kolumny rozdziel tabulatorami;
# udziały procentowe podaj z dwoma miejscami po przecinku.
#
# **Sprawdź:** plik `dane/kontrola.fasta` zawiera sekwencję z przykładu. Jej długość to `7`,
# a najczęstsze aminokwasy to `A` i `K` — po `2` wystąpienia, czyli po około `28.57%`. Suma
# zliczeń musi być równa długości sekwencji. Zaokrąglone procenty nie muszą sumować się
# dokładnie do `100.00`.

# Rozwiązanie:

