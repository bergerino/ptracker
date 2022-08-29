# Aplikace pro sledování časové náročnosti úkolů

Aplikace slouží pro sledování měsíční časové náročnosti úkolprojektů v rámci firmy. Sledování je možné ve třech režimech:

1. Pohled - Přehled náročnosti úkolů
V přehledu náročnosti úkolů můžete sledovat dílčí pracovní úkoly jednotlivými projekty, je zde možné vyhledávání.
Můžete se podívat kolik času vybraný zaměstnanec strávil plněvšech úkolů bez ohledu na projekt. Další možností je sledování času strávého plněním veškerých úkpatřící pod určitý projekt, ale bez ohledu na plnitele úkolu. Další varianta je kombinace dvou předešlých, takže sledování kočasu strávil určitý zaměstnanec při plnění úkolů pod určitým projektem.
2. Pohled - Celková odpracovaná doba Jedná se pouze o jednoduchou tabulku s informací o odpracované dzaměstnanců s možností vyhledávání
3. Pohled - Časová náročnost projektu. Tabulka obsahuje základní informace o projektu, ale především kose do projektu investovalo v daném měsíci času

## Návod na zprovoznění aplikace pomocí dockeru

**Možný problém**

Je možné, že při klonování repozitáře budete mít nastané zakončování řádků v režimu CLRF (Windows), docker toto bude brát jako chybu protože image běží pod linuxem. Je tedy třeba soubory důležité pro docker nastavit tak, aby měly zakončování řádků v režimu LF. Obvykle se to dá u textových editorů nebo IDE upravit ve spodní liště vpravo. (Otestováno s VS Code a Pycharm).

jedná se o soubory:
- docker-compose.yml
- Dockerfile
- requirements.txt
- entrypoint.sh

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
Při spouštění aplikace přistupujeme na adresu **http://localhost:8000/tracker/**

## Architektura aplikace
![alt text](/architektura.drawio.png)
