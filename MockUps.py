from random import randint

def genMvacas(n,nombre):
    with open(nombre+'.txt','w') as txt:
        for x in range(n):
            id_ani = randint(1,n)
            txt.write(f"{id_ani} animal{id_ani} \n")
        txt.write("fin"+str(x))

genMvacas(10000000,"Animales10000k")
    