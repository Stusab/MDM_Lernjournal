# Woche 2 – Container & Docker Basics

## Inhalte der Woche

In Woche 2 habe ich mich mit den Grundlagen von Docker beschäftigt. Ich habe gelernt, wie man ein Image aus dem Docker Hub herunterlädt, daraus einen Container erstellt, diesen startet und über den Browser darauf zugreift. 

Als praktisches Beispiel habe ich das offizielle Image von **MediaWiki** verwendet und erfolgreich eine Web-Anwendung in einem Container lokal ausgeführt.

## Vorgehen

1. Ich habe über das Terminal das aktuelle MediaWiki-Image mit folgendem Befehl geladen:

    ```bash
    docker pull mediawiki:1.42.3
    ```

2. Anschließend habe ich den Container mit diesem Befehl gestartet:

    ```bash
    docker run --name wiki-container -p 8081:80 -v mediawiki:/var/www/html -d mediawiki:1.42.3
    ```

    Dadurch wurde MediaWiki auf `http://localhost:8081` verfügbar gemacht.

3. Im Browser erschien die MediaWiki-Weboberfläche mit dem Hinweis, dass die `LocalSettings.php` noch nicht eingerichtet ist – ein typisches Zeichen dafür, dass die Anwendung korrekt läuft und bereit zur Konfiguration ist.

4. Mit dem Befehl `docker ps` konnte ich mir anzeigen lassen, dass der Container erfolgreich läuft.

## Screenshots

### MediaWiki-Weboberfläche im Browser

![MediaWiki im Browser](../images/woche02_mediawiki-browser.png)

### Terminalausgabe mit `docker ps`

![Docker PS](../images/woche02_docker-ps.png)

## Docker Compose Deployment

Um die Containerverwaltung zu vereinfachen, habe ich zusätzlich ein `docker-compose.yml` erstellt. Es enthält zwei Services: MediaWiki (Frontend) und MariaDB (Datenbank).

```yaml
version: '3.3'

services:
  db:
    image: mariadb:10.5
    restart: always
    environment:
      MYSQL_DATABASE: mediawiki
      MYSQL_USER: wikiuser
      MYSQL_PASSWORD: wikisecret
      MYSQL_ROOT_PASSWORD: rootpass
    volumes:
      - db_data:/var/lib/mysql

  mediawiki:
    image: mediawiki:1.39
    restart: always
    ports:
      - "8080:80"
    environment:
      MEDIAWIKI_DB_TYPE: mysql
      MEDIAWIKI_DB_HOST: db
      MEDIAWIKI_DB_NAME: mediawiki
      MEDIAWIKI_DB_USER: wikiuser
      MEDIAWIKI_DB_PASSWORD: wikisecret
    depends_on:
      - db

volumes:
  db_data:
```

Die Container wurden mit folgendem Befehl gestartet:

```bash
docker-compose up -d
```

Anschließend war MediaWiki unter `http://localhost:8080` erreichbar.

### Docker Compose Terminalausgabe

![docker-compose-up](../images/b3ebf40b-3152-4bcb-8794-878d5047e257.png)

Durch `docker-compose` wurde mir bewusst, wie effektiv man mehrere abhängige Dienste orchestrieren kann. Es erleichtert die Verwaltung deutlich gegenüber der manuellen Einzelkonfiguration.

## Erkenntnisse

Ich habe durch diese Übung verstanden, wie schnell sich fertige Anwendungen mit Docker lokal starten lassen. Besonders hilfreich war zu sehen, wie die Kombination von Image, Container, Volume und Portweiterleitung zusammenspielt, um eine Anwendung direkt im Browser verfügbar zu machen.

Der Ansatz „Build once, run anywhere“ ist nun für mich greifbar. Ich sehe darin großes Potenzial, um Entwicklungs- und Deploymentprozesse zu vereinfachen.

## Ausblick

In der nächsten Woche möchte ich mich mit dem Speichern und Bereitstellen von Machine Learning Modellen beschäftigen. Zusätzlich plane ich, mich mit **Docker Compose** auseinanderzusetzen, um mehrere Container (z. B. App und Datenbank) gemeinsam zu verwalten.
