<img src="/img/image.png" alt="Umweltdaten Hamburg" width="200">

# 🏙️ Umweltdaten Hamburg – Analyse & Visualisierung (2005–2025)

## Projektbeschreibung

Dieses Projekt untersucht die Entwicklung von Umweltdaten in Hamburg über einen Zeitraum von 20 Jahren. Im Fokus stehen unter anderem Luftqualität, CO₂-Emissionen und Lärmwerte. Ziel ist es, Trends auf Stadtteilebene sichtbar zu machen und datenbasierte Erkenntnisse über die ökologische Entwicklung der Stadt zu gewinnen.

Die Datenanalyse erfolgt in Python (Pandas, Matplotlib, Seaborn), die Visualisierung in Tableau.

---

## 🔧 Technologien

- **Python 3.12+**
  - pandas
  - matplotlib / seaborn
  - numpy
- **Jupyter Notebooks**
- **Tableau** (Public) [https://public.tableau.com/app/profile/marcus.krause/vizzes]
- **Quellen**: Open Data Hamburg, Umweltbundesamt, DWD, Statistisches Bundesamt

---

## 📁 Projektstruktur
    umweltdaten_hamburg/
    ├── data/                   # Rohdaten & externe Quellen
    ├── notebooks/              # EDA & Analyse-Notebooks
    ├── scripts/                # Reinigungs- und Export-Skripte
    ├── tableau_exports/        # Bereinigte CSVs für Tableau
    ├── reports/                # Exportierte Visualisierungen und Dashboards
    └── README.md
---
##  Umweltfaktoren die untersucht werden :

><head></head>
Umweltfaktor | Typische Einheit | Erläuterung
-- | -- | --
Luftqualität | µg/m³ (Mikrogramm pro Kubikmeter) | Für Feinstaub (PM10, PM2.5), Stickstoffdioxid (NO₂), Ozon (O₃), Schwefeldioxid.
CO₂ | ppm (parts per million) | CO₂-Konzentration in der Luft.
Lärm | dB(A) (Dezibel, A-bewertet) | A-Bewertung berücksichtigt das menschliche Hörempfinden.
Wasserqualität | mg/l (Milligramm pro Liter), pH-Wert, NTU, µS/cm | Je nach Parameter: Nitrat, Phosphat, Trübung (NTU), Leitfähigkeit (µS/cm).
Grünflächen | m² pro Einwohner / % der Stadtfläche / ha (Hektar) | Flächenanteil von Parks, Wald etc. je nach Maßstab und Vergleichsgröße.

---

## 📊 Ziel-Visualisierungen in Tableau

- Entwicklung der Luftqualität über 20 Jahre
- Stadtteilvergleich (CO₂, Lärm, Feinstaub)
- Kartenbasierte Darstellung von Umwelt-Hotspots
- Vorher-Nachher-Vergleich (z. B. vor/nach 2020)

---

## 📌 To Do

- [ ] Datenquellen sammeln
- [ ] Explorative Datenanalyse (EDA)
- [ ] Daten bereinigen & transformieren
- [ ] Tableau-Dashboard finalisieren
- [ ] Abschlussbericht schreiben

---

## 📎 Lizenz

MIT License – feel free to use, adapt and build upon it.

---

## 🙋‍♀️ Kontakt

Projekt von Marcus Krause aka [sulfidate](https://github.com/sulfidate)  
Fragen oder Feedback? Gerne per [GitHub Issues](https://github.com/sulfidate/repo/issues) oder via E-Mail: [dev(at)sulfidate.rocks]

