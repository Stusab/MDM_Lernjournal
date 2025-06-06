# Woche 3: ONNX Modellanalyse und Inferenz-Vergleich

## Was habe ich gemacht?
Diese Woche stand im Zeichen der ONNX-Runtime und des Verständnisses vortrainierter Modelle. Ich habe ein ONNX-Modell (EfficientNet-Lite4) analysiert und anschließend zwei Varianten (Original vs. quantisiert) auf drei Testbilder angewendet und verglichen.

## Wie bin ich vorgegangen?
1. **Modellauswahl**: Ich habe das Modell `efficientnet-lite4-11.onnx` aus dem offiziellen ONNX Model Zoo heruntergeladen.
2. **Modellanalyse mit Netron**: Das Modell wurde mit Netron geöffnet. Ich analysierte den Aufbau (u. a. Eingabegröße 1×224×224×3, Conv2D-Schichten, BatchNormalization, etc.).
   - ![Netron Analyse](../lernjournal3-onnx/images/netron.png)
3. **Projektstruktur**: Die Modellvarianten sowie das Testskript `compare_models.py` wurden lokal organisiert.
   - ![Projektstruktur](../lernjournal3-onnx/images/Struktur_Verzeichnis.png)
4. **Inferenz-Vergleich**: Mit dem Skript wurden die Modelle `efficientnet-lite4-11.onnx` und `efficientnet-lite4-11-int8.onnx` auf drei Bilder angewendet.
   - Bilder: `Australien.png`, `Buchstabensalat.jpg`, `Tiere-im-Wald.jpg`
   - ![Terminalvergleich](../lernjournal3-onnx/images/Terminal_inferenz-Vergleich.png)

## Was habe ich gelernt?
- Netron ist ein hilfreiches Tool zur Visualisierung von ONNX-Modellen.
- ONNX-Modelle lassen sich mit `onnxruntime` einfach in Python ausführen.
- Quantisierte Modelle sind kleiner und schneller, aber leicht ungenauer.
- Die strukturelle Analyse verbessert mein Verständnis von CNN-Architekturen.

## Welche Probleme habe ich gelöst?
- Der ONNX-Ladefehler lag an einer korrupten Datei. Ich habe das Modell erneut heruntergeladen.
- Ein Shape-Mismatch bei der Inferenz wurde durch korrektes Preprocessing behoben.
