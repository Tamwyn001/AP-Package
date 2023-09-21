from random import randint
#imported from blender source code
class bcolors:
    PURPLE = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m' #back to normal
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_category(name : str)->None :
    colors = [bcolors.OKBLUE, bcolors.OKCYAN, bcolors.OKGREEN]
    print("-----[",colors[randint(0,len(colors)-1)],name, bcolors.ENDC,"]-----")
    return

def print_title(name:str)->None:
    print("_.- ", bcolors.BOLD, name, bcolors.ENDC,"-._")
    return

print(bcolors.PURPLE, "PURPLE exemple")

print(bcolors.OKBLUE, "OKBLUE exemple")

print(bcolors.OKCYAN, "OKCYAN exemple")

print(bcolors.OKGREEN, "OKGREEN exemple")

print(bcolors.WARNING, "WARNING exemple")

print(bcolors.FAIL, "FAIL exemple")

print(bcolors.ENDC, "ENDC exemple")

print(bcolors.BOLD, "BOLD exemple")

print(bcolors.UNDERLINE, "UNDERLINE exemple")