# LogenPlatz
App für die praktische Untersuchung zur Bachelorarbeit mit dem Thema

> Analyse der Auswirkungen von empathischem Error Design auf die Recovery Time bei der Bewältigung von Interaktionsunterbrechungen

im Studiengang Wirtschaftsinformatik B.Sc.

an der Hochschule für Wirtschaft und Recht Berlin

im Somersemester 2026 / Wintersemester 2026

Eingereicht am ...

von Eliana Kaping (Matrikelnummer: 77211973055 , GitHub: el231204)


Erstgutachterin: Prof. Dr. Fatoumata Camara

Zweitgutachter: Prof. Dr. Markus Schaal


## Über dieses Projekt
 
**LogenPlatz** ist eine im Rahmen einer Bachelorarbeit an der Hochschule für Wirtschaft und Recht Berlin (Studiengang Wirtschaftsinformatik) entwickelte Applikation. Sie **simuliert eine Online-Ticketplattform** für Kulturveranstaltungen, ist jedoch **keine echte Shopping-Plattform**, sondern ein eigens für eine wissenschaftliche Nutzerstudie konstruiertes Studienobjekt.
 
### Ziel der Arbeit
 
Untersucht wird, **inwieweit empathisch formuliertes Error-Design die Recovery Time von Nutzern nach einer Interaktionsunterbrechung reduziert**. Recovery Time bezeichnet dabei die Zeit zwischen dem ersten Auftreten einer Fehlermeldung und der nächsten Aktion des Nutzers.
 
### Funktion der App
 
LogenPlatz enthält bewusst mehrere **kontrolliert auslösbare Fehlerzustände** (z. B. erfolglose Suche, ausverkaufte Events, abgelaufener Warenkorb-Timer, nicht implementierte Favoriten-Seite), die während festgelegter Aufgaben zuverlässig auftreten. Alle übrigen Aspekte der Anwendung (Layout, Ablauf, Usability) sind bewusst konstant und an bekannten Online-Shopping-Plattformen orientiert, damit sich Nutzer ohne Einarbeitung zurechtfinden und die Ergebnisse gezielt auf das Fehlerdesign zurückgeführt werden können.
 
### Experimentaufbau
 
Die App liegt in **zwei Varianten** vor, die sich ausschließlich im Design der Fehlermeldungen unterscheiden:
 
- **Design 1:** technisch-neutrales Feedback
- **Design 2:** empathisch formuliertes Feedback

Teilnehmende werden nach einem **Between-Subjects-Design** einer der beiden Varianten zugeordnet und bearbeiten anhand eines Szenarios mehrere unstrukturierte Aufgaben (Event suchen, buchen, favorisieren, Bestellung abschließen). Alle Interaktionen (Seitenaufrufe, Aktionen, Zeitstempel) werden während der Sitzung automatisch und anonymisiert protokolliert, um die Recovery Time nach jeder Fehlersituation zu berechnen.
 
Die App dient somit ausschließlich der kontrollierten Datenerhebung im Rahmen dieser Studie und ist nicht für den produktiven Einsatz vorgesehen.


## Schritte zum Ausführen der Applikation

### Voraussetzungen
- Python (Version 3.6 oder höher)
- Git

### Schritt-für-Schritt Anleitung
- Klonen Sie das GitHub-Repository auf Ihren lokalen Rechner.
- Erstellen Sie eine virtuelle Umgebung, um Abhängigkeiten isoliert zu installieren. Führen Sie dazu den folgenden Befehl aus:
> python -m venv venv
- Installieren Sie die benötigten Abhängigkeiten, die in der requirements.txt Datei aufgeführt sind:
> pip install -r requirements.txt
- Achten Sie darauf, ob am Anfang des Pfads im Terminal (venv) steht, was anzeigt, dass Sie in sich in der virtuellen Umgebung befinden. Sollte dies nicht der Fall sein, aktivieren Sie diese zunächst mit:
> .\venv\Scripts\activate.bat

#### Erstellen der Log-Datei
- Die Log-Datei ist im Repo nicht mit enthalten. Um den Programmablauf zu gewährleisten muss diese zunächst lokal erstellt werden.
- Im Ordner data/ wird die Datei log.csv benötigt.
- Die Datei sollte die folgenden Spalten enthalten:
> participant_id,condition,timestamp,client,event,page,extra

#### Nun können Sie LogenPlatz ausführen.
- Starten Sie die App im gleichen Terminal. Dabei müssen Sie die Participant_Id fürs Loggig und die Condition für das gewählte Fehlerdesign mitgeben:
- Sie können die Participant_Id beliebig anpassen. Für die Condition wählen Sie zwischen error_design_1 und error_design_2.
- Achten Sie darauf, dass nach den Variablen keine Leerzeichen eingegeben sind.
> set PARTICIPANT_ID=1_test&& set CONDITION=error_design_2&& flask run
- Öffnen Sie anschließend im Browser http://127.0.0.1:5000/ um LogenPlatz zu starten. Sie sollten nun auf der Startseite sein und mit der Suche beginnen können.

### Problemlösung
Falls Sie auf Probleme stoßen, überprüfen Sie die folgenden Punkte:
- Stellen Sie sicher, dass alle Abhängigkeiten korrekt installiert sind.
- Stellen Sie sicher, dass die virtuelle Umgebung aktiviert ist.
- Setzen Sie app.py manuell als FLASK_APP, falls die App nicht startet
> set FLASK_APP=home.py
- Stellen Sie sicher, dass die log-Datei existiert, jedoch nicht geöffnet ist.
