# Lernplan für Phase 4 – Datenbanken


## Schritt 1: Projektbasis vorbereiten

#### Ziel: Saubere Ordner, Konfiguration, DB URL per Umgebung.

Ordner anlegen: db, models, repositories, tests.

.env einführen mit DATABASE_URL=sqlite:///./workouts.db.

Eine kleine Konfigurationsfunktion schreiben, die die DB URL ausliest.
Beispielidee

Eine Funktion get_settings() die aus .env liest und ein Objekt mit database_url zurückgibt.
DoD

app startbar, aber noch ohne Tabellen.

Commit: chore: add base dirs and env config

## Schritt 2: SQLModel installieren und Engine definieren

#### Ziel: Engine und Session Management bereitstellen.

SQLModel installieren.

In db/engine.py: Engine erstellen aus database_url.

In db/session.py: SessionLocal und eine FastAPI Dependency get_session() erstellen.
Beispielidee

Eine Dependency, die per yield eine Session bereitstellt und danach schließt.
DoD

Eine kleine Probe Route, die nur testweise eine Session öffnet und wieder schließt.

Commit: feat: add engine and session dependency

## Schritt 3: Modelle definieren

#### Ziel: User und Workout als SQLModel Klassen.


models/user.py: id, email, created_at.

models/workout.py: id, user_id (FK), date, type (Enum), duration_min, notes optional, Timestamps optional.

Ein Enum für Workout Typen wie in Phase 3.
Beispielidee

Nur als Muster: FK definieren, Enum Feld, __tablename__ setzen.
DoD

Beide Klassen kompilieren fehlerfrei.

Commit: feat: add user and workout models with enum

## Schritt 4: Alembic initialisieren und Basismigration

#### Ziel: Tabellen entstehen über Migrationen.


Alembic init.

alembic.ini auf deine DATABASE_URL aus .env konfigurieren.

Script env so anpassen, dass SQLModel Metadaten für Autogenerate bekannt sind.

Erste Autogenerate Migration erstellen und anwenden.
Beispielidee

In der env Datei von Alembic die Meta aus deinen Modellen importieren und target_metadata setzen.
DoD

alembic upgrade head erzeugt users und workouts in workouts.db.

Commit: chore: init alembic and create base migration

## Schritt 5: Constraints und Indizes

#### Ziel: Regeln in der Datenbank verankern.


Unique Constraint auf (user_id, date, type).

Check Constraint duration_min > 0.

Index auf user_id, date für schnelle Abfragen.
Beispielidee

In SQLModel kannst du über __table_args__ einen UniqueConstraint und CheckConstraint setzen.

Danach neue Migration autogenerieren.
DoD

Migration angewandt, Tabellen haben die Constraints.

Commit: feat: add unique and check constraints with migration

## Schritt 6: Repository Schicht

#### Ziel: Saubere CRUD Zugriffe, Router bleibt schlank.


repositories/users.py: create, get_by_id, get_by_email.

repositories/workouts.py: create, get_by_id, list_by_user, update, delete.

Fehlerbilder definieren: beim Duplikat eine elegante Ausnahme werfen, die der Router später in einen passenden Statuscode übersetzt.
Beispielidee

In den Repos mit der Session arbeiten und SQLModel Klassen nutzen, Transaktionen über die Dependency.
DoD

Manuell in einer kleinen Probe Route testen: ein User anlegen und ein Workout speichern.

Commit: feat: add user and workout repositories

## Schritt 7: Router an Datenbank anbinden

#### Ziel: Deine bestehenden Workout Endpunkte nutzen jetzt die Repos.


Dependency get_session in die Router Funktionen einbinden.

Statt In Memory Liste die Repo Funktionen rufen.

Eindeutigkeit sauber behandeln: bei Verstoß sauberer Fehlercode.

Optionale Validierung: Datum nicht in der Zukunft in der Request Verarbeitung prüfen.
Beispielidee

Im Router eingehende Daten validieren, dann Repo call, dann Response Schema zurückgeben.
DoD

POST, GET, PUT, DELETE funktionieren gegen SQLite.

Neustart der App zeigt, dass Daten erhalten bleiben.

Commit: feat: wire routers to repositories and db

## Schritt 8: Seed Script für Dummy Daten

#### Ziel: Deine vorhandenen Dummy Daten einmalig sauber übernehmen.


Ein kleines Skript, das aus einer Liste von Dicts Users und Workouts anlegt.

Beim Einspielen Duplikate überspringen oder melden.
Beispielidee

Schleife über Dummy Datensätze, erst User prüfen oder anlegen, dann Workout einfügen.
DoD

Nach dem Lauf sind die Daten in SQLite sichtbar.

Commit: chore: add seed script for sample data

## Schritt 9: Tests für Datenbankfunktionen

#### Ziel: Automatisierte Tests prüfen die wichtigsten Fälle.


Test Setup: temporäre SQLite Datei, frische Tabellen, App mit TestClient starten.

Tests für Create und Read bei Workouts.

Tests für den Unique Verstoß.

Tests für duration_min Fehlerfall.

Optional: Test für Datum in der Zukunft auf Applikationsebene.
Beispielidee

Ein Fixtur, die vor den Tests die DB Datei löscht, Engine neu baut und Alembic auf head bringt oder direkt create_all nur für Tests verwendet.
DoD

Alle Tests grün, mindestens 4 sinnvolle Testfälle.

Commit: test: add db tests for workouts

## Schritt 10: README Phase 4

#### Ziel: Dokumentation deiner Datenbankstruktur und Lernpunkte.


Kurze Erklärung, warum relationale Datenbanken.

ER Skizze in Worten: User 1:n Workouts.

Wichtige Constraints und warum sie wichtig sind.

Wie man lokal startet und Migrationen fährt.

Checkliste Erfolgskontrolle.
DoD

README im Repo, sauber gegliedert.

Commit: docs: add Phase 4 database README