# Ćwiczenie 06 — Zadanie 1 — Analizator motywów białkowych — 5 pkt
#
# Napisz program, który odczytuje plik wielosekwencyjny FASTA, sprawdza poprawność rekordów i
#   wyszukuje motywy białkowe za pomocą wyrażeń regularnych. Program ma odnajdywać również
#   trafienia nakładające się, raportować ich pozycje i otoczenie, obliczać pokrycie
#   sekwencji oraz zapisywać wybrane i zamaskowane białka.
#
# Pracujesz nad jednym programem zadanie_01.py. Poszczególne części poniżej są etapami tego
#   samego zadania, za które łącznie można uzyskać 5 pkt.
#
# A. Organizacja programu i dane wejściowe
#
# - Korzystaj z biblioteki standardowej. Głównym narzędziem analizy tekstu ma być re.
# - Program uruchamiaj poleceniem python3 zadanie_01.py, mając katalog 06/ jako bieżący
#   katalog roboczy.
# - Przez input() pobierz ścieżkę do pliku FASTA. Dla dołączonych danych jest to
#   dane/sekwencje.fasta.
# - Pobierz także długość kontekstu k oraz minimalną liczbę trafień n, według której będą
#   wybierane białka. Obie wartości muszą być liczbami całkowitymi nieujemnymi. Puste
#   odpowiedzi oznaczają odpowiednio k = 2 i n = 3. Przy błędnej wartości ponów pytanie.
# - Umożliw określenie dodatkowego motywu M4 według zasad z części D. Obsługa tej możliwości
#   jest wymagana; użytkownik może jednak wybrać analizę bez M4.
# - Pliki wejściowe pozostaw bez zmian. Wyniki zapisuj w katalogu wyniki_06/, tworzonym przez
#   os.makedirs(..., exist_ok=True).
# - Pliki tekstowe odczytuj i zapisuj jako UTF-8. W TSV separatorem jest pojedynczy tabulator
#   \t, a pierwszy wiersz zawiera nazwy kolumn.
# - Wydziel funkcje odpowiadające etapom pracy, np. odczytowi FASTA, przygotowaniu wzorców,
#   wyszukiwaniu trafień, maskowaniu i zapisowi raportów. Uruchomienie programu umieść pod if
#   __name__ == "__main__":.
# - Obsłuż błędy plikowe, np. FileNotFoundError, PermissionError lub inne OSError. Wyświetl
#   komunikat wyjaśniający problem.
#
# B. Odczyt i sprawdzenie FASTA
#
# 1. Przed analizą pojedynczego wiersza zastosuj strip(). Puste wiersze pomijaj.
# 2. Nowy rekord rozpoczyna każdy wiersz zaczynający się od >. Rekord trwa do następnego
#   takiego wiersza albo do końca pliku. Pamiętaj o przetworzeniu ostatniego rekordu, również
#   gdy plik nie kończy się znakiem nowej linii.
# 3. Nagłówek ma postać >SEQddd albo >SEQddd opis, gdzie ddd oznacza dokładnie trzy cyfry
#   ASCII. Opis, jeżeli występuje, jest oddzielony od identyfikatora co najmniej jedną spacją
#   lub tabulatorem i jest niepusty.
# 4. Sprawdź cały nagłówek przez fullmatch(). Użyj grup nazwanych id i opis; opis może być
#   grupą opcjonalną. Do zapisu FASTA zachowaj cały nagłówek po usunięciu skrajnych białych
#   znaków.
# 5. Połącz wiersze sekwencji. Sekwencja musi być niepusta i zawierać wyłącznie 20
#   standardowych jednoliterowych kodów aminokwasów:
#
# ACDEFGHIKLMNPQRSTVWY
#
# Dopuszczaj także małe litery. Sprawdź alfabet całej sekwencji przez regex, uwzględniając
#   obie wielkości liter, a następnie przekształć poprawną sekwencję na wielkie litery. Przy
#   IGNORECASE zastosuj również ASCII.
# 6. Nie dopuszczaj m.in. X, B, Z, J, O, U, *, -, cyfr ani spacji wewnątrz wiersza sekwencji.
#   Nie usuwaj takich znaków w celu „naprawienia” rekordu.
# 7. Identyfikatory zaakceptowanych rekordów muszą być unikalne. Odrzuć późniejszy poprawnie
#   zbudowany rekord o już zaakceptowanym identyfikatorze. Identyfikator z odrzuconego
#   rekordu nie blokuje jego późniejszego poprawnego użycia.
# 8. Dla błędnego rekordu zapisz jeden błąd według kolejności kontroli: naglowek,
#   pusta_sekwencja, alfabet, duplikat. Następnie przejdź do kolejnego rekordu. Po
#   niepoprawnym nagłówku pomiń jego sekwencję do następnego wiersza >.
# 9. Licznik rekordów obejmuje także rekordy niepoprawne. Zapamiętaj fizyczny numer wiersza
#   nagłówka, z uwzględnieniem pustych wierszy. Odrzuconych rekordów nie uwzględniaj w
#   wyszukiwaniu ani statystykach sekwencji.
# 10. Niepusty wiersz przed pierwszym nagłówkiem oznacza błąd struktury całego pliku. Zakończ
#   wtedy analizę z czytelnym komunikatem.
#
# C. Trzy obowiązkowe motywy
#
# Samodzielnie zapisz regex dla każdego z poniższych motywów dydaktycznych. „Dowolny
#   aminokwas” oznacza dowolny znak z wcześniej sprawdzonego alfabetu białkowego.
#
# Motyw - Reguła
# M1 - Dokładnie 4 aminokwasy: N, potem aminokwas inny niż P, następnie S albo T, a na końcu
#   aminokwas inny niż P
# M2 - C, następnie od 2 do 4 dowolnych aminokwasów, a na końcu C
# M3 - K albo R, następnie dokładnie 2 dowolne aminokwasy, potem D albo E, a na końcu ten sam
#   aminokwas, który rozpoczynał motyw
#
# Wymagania dotyczące implementacji:
#
# - Każdy wzorzec ma przechwytywać całe trafienie w grupie nazwanej motyw.
# - W M2 przechwyć fragment między skrajnymi C w grupie odstep.
# - W M3 przechwyć pierwszy aminokwas w grupie kotwica i zastosuj nazwane odwołanie wsteczne
#   do sprawdzenia ostatniego aminokwasu.
# - Motywy analizuj oddzielnymi wzorcami, aby nazwy grup nie kolidowały między motywami.
# - Szukaj także trafień nakładających się, korzystając z dodatniego lookahead oraz
#   finditer().
# - W M2, jeśli od tej samej pozycji pasuje kilka długości, zgłoś wyłącznie najdłuższe
#   dopuszczalne trafienie. Uwzględnij również trafienia zaczynające się od kolejnych
#   pozycji.
# - Analizuj całą połączoną sekwencję, również przez granice wierszy FASTA. Nie stosuj granic
#   słów \b do wyszukiwania motywu wewnątrz białka.
#
# Motyw - Przykłady pasujące w całości - Przykłady niepasujące w całości
# M1 - NNST, NQST, NATA - NPSA, NATP
# M2 - CAAC, CAAAC, CAAAAC - CAC, CAAAAAC
# M3 - KAAEK, RSTDR - KAAER, RAADK
#
# D. Dodatkowy motyw użytkownika M4
#
# Użytkownik wybiera jeden z trzech trybów: brak, doslowny lub regex. Pusta odpowiedź oznacza
#   brak. Dla nieznanego trybu ponów pytanie.
#
# Tryb - Zachowanie
# brak - Analizuj tylko M1, M2 i M3
# doslowny - Pobierz niepusty fragment tekstu i potraktuj wszystkie jego znaki dosłownie,
#   korzystając z re.escape()
# regex - Pobierz niepusty wzorzec i potraktuj go jako wyrażenie regularne
#
# Dla M4:
#
# 1. Uwzględniaj obie wielkości liter przy użyciu re.IGNORECASE | re.ASCII.
# 2. Użytkownik podaje sam motyw, bez zewnętrznego lookahead i bez grupy obejmującej całe
#   trafienie. Program dodaje te elementy, aby dla M4 także była dostępna grupa motyw i
#   nakładające się trafienia.
# 3. Nazwa grupy motyw jest zarezerwowana przez program. W trybie regex odrzuć wzorzec,
#   jeżeli już deklaruje taką grupę. W trybie doslowny cały podany tekst pozostaje tekstem
#   dosłownym.
# 4. Własny regex może zawierać grupy nieprzechwytujące i nazwane oraz nazwane odwołania
#   wsteczne. Dla tego zadania przyjmij, że użytkownik nie stosuje numerowanych odwołań
#   wstecznych ani globalnych flag wewnątrz wzorca. Dodanie zewnętrznej grupy zmieniałoby
#   numery grup, a globalna flaga nie może znajdować się w dowolnym miejscu wzorca. Nie
#   musisz tworzyć osobnego walidatora tych dwóch ograniczeń.
# 5. Skompiluj przygotowany wzorzec i obsłuż re.error. Po błędzie wyświetl komunikat i pozwól
#   ponownie wybrać tryb oraz treść M4.
# 6. Motyw musi dopasowywać co najmniej jeden aminokwas. Odrzuć regex pasujący do pustego
#   napisu. Dodatkowo sprawdzaj długość grupy motyw podczas wyszukiwania: wzorzec taki jak
#   (?=A) może zwrócić pusty fragment dopiero w otoczeniu konkretnej sekwencji. Jeżeli takie
#   trafienie wystąpi w którymkolwiek zaakceptowanym białku, odrzuć konfigurację M4, ponów
#   pytanie i przelicz analizę z poprawną konfiguracją.
# 7. Brak trafień poprawnego, niepustego wzorca jest zwykłym wynikiem analizy, a nie błędem.
#   Wybrane przez silnik jedno dopasowanie od danej pozycji traktuj jako jedno trafienie; nie
#   wyliczaj wszystkich możliwych wariantów alternatyw i długości.
#
# Przykłady do sprawdzenia:
#
# - AA w trybie doslowny i A{2} w trybie regex powinny dawać te same trafienia.
# - A.A w trybie doslowny nie daje trafień w poprawnych sekwencjach z dołączonego pliku,
#   ponieważ nie zawierają one dosłownych kropek. W trybie regex kropka ma znaczenie znaku
#   dowolnego.
# - [ w trybie regex ma spowodować komunikat o błędnej składni i ponowienie pytania.
# - A* oraz (?=A) w trybie regex mają zostać odrzucone jako dopasowujące puste fragmenty.
#
# Gdy użytkownik wybierze brak, w raportach liczba trafień M4 ma wynosić 0. Nie twórz dla
#   niego zastępczych trafień.
#
# E. Raport trafień i kontekst aminokwasowy
#
# Zapisz wyniki_06/motywy.tsv z kolumnami:
#
# id    typ    start    koniec    fragment    dlugosc_odstepu    kotwica    lewy_kontekst
#   prawy_kontekst
#
# Powyżej pokazano nazwy kolumn; w pliku rozdziel je tabulatorami.
#
# - typ to M1, M2, M3 albo M4.
# - Pozycje start i koniec numeruj od 1, z obiema pozycjami włącznie.
# - Granice obliczaj na podstawie span("motyw"), a nie pustego przedziału z span(0)
#   lookahead.
# - fragment to tekst grupy motyw w oryginalnej sekwencji po zamianie liter na wielkie.
# - dlugosc_odstepu podaj tylko dla M2, a kotwica tylko dla M3. W pozostałych przypadkach
#   wpisz -, także dla M4 niezależnie od jego wewnętrznych grup.
# - lewy_kontekst zawiera maksymalnie k aminokwasów bezpośrednio przed trafieniem;
#   prawy_kontekst maksymalnie k aminokwasów po trafieniu. Sam motyw nie należy do jego
#   kontekstu. Nie uzupełniaj kontekstu poza granicami sekwencji.
# - Przy pustym kontekście, także dla k = 0, wpisz -.
# - Zachowaj kolejność zaakceptowanych sekwencji z pliku. W obrębie sekwencji sortuj po
#   start, następnie po typ w kolejności M1, M2, M3, M4, a następnie po koniec.
# - To samo miejsce dopasowane przez dwa różne typy motywów stanowi dwa trafienia.
#   Dopasowania nakładające się także licz oddzielnie.
#
# F. Maskowanie i pokrycie sekwencji
#
# Zapisz wyniki_06/maskowane.fasta, obejmujący wszystkie zaakceptowane rekordy, także bez
#   trafień. Zachowaj ich kolejność oraz nagłówki. Każdą wynikową sekwencję zapisz w jednym
#   wierszu.
#
# Zastąp X każdą pozycję należącą do co najmniej jednego trafienia dowolnego aktywnego
#   motywu. Długość sekwencji ma pozostać bez zmian. Sekwencje bez trafień zapisz wielkimi
#   literami bez maskowania.
#
# Najpierw znajdź wszystkie trafienia w niezamaskowanej sekwencji. Następnie wyznacz sumę ich
#   przedziałów i wykonaj maskowanie. Pomocny może być zbiór indeksów albo lista wartości
#   logicznych.
#
# Liczba trafień i liczba objętych nimi pozycji to różne wielkości. Jeśli dwa motywy się
#   nakładają, wspólne aminokwasy należą do pokrycia tylko raz. Oblicz:
#
# pokrycie_proc = 100 * liczba_zamaskowanych_pozycji / dlugosc_sekwencji
#
# Nie wyznaczaj pokrycia przez dodawanie długości trafień.
#
# G. Podsumowanie białek i wybór sekwencji
#
# Zapisz wyniki_06/podsumowanie.tsv z kolumnami:
#
# id    dlugosc    M1    M2    M3    M4    razem    typy_motywow    zamaskowane
#   pokrycie_proc    wybrana
#
# - Uwzględnij każde zaakceptowane białko, także z zerową liczbą trafień.
# - M1–M4 oznaczają liczby trafień, razem ich sumę, a typy_motywow liczbę typów mających co
#   najmniej jedno trafienie.
# - zamaskowane to liczba różnych pozycji objętych trafieniami.
# - pokrycie_proc zapisuj z dwoma miejscami po kropce. Do sortowania używaj wartości przed
#   zaokrągleniem.
# - wybrana ma wartość tak, jeśli liczba trafień razem jest co najmniej równa n, lub nie w
#   przeciwnym przypadku.
# - Wiersze podsumowania posortuj malejąco według pokrycia, następnie malejąco według liczby
#   trafień, a na końcu rosnąco według identyfikatora.
#
# Zapisz także wyniki_06/wybrane.fasta: tylko białka spełniające próg n, z niezamaskowanymi
#   sekwencjami zapisanymi wielkimi literami, w kolejności z pliku wejściowego. Zachowaj ich
#   nagłówki. Dla n = 0 wybierane są wszystkie zaakceptowane białka.
#
# Próg wyboru wpływa wyłącznie na wybrane.fasta i kolumnę wybrana. Wszystkie zaakceptowane
#   białka nadal podlegają wyszukiwaniu, maskowaniu i statystykom.
#
# H. Błędy, statystyki ogólne i puste wyniki
#
# Zapisz wyniki_06/bledy_fasta.tsv z kolumnami nr_rekordu, nr_wiersza, id, etap, powod. Przy
#   niepoprawnym nagłówku w kolumnie id wpisz -. Błędy zapisuj w kolejności rekordów
#   wejściowych.
#
# Na ekranie wypisz:
#
# - liczbę rekordów wszystkich, zaakceptowanych i odrzuconych;
# - dla każdego typu M1–M4 łączną liczbę trafień i liczbę białek z co najmniej jednym
#   trafieniem tego typu;
# - łączną liczbę trafień i łączną liczbę różnych objętych nimi pozycji, sumowaną osobno po
#   białkach;
# - łączne pokrycie zbioru: 100 * suma_zamaskowanych / suma_dlugosci, z dwoma miejscami po
#   kropce;
# - liczbę białek wybranych do wybrane.fasta;
# - czas wyszukiwania i obliczania statystyk zmierzony przez time.perf_counter(), bez czasu
#   oczekiwania na odpowiedzi użytkownika.
#
# Łączne pokrycie nie jest zwykłą średnią procentów pokrycia poszczególnych białek.
#
# Jeżeli plik nie zawiera rekordów albo wszystkie zostaną odrzucone, TSV nadal mają zawierać
#   nagłówki, oba wynikowe pliki FASTA mają być puste, a podsumowanie ma wyjaśniać brak
#   zaakceptowanych sekwencji. Przyjmij wtedy łączne pokrycie 0.00, bez dzielenia przez zero.
#
# Dane wejściowe i kontrola wyników
#
# Pełne dane i tabele wyników znajdują się w README.md ćwiczenia.
# Plik wejściowy: dane/sekwencje.fasta.
# Konfiguracja podstawowa: M4 = brak, k = 2, n = 3.
# Oczekiwane: 10 rekordów, 6 zaakceptowanych i 4 odrzucone; 10 trafień,
# 39 zamaskowanych pozycji z 68 aminokwasów, pokrycie 57.35%.
# Wybrane białka: SEQ001 i SEQ002.
# Dla M4 = AA: 15 trafień, 41 zamaskowanych pozycji, pokrycie 60.29%,
# wybrane białka: SEQ001, SEQ002, SEQ005.

#  Punktacja
#
# Kryterium - Punkty
# Odczyt FASTA, grupy nagłówka, sprawdzenie alfabetu i obsługa błędnych rekordów - 0,75
# Poprawne wzorce M1–M3, wymagane grupy, nazwane odwołanie wsteczne i nakładające się
#   trafienia - 1,25
# Obsługa M4: tryb dosłowny, re.escape(), własny regex i odrzucanie błędnych lub pustych
#   dopasowań - 0,75
# Współrzędne trafień i kontekst aminokwasowy - 0,50
# Maskowanie sumy przedziałów, pokrycie i statystyki białek - 0,75
# Kompletne raporty, kolejność wyników, wybór białek i podsumowanie ogólne - 0,50
# Podział na funkcje, obsługa plików, opis własnych prób i odpowiedzi - 0,50
# Razem - 5,00
#

# Rozwiązanie:


