# Digitale Schatzsuche – 9 Posten

## Enthalten
- `index.html`: mobile Website mit dunklem, schatzkartenartigem Design
- `stations.json`: neun Texte und zufällige Tokens
- `make_qr_codes.py`: erstellt die QR-Codes nach dem Hosting
- `fotos/`: Platz für eigene Fotos

## Online stellen
1. Erstelle ein kostenloses GitHub-Konto und ein neues Repository.
2. Lade `index.html` und `stations.json` hoch (die Seite enthält die Daten bereits eingebettet; `stations.json` ist die lesbare Arbeitskopie).
3. Im Repository: **Settings → Pages**, Quelle `Deploy from a branch`, Branch `main`, Ordner `/root`, speichern.
4. Sobald GitHub Pages eine URL anzeigt, öffne `make_qr_codes.py` und trage sie bei `BASE_URL` ein.
5. Installiere Python-Paket `qrcode[pil]` und führe das Skript aus. Die PNGs sind dann druckfertig.

## QR-Codes erst nach dem Hosting erzeugen
QR-Codes können erst die echte Website-Adresse enthalten, wenn diese feststeht. Die zufälligen Tokens verhindern leichtes Erraten von Stationsnummern.

## Fotos ergänzen
Lade deine Bilder in den Ordner `fotos/` hoch. Trage bei der passenden Station in `index.html` im Feld `photo` z.B. `fotos/posten1.jpg` ein. Ändere dieselbe Station auch in `stations.json`, damit beide Kopien gleich bleiben.

## Ehrliche Sicherheitsgrenze
Das ist eine statische Website: Die URLs sind zufällig und nicht nummeriert, aber alle Stationstexte stecken im ausgelieferten Quellcode. Für eine private Geburtstagsschatzsuche reicht das gegen simples Überspringen normalerweise. Echter Schutz vor technisch versierten Leuten braucht einen Server oder Passwortdienst.
