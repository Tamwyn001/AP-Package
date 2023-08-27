from math import sqrt
import ReadWriteFile as FILE
import EnhancedTerminal as ET

ET.print_category("#### USER DATAS ####")
val_a : float = float (input("Experimental value A: "))
val_a_uncertainty : float = float (input("uncertainty for value A: "))

val_b : float = float (input("Theoretical value B: "))
val_b_uncertainty : float = float (input("uncertainty for value B: "))

diff_wished : float = float(input("Wich difference between the data are you wainting for: ")) 


diff : float = abs(val_a - val_b)
diff_uncertain : float = sqrt(pow(val_a_uncertainty, 2) + pow(val_b_uncertainty, 2))

standard_deviation : float = abs(diff - diff_wished) / diff_uncertain # also called t later

#Assuming a normal distribution, the following applies: The probability that a result is
#is at most 𝑡 standard deviations away from 𝑑_erw is calculated via the normal error integral

probability_in = FILE.open_data("C:\\Users\\Tamwyn\\Documents\\Physik\\AP\\Source\\AP Package\\ProbaGaussIn.dat")

#find the probability with t in [t, probability]
to_find_t : float = round(standard_deviation, 4)
print("Standart deviation ",standard_deviation)

result : float = 1
for proba_value in probability_in:

    if proba_value[0] == to_find_t:
        result : float = proba_value[1]
        break
    
ET.print_category("#### TEST RESULTS ####")
print("The result is maximum", to_find_t, "standart deviation from wished difference with a probability of", result,".")

proba_good : float = (1-result) * 100
if proba_good > 95.0:
    color : str = ET.bcolors.OKGREEN
elif proba_good > 50.0:
    color : str = ET.bcolors.WARNING
else:
    color : str = ET.bcolors.FAIL
print("Your result (A) matches with",color, proba_good, ET.bcolors.ENDC , "% the theoretical value (B)!")