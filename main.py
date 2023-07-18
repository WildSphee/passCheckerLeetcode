def passChecker(password: str) -> int:

    digits = ['1','2','3','4','5','6','7','8','9','0']
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    pw = password

    # rule 1 - length
    r1changes = 0
    if len(pw) < 6 or len(pw) > 20:
        r1changes = min(abs(len(pw) - 6), abs(20 - len(pw)))
    
    # rule 2 - one digit and one cap
    r2changes = 3
    for n in digits:
        if pw.find(n) >= 0:
            r2changes -= 1
            break

    for n in letters:
        if pw.find(n) >= 0:
            r2changes -= 1
            break
    
    for n in letters:
        if pw.find(n.capitalize()) >= 0:
            r2changes -= 1
            break

    #rule 3 - no cap - gas station problem
    r3changes = 0
    i = 0
    while i <= len(pw) - 3:
        if pw[i] == pw[i+1] == pw[i+2]:
            i += 3
            r3changes += 1
            continue
        i += 1
    
    # final calculation
    nchanges = 0

    #r2 and r3 both are changing
    #therefore:
    r23 = max(r2changes, r3changes)


    # for length > 20 but r2changes > 0
    if len(pw) > 20 and r23 > 0:
        r1changes += r23
    
    nchanges = max(nchanges, r23)



    print(f'{pw}\t r1={r1changes} r2={r2changes} r3={r3changes} n={nchanges}')

    # print([pw.find(n.__str__) for n in digits].__str__)
    # print([pw.find(n.capitalize) for n in letters])
    # print([pw.find(n) for n in letters])
        


    # print(f"{pw}, {nchanges=}")
    return nchanges


passChecker("a")
passChecker("aA1")
passChecker("1337c0dd") # 8 char
passChecker("1337C0d3wrrwer16") #16 char
passChecker("1337C0d3sfsacfsfcasdfasdcs28") #28 char
passChecker("1337C6") # 6 char
passChecker("NNNNNNNNNNNNNNNNNNNNN") # 21 char
passChecker("NN0NN0NNN1NNN2NN0NTN0") # 21 char
passChecker("NNNNNNNNNNNNNNNNNNNNNNNN") # 24 char
passChecker("!!!!!!!") # 7 char
passChecker("!2!!!!") # 6 char

