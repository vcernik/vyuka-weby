# AGENTS.md

Tento soubor popisuje projekt pro AI agenty a automatizované nástroje.

## Přehled projektu

**Tajný trezor** – výuková Flask aplikace demonstrující rozdíl mezi ověřením hesla na straně klienta (frontend) a serveru (backend).

## Design – barevné schéma

Aplikace používá světlý, lehce modrý barevný styl.

## Poznámky pro agenty

- Šablony používají Jinja2 a dědí od `layout.html` přes `{% extends %}`.
- `frontend.html` ověřuje heslo pouze v JavaScriptu – bezpečnostně nevhodné.
- `backend.html` ověřuje heslo na serveru pomocí POST požadavku – správný přístup.
- Při úpravách šablon zachovej bloky `{% block content %}` a `{% block scripts %}`.
- Nová trasa se přidává do `app.py` pomocí dekorátoru `@app.route`.
