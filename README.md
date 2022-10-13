# Aplikace pro sledování gitlab záznamů

Aplikace slouží pro sledování měsíční časové náročnosti úkolprojektů v rámci firmy. Sledování je možné ve třech režimech:

1. Úkoly - V přehledu náročnosti úkolů můžete sledovat dílčí pracovní úkoly jednotlivými projekty, je zde možné vyhledávání.
Můžete se podívat kolik času vybraný zaměstnanec strávil plněvšech úkolů bez ohledu na projekt. Další možností je sledování času strávého plněním veškerých úkpatřící pod určitý projekt, ale bez ohledu na plnitele úkolu. Další varianta je kombinace dvou předešlých, takže sledování kočasu strávil určitý zaměstnanec při plnění úkolů pod určitým projektem.
2. Zaměstnanci - Jedná se pouze o jednoduchou tabulku s informací o odpracované doby zaměstnanců s možností vyhledávání. Tabulka rozlišuje dílčí kategorie odpracované doby, např. meetingy, bugfixy, absence.
3. Projekty - Tabulka obsahuje základní informace o projektu, ale především kose do projektu investovalo v daném měsíci času
4. Můj přehled - Kontigenční tabulka zaměřená především na použití jednotlivým zaměstnancem pro vlastní přehled o odpracované době nad úkoly v jednotlivých dnech v měsíci.

## Architektura aplikace
![alt text](/architektura.drawio.png)

## Konfigurace systému

Na samotné aplikaci nebo systému na kterém běží pro její spuštění není třeba nic moc nastavovat, je třeba pouze nakonfigurovat databázi v souboru ptracker/settings.py v adresáři projektu. Současně jsou přednastaveny dvě možnosti, které jsou od řádku 85 popsány přímo v konfiguračním souboru.

Aplikace používá několik python modulů třetí strany, docker si vše dělá automaticky, ale jedná se o tyto requirements:
- Django>=4.0.6
- psycopg2>=2.9.3
- django-db-readonly>=0.7.0

## Návod na zprovoznění aplikace pomocí dockeru a její spuštění

**Možný problém**

Je možné, že při klonování repozitáře budete mít nastané zakončování řádků v režimu CLRF (Windows), docker toto bude brát jako chybu protože image běží pod linuxem. Je tedy třeba soubory důležité pro docker nastavit tak, aby měly zakončování řádků v režimu LF. Obvykle se to dá u textových editorů nebo IDE upravit ve spodní liště vpravo. (Otestováno s VS Code a Pycharm).

jedná se o soubory:
- docker-compose.yml
- Dockerfile
- requirements.txt
- entrypoint.sh

Dále si při nasazení zkontrolujme zda má aplikace nastaveno SITE_READ_ONLY = True v settings.py, přestože má aplikace několik ochran proti zápisu do ostré databáze, pro jistotu ověřme i tento krok.

Aplikaci je ideální spouštět přes docker, v adresáři projektu se nachází oba nutné souboru pro zdockerování, docker-compose.yml a Dockerfile. Nám tedy jednoduše bude stačit spustit příkazy

```
docker-compose build
docker-compose up
```
který stáhnou veškeré image a nabuilduje veškeré potřebné kontejnery. Nicméně je potřeba vložit si do databáze testovací data. To uděláme následujícími příkazy:

Vyhledáme náš docker container s postgresql databází:
```
docker ps
```
Jedná se o container s názvem ptracker_db_1.
V adresáři s projektem máme soubor gitlab_dump_tables.sql, jedná se o zálohu databáze kterou použijeme jako testovací data, nejprve je však musíme postgresql nástrojem do databáze vložit.
Prvně dump překopírujeme do kontejneru, abychom s ním dále v rámci kontejneru mohli pracovat:
```
docker cp <cesta_k_dumpu_databaze> <container>:/home/gitlab_dump_tables.sql
```
Dále otevřeme samotný kontejner s databází v interaktivním režimu:
```
docker exec -it ptracker_db_1 bash
```
A konečně vytažení databáze z dumpu
```
psql -U postgres -f /home/gitlab_dump_tables.sql gitlabdumptables
```
Při spouštění aplikace přistupujeme na adresu **http://localhost:8000/tracker/**. V případě, že je aplikace nasazena na ostrém serveru, doménu samozřejmě měníme.

## Údržba aplikace

Z důvodu velké nepřehlednosti potenciální nepřehlednosti logovacího souboru jsem django nastavil tak, aby logger zachytil pouze errory které vedou k selhání aplikace. Nastavení loggerů je v souboru settings.py pod názvem LOGGING. Logovací soubor:

```
/debug.log
```

## Zasílání HTTP požadavků na aplikaci

Z testovacích důvodů je možné na aplikaci zasílat předpřipravený jednoduchý GET požadavek. Z postmana, či jiného HTTP klienta zašlete tento request:
```
http://localhost:8000/tracker/fungujes
```
V případě, že aplikace je funkční a reaguje na HTTP requesty, dostaneme odpověď s potvrzením, že aplikace funguje.