# Závěrečný projekt: Vlastní webová aplikace

## Zadání

Vytvoř vlastní jednoduchou webovou aplikaci pomocí Flasku. **Téma a funkci aplikace si vymysli sám/sama** – důležité je, aby splňovala technická kritéria níže. Aplikace musí mít smysl: uživatel na ní něco zadá, server to zpracuje a vrátí mu výsledek.

---

## Co musí aplikace umět (technická kritéria)

### Povinné

1. **Více stránek** – aplikace má alespoň 2 různé URL (routy).
2. **Formulář s metodou POST** – alespoň jeden formulář odesílá data na server metodou POST.
3. **Zpracování dat na serveru** – backend přijatá data skutečně zpracuje (nestačí je jen zobrazit zpět).
4. **Výstup pro uživatele** – výsledek zpracování se zobrazí v HTML šabloně.
5. **Validace vstupu** – server zkontroluje, zda uživatel zadal platná data, a při chybě zobrazí srozumitelnou hlášku.
6. **Šablony** – aplikace používá Jinja2 šablony; stránky sdílejí společný layout (`extends`).
7. **Nasazení online** – aplikace běží na veřejné URL (Render.com nebo jiná služba).
8. **GitHub repozitář** – kód je verzovaný a dostupný.

### Volitelné (pro lepší hodnocení)

- Použití `session` pro zapamatování stavu přes více požadavků.
- Čtení dat ze souboru (JSON, CSV) nebo zápis do souboru.
- Hezký CSS styl (vlastní nebo framework Bootstrap).
- Ošetření chyby 404 vlastní stránkou.

---

## Co odevzdat

1. **Odkaz na GitHub repozitář** (veřejný).
2. **Odkaz na běžící aplikaci** (Render nebo jiné nasazení).
3. **Krátký popis** (4–8 vět):
   - Co aplikace dělá a proč jsi si vybral/a právě toto téma.
   - Co ti šlo dobře a co byl největší problém.

---


## Příklady projektů

Níže najdeš ukázky toho, jak by takový projekt mohl vypadat. Můžeš si vybrat jeden z nich, nebo si vymyslet vlastní téma.

---

### 1. Kalorická kalkulačka

Uživatel zadá seznam jídel a jejich gramáž. Server spočítá přibližný celkový příjem kalorií a zobrazí přehled. Data o kaloriích jsou uložena v JSON souboru na serveru.

---

### 2. Tajný vzkaz

Uživatel napíše zprávu a zvolí jednoduchý způsob zašifrování (např. Caesarova šifra, obrácení textu). Server text zašifruje a zobrazí výsledek, který si uživatel může zkopírovat. Na druhé stránce je možnost zprávu dešifrovat.

---

### 3. Generátor náhodných úkolů

Student zadá předmět (např. „matematika") a obtížnost. Server vybere náhodný příklad nebo otázku z připraveného souboru a zobrazí ji. Po zodpovězení ukáže správnou odpověď.

---

### 4. Hlasovací aplikace

Uživatel vidí seznam možností (např. oblíbená jídla, filmy) a může hlasovat. Server uloží hlasy do souboru a zobrazí aktuální výsledky hlasování jako přehled nebo procenta.

---

### 5. BMI kalkulačka s radou

Uživatel zadá výšku a váhu. Server spočítá BMI, zařadí výsledek do kategorie (podváha, norma, nadváha…) a zobrazí stručnou radu. Výsledek je stylizovaný podle kategorie (jiná barva).

---

### 6. Náhodný citát dne

Uživatel klikne na tlačítko a server mu vrátí náhodný citát ze souboru. Může si filtrovat citáty podle tématu (motivace, humor, filozofie). Každý citát má autora.

---

### 7. Jednoduchý kvíz

Aplikace zobrazí sérii otázek (z oblasti, kterou si autor vybere – zeměpis, filmy, sport…). Uživatel označí odpovědi a po odeslání server vyhodnotí skóre a zobrazí, které otázky zodpověděl správně.

---

### 8. Převodník jednotek

Uživatel zadá hodnotu a vybere typ převodu (km ↔ míle, °C ↔ °F, kg ↔ libry…). Server provede výpočet a zobrazí výsledek. Aplikace nabízí více kategorií převodů na různých stránkách.
