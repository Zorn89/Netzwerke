# Aufgabe:

## Beschreibe in eigenen Worten:
***- Was passiert, wenn die Route / aufgerufen wird?*** 

Wenn die Route / aufgerufen wird, gibt die Flask-App den Text „Willkommen bei meiner Flask-App!“ zurück. Dies ist die Standard-Startseite der App.

***- Was geben die Routen /info, /team, /hilfe und /kontakt zurück?*** 
- Route /info: Gibt den Text „Dies ist eine einfache API mit Flask.“ zurück.
- Route /team: Gibt den Text „Unser Team besteht aus IT-Experten und Entwicklern.“ zurück. 
- Route /hilfe: Gibt den Text „Hier findest du Unterstützung zu unserer API.“ zurück. 
- Route /kontakt: Gibt den Text „Schreibe uns eine E-Mail an kontakt@example.com.“ zurück. 

***- Warum wird app.run(port=6060) verwendet?*** 

Die Methode app.run(port=6060) startet den Flask-Webserver und macht die App im Browser verfügbar. Die App wird auf dem lokalen Rechner unter dem Port 6060 ausgeführt, sodass die App über http://127.0.0.1:6060/ im eigenen Browser aufgerufen werden kann. Der Port 6060 ist spezifisch festgelegt, damit der Server auf einem von anderen möglichen Anwendungen nicht genutzten Port läuft.

## Starte die App auf deinem Rechner, rufe die Routen im Browser auf und überprüfe die Ausgaben.

Korrekt.

## Überlege, welche weiteren Inhalte du einer API hinzufügen könntest. 

Googelrecherche: Datenbank, Supporttickets 