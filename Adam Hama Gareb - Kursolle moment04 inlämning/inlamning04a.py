sida1 = int(input("Ange rektangelns längd: "))
sida2 = int(input("Ange rektangelns bredd: "))

area = sida1 * sida2

print("Rektangeln har sidorna", sida1, "och", sida2, "vilket gör att arean är", area)

if sida1 == sida2:
    print("Eftersom båda sidorna är lika långa så är denna rektangel en kvadrat.")

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