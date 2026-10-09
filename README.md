# Network Scanner

Ein kleines, bewusst schlankes Python-Tool zur Erkennung erreichbarer Hosts in **eigenen oder ausdrücklich autorisierten Netzwerken**.

```text
  ┌─ GeekStation / Network Scanner ──────────┐
  │  Ping-basierte Host-Erkennung             │
  │  Hostnamen-Auflösung · parallele Anfragen │
  └──────────────────────────────────────────┘
```

## Was das Tool macht

- akzeptiert einen Netzwerkbereich im CIDR-Format
- prüft Hosts parallel per Ping
- löst für erreichbare Hosts nach Möglichkeit den Namen auf
- läuft unter Windows, Linux und macOS mit der jeweiligen `ping`-Variante
- benötigt keine zusätzlichen Python-Pakete

## Schnellstart

Voraussetzung: Python 3.

```bash
git clone https://github.com/CeeLeeT/network-scanner-python.git
cd network-scanner-python
python scanner.py 192.168.1.0/24
```

Die Anzahl paralleler Anfragen lässt sich anpassen:

```bash
python scanner.py 192.168.1.0/24 --workers 32
```

## Beispielausgabe

```text
Scanning 192.168.1.0/24 ...
[UP] 192.168.1.10    lab-host
[UP] 192.168.1.20    nas
```

## Sicherheitsrahmen

Dieses Projekt ist ein Lern- und Diagnosewerkzeug. Nutze es nur in Netzwerken, für die du eine eindeutige Erlaubnis hast. Es führt keinen Portscan und keine Sicherheitsprüfung durch.

## Aufbau

| Datei | Zweck |
| --- | --- |
| `scanner.py` | Kommandozeilenprogramm für Ping-Checks und Namensauflösung |

## GeekStation

Teil der persönlichen Sammlung kleiner Tools für Linux, Netzwerke und Security: [GeekStation](https://ceeleet.github.io/)
