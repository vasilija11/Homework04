from random import randint
def selection_sort(niz):

    duzina = len(niz)

    for pozicija in range(duzina-1):             
        minimum = pozicija

        for i in range(minimum+1, duzina):

            if niz[i] < niz[minimum]:
                minimum = i

        niz[pozicija], niz[minimum]= niz[minimum], niz[pozicija]

    return niz


if __name__== "__main__":
    niz=[]

    for i in range(1000):
        niz.append(randint(0,1000))

    sortirani_niz=selection_sort(niz)
    print(sortirani_niz)
