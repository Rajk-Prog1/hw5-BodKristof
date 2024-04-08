def eggs_solution():
    lepes=14
    szamolo=1
    emelet=0

    for i in range(0,14):
        szamolo=szamolo+lepes
        lepes=lepes-1
        if breaks(szamolo):
            for j in range(szamolo-(lepes+1),szamolo):
                if breaks(j):
                    return j-1
                    break
            return emelet
    return 100
    

