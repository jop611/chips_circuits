# Chips-Circuits

## Regels:
### - De lijnen mogen niet langs dezelfde route gaan
### - De lijnen mogen elkaar niet kruisen
### - De lijn mag niet buiten de grid komen, 17x12 voor print 1 en 17x16 voor print 2

## Werkwijze:
### Tot nu toe:

Er wordt met python gewerkt voor deze case. De csv bestanden worden gelezen en de coordinaten van de chips worden in een dictionary gestopt. De netlists worden in een lijst gestopt. Er is voor een lijst gekozen ipv een dictionary, omdat de volgorde niet echt uitmaakt van de verbindingen die gemaakt moeten worden. 
### Toekomst:

Er zal naar de netlist gekeken worden, per connectie zal de route stap voor stap uitgestippeld worden. Ondertussen moeten de coordinaten worden bijgehouden en deze worden toegevoegd aan een dictionary waarbij de key de connectie tussen 2 chips is. Per stap moet worden gekeken of een chip bereikt is, zo ja of de juist chip bereikt is. Ook moet worden gecheckt of de stap gemaakt mag worden. Dit kan worden gedaan door te checken of de coordinaten van de stap die je wil zetten in die ene dictionary zitten waarbij de gemaakte stappen opgeslagen zijn. Het programma moet ook bijhouden welke richtingen (4 richtingen in 2D, 6 richtingen in 3D) al gecheckt zijn om een inifinite loop te voorkomen.

Presentatie notities:
- Upper & Lower bound
