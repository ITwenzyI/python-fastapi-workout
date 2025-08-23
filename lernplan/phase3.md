# Lernplan für Phase 3 – Router & Abhängigkeiten

## Ziel
- Dein Projekt wird modular und erweiterbar.
- Du lernst, wie Router sauber eingebunden werden.
- Du lernst Abhängigkeiten (Dependencies) kennen – ein mächtiges Werkzeug von FastAPI.

### 1. Projektstruktur verstehen und aufbauen

- Warum Modularisierung?

- Bessere Übersicht

- Leichter testbar

- Bessere Wartbarkeit, wenn später User, Auth, Patientenakte usw. dazukommen

### 2. Router einbinden und verstehen

- Router werden in main.py registriert.

### 3. Abhängigkeiten (Dependencies) – Einstieg

- Dependencies sind kleine Bausteine, die automatisch vor einer Route ausgeführt werden.

Einsatzmöglichkeiten:

- Filter nach User ID (z.B. Workouts nur für diesen User)

- Authentifizierung (Dummy-Version)

- Logging oder Zeitmessung

### 4. Abhängigkeiten in Routen einbauen

- Abhängigkeiten werden mit Depends genutzt.

### 5. Theorie-Tag – Warum Modularisierung + Dependencies wichtig sind

- Klarer Aufbau = besser skalierbar.

- Dependencies = weniger Code-Dopplung.

- Sicherheit & Wiederverwendung für später (Auth, DB, Logging).

### 6. Mini Projekt – Workout Tracker modularisieren

- Workouts bleiben in routers/workouts.py.

- User-Router in routers/users.py.

- Dummy-Dependency sorgt dafür, dass Workouts immer nur für einen „eingeloggten“ User sind.

- Alles läuft wie bisher in den Docs.

### 7. Tests erweitern

- Testen, ob die Abhängigkeit greift (z.B. Workout hat richtige User-ID).

- Prüfen, ob beide Router sauber eingebunden sind.