[readme.md](https://github.com/user-attachments/files/26633840/readme.md)
# Platformy programistyczne .NET i Java
# Sprawozdanie 1 - Wiktor Hebdowski

## Wstęp

Repozytorium zawiera projekt aplikacji bazodanowej .NET pobierającej dane pogodowe z ogólnodostępnego API i umieszczającej je w dedykowanej bazie danych. 
## Klasy

### APITest

Głównym jej elementem jest funkcja GetGeoData zwracająca dane lokalizacyjne, konieczne do pozyskania danych pogodowych danego miasta. Jednocześnie, w przypadku wykrycia nowych danych, dodawane są do bazy danych, zdefiniowanej w innych klasach

![Dodawanie do bazy danych](https://i.imgur.com/649YLvu.png)

### Klasy danych pogodowych
Dane pogodowe i lokalizacyjne są przechowywane w czterech klasach:
#### LocationData
Nazwa miasta i jego współrzędne
#### Weather Data
Obiekt składający się z parametrów pogodowych i opisu pogody (zachmurzenia)
#### Main
Parametry pogodowe
#### WeatherDesc
Opis pogody

### Klasy bazy danych
#### City
Przechowuje informacje o mieście dla bazy danych
#### WeatherHistory
Przechowuje historyczne dane pogodowe dla bazy danych
#### WeatherContext
Tworzy dwie tablice bazy danych w ramach powyższych klas
## Sortowanie bazy danych
Zaimplementowano funkcję ShowDatabaseFeatures(), która zajmuje się filtrowaniem oraz sortowaniem wyników bazy na trzy przypadki: sortowanie od najwyższej temperatury, wyświetlanie wyłączenie rekordów temperatury powyżej 10 stopni, wyświetlanie danych dla konkretnego miasta.

![Funkcja](https://i.imgur.com/FR8cP35.png)

## Drzewo projektu

![Zdjęcie drzewa](https://i.imgur.com/ASTuMEt.png)
