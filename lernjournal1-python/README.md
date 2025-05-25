# Lernjournal 1 Python

## Repository und Library

| | Bitte ausfüllen |
| -------- | ------- |
| Repository (URL)  |
| Kurze Beschreibung der App-Funktion |Ziel des Projekts war es, eine intelligente Webanwendung zu entwickeln, die Heilpflanzen auf Basis von Benutzersymptomen vorschlägt. Dies geschieht durch semantisches Matching von eingegebenem Freitext mit einem vordefinierten Heilpflanzen-Symptom-Datensatz. |
| Verwendete Library aus PyPi (Name) | streamlit
||scikit-learn	
||nltk	
||pandas	
||sentence-transformers	
||transformers	
||torch	
||beautifulsoup4
|
| Verwendete Library aus PyPi (URL) | 
||https://pypi.org/project/scikit-learn/
||https://pypi.org/project/nltk/
||https://pypi.org/project/pandas/
||https://pypi.org/project/sentence-transformers/
||https://pypi.org/project/streamlit/
||https://pypi.org/project/transformers/
||https://pypi.org/project/torch/
||https://pypi.org/project/beautifulsoup4/
| ... | |
| ... | |

## App, Funktionalität

 Nutzeroberfläche
Die Benutzer geben über eine einfache Streamlit-Seite Symptome ein.

Semantische Suche
Die Texteingabe wird mit SentenceTransformer in einen Vektor umgewandelt und mit bestehenden Symptomvektoren verglichen. Das Modell distiluse-base-multilingual-cased-v1 liefert die Top-N ähnlichsten Einträge aus dem CSV-Datensatz zurück.

Scrapy-Crawler
Der Scrapy-Crawler lädt automatisiert Heilpflanzenseiten und extrahiert Name + Anwendungsgebiete via xpath / css.

Selenium-Skript
Für unvollständige Daten (ohne Symptome) wird mit Selenium dynamisch nachgeladen. Die Einträge stammen aus einer JSON-Datei und die Ergebnisse werden in MongoDB gespeichert.

BeautifulSoup-Test
Die Datei test_bs4.py diente der Analyse, ob HTML-Strukturen korrekt geparst werden können, insbesondere <ul>-Listen nach dem „Anwendungsgebiete“-Header.

## Dependency Management

 Für das Management der Projektabhängigkeiten wurde eine requirements.txt verwendet. Diese enthält alle benötigten Python-Pakete mit exakten Versionsangaben (z. B. sentence-transformers==2.2.2, torch>=1.10, streamlit). Dadurch ist sichergestellt, dass die Anwendung auf jedem System mit den gleichen Bibliotheken ausgeführt werden kann.

Zusätzlich sorgt das Dockerfile dafür, dass beim Container-Build automatisch alle Abhängigkeiten installiert werden:


RUN pip install --no-cache-dir -r requirements.txt

Diese Kombination ermöglicht eine reproduzierbare und portable Entwicklungsumgebung, sowohl lokal als auch beim Deployment (z. B. via GitHub Actions oder DockerHub).

## Deployment

 Die Anwendung wird mit einem einfachen dockerfile containerisiert. Sie läuft dann auf Port 8501 mit dem Befehl:

streamlit run app.py --server.port=8501 --server.address=0.0.0.0

Eine GitHub Action (docker-build.yml) automatisiert den Build und Upload in DockerHub.
Leider ist es mir in diesem Projekt nicht möglich gewesen via Azure zu deployen. Ich habe das deployment 6h lang versucht, bis ich am ende immerwieder den Error bezüglich Nutzerrechte und einschränkung meines Students Account erhalten habe.

