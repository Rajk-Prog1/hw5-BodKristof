def eggs_solution(breaks):
    lepes=14
    szamolo=1

    for i in range(0,14):
        szamolo=szamolo+lepes
        if breaks(szamolo):
            for j in range(szamolo-lepes,szamolo):
                if breaks(j):
                    return j - 1
        else:
            lepes=lepes-1

