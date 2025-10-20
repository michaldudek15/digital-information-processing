Dane: plik oceny.csv zawierający informacje o 50 studentach w dwóch grupach (A i B).
Każdy przedmiot posiada ocenę z wykładu i z ćwiczeń. Oceny występują w skali 2–5 lub w formie „nzal”.

## Część 1 – Wczytanie i przygotowanie danych
* Wczytać dane z pliku CSV do struktury umożliwiającej analizę (np. lista słowników).
* Upewnić się, że puste wartości i „nzal” są poprawnie traktowane jako brak zaliczenia.
* Zamienić dane tekstowe ocen (2–5) na wartości liczbowe, pozostawiając „nzal” jako oznaczenie braku.

## Część 2 – Analizy indywidualne
* Obliczyć średnią ocen dla każdego studenta, pomijając „nzal”.
* Dodać informację o liczbie przedmiotów, które każdy student zaliczył.
* Utworzyć ranking studentów posortowany malejąco według średniej ocen.
* Wypisać listę studentów, którzy nie mają żadnego „nzal”.

## Część 3 – Analizy grupowe
* Obliczyć osobno średnią ocen dla grupy A i grupy B.
* Porównać, która grupa wypadła lepiej pod względem średniej.
* Zliczyć procent studentów z co najmniej jedną oceną „nzal” w każdej grupie.

## Część 4 – Analizy przedmiotowe
* Wyznaczyć średnią ocen dla każdego przedmiotu.
* Sprawdzić, który przedmiot jest najczęściej zaliczany na ocenę 5.
* Wskazać przedmiot z największą liczbą ocen „nzal”.

## Część 5 – Raport
* Zapisać wyniki analiz (średnie, rankingi, porównania grup) do nowych plików CSV.
* Przygotować czytelny raport w konsoli, prezentujący:
  * 5 najlepszych studentów,
  * średnie ocen dla każdej grupy,
  * najtrudniejszy i najłatwiejszy przedmiot.

## Pytania kontrolne
* Jakie błędy mogą wystąpić podczas wczytywania pliku CSV z danymi?
* W jaki sposób można rozpoznać, że dane w pliku są niekompletne lub uszkodzone?
* Jakie podejście jest lepsze przy błędzie w danych: zatrzymać program, czy pominąć błędny wiersz?
* Jakie informacje warto wyświetlić użytkownikowi, gdy program napotka problem z plikiem danych?
* Dlaczego przy przetwarzaniu danych tekstowych należy uwzględniać możliwość wystąpienia wartości pustych lub błędnych?
* Jak można bezpiecznie zamienić dane tekstowe (np. oceny zapisane jako tekst) na liczby?
* W jakich sytuacjach przydatne jest ignorowanie błędnych wartości zamiast przerywania programu?
* Do czego służy blok try i except w Pythonie?
* Jakie są potencjalne zagrożenia używania except: bez wskazania konkretnego typu błędu?
* W jakiej sytuacji warto dodać również blok finally?
* Dlaczego warto wyświetlać komunikat o błędzie, zamiast po prostu „przechwycić” wyjątek i nic nie robić?
* Jak można zapobiegać powtarzaniu tego samego błędu w wielu miejscach programu?
* Co oznacza sytuacja, w której obliczona średnia ocen wynosi None lub NaN?
* Jak sprawdzić, czy dane statystyczne (np. średnie ocen) są wiarygodne, jeśli część wartości była błędna lub brakowała?
* W jaki sposób można porównać jakość danych między dwiema grupami, jeśli jedna z nich ma więcej braków lub „niezaliczeń”?
* Dlaczego warto dodawać do programu komunikaty informujące o liczbie przetworzonych rekordów?
* Jakie zalety ma stosowanie obsługi wyjątków w dużych projektach, gdzie dane pochodzą z wielu różnych źródeł?
* W jaki sposób obsługa wyjątków wpływa na wiarygodność i stabilność aplikacji?
* Jakie błędy można wykryć dzięki testowaniu programu na niepoprawnych danych wejściowych?
* Dlaczego ważne jest oddzielenie logiki przetwarzania danych od obsługi błędów?
