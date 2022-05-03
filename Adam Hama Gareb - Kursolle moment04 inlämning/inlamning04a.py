#Här är input variablerna vart man anger längden till både längden och bredden av en rektangel
#Svaren är inställd till att vara interger då man skulle använda sig av heltal till den här uppgiften
sida1 = int(input("Ange rektangelns längd: "))
sida2 = int(input("Ange rektangelns bredd: "))

#Det här är berkäkningen som beräknar arean åt dig efter du angett de två olika sidornas längd
area = sida1 * sida2

#Det här är texten som den här koden kommer att printa ut efter den har beräknat arean på rektangeln
#och visar för användaren vad arean blev
print("Rektangeln har sidorna", sida1, "och", sida2, "vilket gör att arean är", area)

#Ifall det visade sig att båda sidorna var lika långa så kommer den här koden veta om det och printa
#ut det som står nedan om att rektangeln användaren angett är en kvadrat
if sida1 == sida2:
    print("Eftersom båda sidorna är lika långa så är denna rektangel en kvadrat.")

#Det här är en tabell som visar vad volymen skulle blivit på rektangeln ifall den hade en höjdlängd,
#som då skulle multipliceras med den arean vi redan fått fram tidigare. Vi har exempel från höjden
#1 fram till 10, för att ge idén över hur sto volym den möjliga rätblocken skulle haft med de olika
#höjdlängderna
print("\nHöjden | Volymen \n----------------")
print("     1 |    ", 1 * area)
print("     2 |    ", 2 * area)
print("     3 |    ", 3 * area)
print("     4 |    ", 4 * area)
print("     5 |    ", 5 * area)
print("     6 |    ", 6 * area)
print("     7 |    ", 7 * area)
print("     8 |    ", 8 * area)
print("     9 |    ", 9 * area)
print("    10 |    ", 10 * area)