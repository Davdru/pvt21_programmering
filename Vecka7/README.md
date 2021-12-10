# Vecka 7
Fokus för veckan kommer att ligga på arbete med tuples och strängar
Vi kommer att använda oss av pythons slice-operationer för att plocka ut delar av, eller på andra
sätt manipulera dem.


Både tuples och strängar är immutable eller på svenska oföränderliga. När de väl har skapats kan 
de inte ändras. Det låter kanske lite konstigt, särskilt med tanke på att vi använt 
operationer som exempelvis upper 
 
```python
"hello".upper()
```
För att ändra en sträng till endast upper case (stora bokstäver). 
Vad som faktiskt hänt är dock inte att vi ändrat varje bokstav i strängen till sin versal-variant
utan vi har skapat en helt ny sträng baserad på den gamla.

På samma sätt kan en tuple inte förändras efter att vi skapat den. 
Till skillnad från en lista eller en dictionary kan vi inte göra följande

```python
>>> t = (1,2,3)
>>> t[0] = 10
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>>

```
Vi får ett fel/exception som talar om att ett objekt av typen tuple inte stöder assignment.
Det vill säga att vi kan inte säga att det första elementet i en existerande tuple
nu skall ha värdet 10 till exempel


## Tuples
En tuple är en ordnad sekvens av värden som när den skapats inte kan ändras.
Vi kan ta varje del av det påståendet och översätta till svenska
#### ordnad
Varje element, eller stycke data i en tuple har sin bestämda plats, exempel:
```python
t = (3,1,5,67)
```
Här består tuplen t av fyra tal, 3, 1, 5 och 67 i just den ordningen

#### Kan inte ändras
Vi kan inte ta bort ett element, t.ex. det första (3) ur tuplen.
Vi kan heller inte byta ut ett element på det sätt vi kan i exempelvis en lista.


### När använder vi tuples?
Tuples använder vi ofta för att klumpa ihop data som på ett naturligt sätt hör ihop.
Ett exempel skulle kunna vara för att representera en punkt i ett kartesiskt koordinatsystem,
(x, y)


Att vi packar ihop våra värden i en tuple fungerar också som en signal från programmeraren 
att det här är värden som inte är tänkta att ändras på. 




Uppgifter
Skapa en funktion som ger oss slumpmässiga punkter i 

## Strängar