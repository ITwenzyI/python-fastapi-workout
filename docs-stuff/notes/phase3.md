# Phase 3 – Router & Dependencies

## 1. Was habe ich gelernt?

- Router in eigene Dateien auslagern (routers/workouts.py, routers/users.py)

- Prefix und Tags in main.py nutzen

#### Abhängigkeiten mit Depends einsetzen

- z.B. get_current_user_id() gibt Dummy User zurück

- POST /workouts setzt user_id automatisch

- GET /workouts filtert nur Workouts für diesen User

## 2. Warum ist das wichtig?

- Modularisierung = bessere Übersicht und Wartbarkeit

- Router → klare Trennung nach Themen (Users, Workouts)

- Dependencies → wiederverwendbare Logik, weniger Copy-Paste