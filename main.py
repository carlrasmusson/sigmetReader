from sigmet import Sigmet


examples = open('SigmetExample.txt', 'r')
f = examples.read()
examplesList = f.split('\n\n')

testList = []
for n in examplesList:
    j = Sigmet(n)
    j.parse()
    testList.append(j)
    if j.phenomenon == 'CNL':
        for sigmet in testList:
            testedId = sigmet.id
            if testedId == j.id:
                testList.remove(sigmet)

print(len(testList))



