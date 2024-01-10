
from math import sqrt
import EnhancedTerminal as ET
a : str = ""
values : list = []
uncertains : list = []
print("\n")
ET.print_category("#### USER DATAS ####")
print("Enter Value + uncertainty. Enter 'q' to quit")
i : int = 0
while a != "q":

    if (i%2 == 0):
        print(ET.bcolors.OKBLUE, "\033[A")
    a = input("Value: ")
    if a != "q":
        try:
            values.append(float(a))
            uncertains.append(float(input("Uncertainty: ")))
        except:
            print(ET.bcolors.FAIL, "Not a valid input. Try again.")
    print(ET.bcolors.ENDC)
    i += 1


def sumList(input : list) -> float:
    sum : float = 0
    for i in input:
        sum += i
    return sum

def generateWeights(uncertains : list) -> list:
    weights : list = []
    for i in uncertains:
        weights.append(1/pow(i,2))
    return weights

#mittelwert
def Mittelwert(values : list, weights : list) -> float:
    fracUp : float = 0
    fracDown : float = 0
    for i in range(0, len(values)):
        fracUp += values[i] * weights[i]

    fracDown = sumList(weights)

    return fracUp / fracDown

def uIntern():
    return sqrt(1/sumList(weights))

def uExtern(values : list, weights : list, mittelwert : float) -> float:
    fracUp : float = 0
    fracDown : float = 0
    for i in range(0, len(values)):
        fracUp += pow(values[i] - mittelwert, 2) * weights[i]
    fracDown = (len(values) - 1) * sumList(weights)

    return sqrt(fracUp / fracDown)

weights : list = generateWeights(uncertains)
mittelwert : float = Mittelwert(values, weights)
internUnsi : float = uIntern()
externUnsi : float = uExtern(values, weights, mittelwert)

ET.print_category("#### MEAN RESULTS ####")
print("Mean values: ", mittelwert)
if(internUnsi > externUnsi):
    print(ET.bcolors.BOLD,">Intern uncertainty: ", internUnsi, ET.bcolors.ENDC)
    print("Extern uncertainty: ", externUnsi)
else:
    print("Intern uncertainty: ", internUnsi)
    print(ET.bcolors.BOLD,">Extern uncertainty: ", externUnsi,ET.bcolors.ENDC)


