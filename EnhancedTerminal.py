from random import randint
#imported from blender source code
class bcolors:
    HEADER = '\033[95m'
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