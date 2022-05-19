# Periode_4_project

FILES:

-> Dataset periode 4 project (CSV)
Bevat de groep 3 tab uit het volledige excel 
bestand afkomstig van het HAN biocentre.


SCRIPTS:

-> main (.py)
Python script waaruit gecalled word naar de andere scripts.

-> Extract excel data (.py)
Een python script om de gegevens uit het excel bestand te filteren. 

-> Blast_script (.py)
Neemt een dictionary en blast de sequences uit deze dictionary.
Returned hiervan de blast resultaten in een xml file.

ScriptFlow:

1..Main -> roept losse scripts aan

2..Extract excel data -> file met alle excel data.

3..Blast_script -> xml files met blast results.

4..SQL_connector_script -> roept process_blast_results aan
                            en voegt de data hiervan toe
                            aan de database.

technical documentation notes:

process_blast_results:
Bij het maken van het script om de .xml files in te lezen met de 
Blast resultaten liep de groep tegen het probleem aan dat één hit
meerdere organismen en eiwitten terug kan geven. Omdat de hits meer
eiwitten en organismen kunnen bevatten worden deze meegegeven als een 
list met bij elke organisme en eiwit combinatie een id(nummer).