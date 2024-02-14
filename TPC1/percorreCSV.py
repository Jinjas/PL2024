#quero
#lista ordenada de modalidades
#percentagens chiques aptos e inaptos
#Distribuição de atletas por escalão etário

import sys

def percorreCSV(file):
    listaDeModalidades = []
    aptos = 0
    total = 0
    distribuicoes = {}

    #skip the lable line
    next(file)


    for line in file:
        row = line.rstrip().split(',')
        total +=1

        nome = row[3] + ' ' + row [4]
        idade = int(row[5])
        key = (idade//5)*5 
        #adicionar o nome da modalidade
        if row[8] not in listaDeModalidades:
            listaDeModalidades.append(row[8])
        listaDeModalidades.sort()
        if row[12] == 'true':
            aptos +=1

        if key not in distribuicoes:
            distribuicoes[key] =(1)
        else:
            quantos = distribuicoes[key]
            distribuicoes[key]= (quantos+1)
    
    return listaDeModalidades,aptos,total,distribuicoes


def main():
    listaDeModalidades, aptos, total, distribuicoes = percorreCSV(sys.stdin)

    print("Modalidades desportivas disponiveis:")
    for i in listaDeModalidades:
        print("\t",i)
    print("\n")
    
    print("Percentagem de atletas aptos:", (aptos/total)*100,"%)")
    print("Percentagem de atletas inaptos:", ((total-aptos)/total)*100,"%)")
    print("\n")

    for i in range(0, 100, 5):
        if i in distribuicoes: 
            print(f"[{i}-{i+4}]:", distribuicoes[i],"/",total,"(" ,distribuicoes[i]/total*100,"%)")
    

if __name__ == "__main__":
    main()