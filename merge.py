def merge(niz1, niz2):

    zbirni= []
    duzina1=len(niz1)
    duzina2=len(niz2)

    i=0
    j=0


    while i < duzina1 and j < duzina2:
        if niz1[i] < niz2[j]:
            zbirni.append(niz1[i])
            i+=1
        else:
            zbirni.append(niz2[j])
            j+=1

    while i < duzina1:
        zbirni.append(niz1[i])
        i+=1

    while j < duzina2:
        zbirni.append(niz[j])
        j+=1

    return zbirni

def merge_sort(niz):

    duzina=len(niz)

    if duzina==1:
        return niz

    mid=duzina//2

    lijevi= niz[:mid]
    desni= niz[mid:]

    lijevi=merge_sort(lijevi)
    desni= merge_sort(desni)

    return merge(lijevi, desni)

niz=[3,1,5,2,6,8,7]
print(merge_sort(niz))