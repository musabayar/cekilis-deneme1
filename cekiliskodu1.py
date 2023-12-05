import random

isimler = ['isim 1','isim 2','isim 3','isim 4','isim 5','isim 6','isim 7','isim 8','isim 9','isim 0']

def hediye_cekilisi():
    alanlar= isimler.copy()
    verenler= isimler.copy()

    while len(alanlar) > 0:
        alici_index = random.randint(0, len(alanlar) -1)
        verici_index = random.randint(0, len(verenler) -1) 

        while alanlar[alici_index] == verenler[verici_index]:
            alici_index = random.randint(0, len(alanlar) -1)
            verici_index = random.randint(0, len(verenler) -1)

        print(alanlar[alici_index], 'su kisiye hediye alacak: ',verenler[verici_index])
        #del alanlar[alici_index] asadakiyle ayni isi goruyomus hoca dedi
        #del verenler[verici_index]
        alanlar.remove(alanlar[alici_index])
        verenler.remove(verenler[verici_index])

hediye_cekilisi()


