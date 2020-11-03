liste = [input("Lav en ting til indkøbslisten "),input("Lav endnu ting til indkøbslisten "),input("Lav endnu ting til indkøbslisten "),input("Lav endnu ting til indkøbslisten ")]
for punkt in liste:
    print(punkt)
liste.pop()
liste.insert(0, input("Hvad er det vigtiste? "))
liste.append(input("Noget blev slettet "))
A = input("Vil du slette noget? ")
if A in liste:
    liste.remove(A)
else:
    print("HOV DET VAR DER IKKE!")
    pass
doublelist = liste.copy()
print("1. lister")
for punkt in liste:
    print(punkt)
print("extra liste")
for punkt in doublelist:
    print(punkt)
#print(liste)
