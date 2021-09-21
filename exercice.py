#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number <0 : 
        return -number
    else :
        return number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    cannetons = []
    for i in range(len(prefixes)) : 
        cannetons.append(str(prefixes[i]+suffixe))
    return cannetons


def prime_integer_summation() -> int:
    nb_entiers_premier = 1
    liste_premiers = [2]
    j = 3
    while nb_entiers_premier <100 :
        premier = True
        for i in range(2,j):
            if j%i ==0:
                premier = False
                break
        if premier == True:
            liste_premiers.append(j)
            nb_entiers_premier +=1
        j+=1
    return sum(liste_premiers)


def factorial(number: int) -> int:
    factoriel = 1
    for i in range(1,number+1):
        factoriel *= i
    return factoriel



def use_continue() -> None:
    for i in range(1,11):
        if i ==5 :
            continue
        else : 
            print(i)
    return ''

def verify_ages(groups: List[List[int]]) -> List[bool]:
    bool_list = []
    def taille (liste):
        if len(liste) <= 3 or len(liste) > 10 :
            return False
    def age_mineur(liste):
        for i in range(len(liste)):
            if liste[i] < 18:
                return False
    def age_70_50(liste):
        for i in range(len(liste)):
            if liste[i]>70 : 
                for k in range(len(liste)):
                    if liste[k] == 50:
                        return False


    def age_25(liste):
        for i in range(len(liste)):
            if liste[i] == 25:
                return True
    
    for i in range(len(groups)):
        if taille(groups[i]) == False:
            bool_list.append(False)

            pass
        elif age_25(groups[i]) == True and taille(groups[i]) != False :
            bool_list.append(True)
        elif age_70_50(groups[i]) == False or age_mineur(groups[i]) == False : 
            bool_list.append(False)
        else : 
            bool_list.append(True)
        

    return bool_list


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
