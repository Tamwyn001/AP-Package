from math import sqrt
import ReadWriteFile as FILE
import EnhancedTerminal as ET
print("\n")
ET.print_category("#### USER DATAS ####")
val_a : float = float (input("Experimental value A: "))
val_a_uncertainty : float = float (input("uncertainty for value A: "))

val_b : float = float (input("Theoretical value B: "))
val_b_uncertainty : float = float (input("uncertainty for value B: "))

diff_wished : float = float(input("Wich difference between the data are you wainting for: ")) 


diff : float = abs(val_a - val_b)
diff_uncertain : float = sqrt(pow(val_a_uncertainty, 2) + pow(val_b_uncertainty, 2))

standard_deviation : float = abs(diff - diff_wished) / diff_uncertain # also called t later

#Assuming a normal distribution, the following applies: The probability that a result isk
#is at most 𝑡 standard deviations away from 𝑑_erw is calculated via the normal error integral

probability_in = FILE.open_data("C:\\Users\\Tamwyn\\Documents\\Physik\\AP\\Source\\AP Package\\Source\\ProbaGaussIn.dat")

#find the probability with t in [t, probability]
to_find_t : float = round(standard_deviation, 4)
print("Standart deviation ",standard_deviation)

result : float = 1
for proba_value in probability_in:

    if proba_value[0] == to_find_t:
        result : float = proba_value[1]
        break

print("\n")
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
print("\n")


ET.print_category("##### LATEX TEXT #####")
print(ET.bcolors.OKCYAN,"\paragraph{Signifikanztest}$~$\\\\")
print("Wir führen zunächst einem Signifikanztest, um die Werte mit der Theorie zu vergleichen.")
print("\\begin{table}[H] \n    \\centering \n    \\begin{tabular}{|c|c|c|c|c|c|}\\hline")
print("      Werte A & Werte B & Differenz $d$ & $d_{erw}$ & $t$ & Übereinstimmung \\\\\\hline")
print("      \\num{", val_a,"(", val_a_uncertainty, ")} & \\num{" , val_b, "(", val_b_uncertainty, ")} & \\num{", diff , "(", diff_uncertain, ")} & \\num{" , diff_wished , "} & \\num{" , standard_deviation ,"} & \\num{" , round(proba_good, 3),"}\%", "\\\\\\hline")
print("    \\end{tabular}\n    \\caption{Der Signifikanztest }\n    \\label{tab:SignTest_}\n \end{table}")

null_hyp : str = "[NULLHYPOTHESE]."
if diff_wished == 0:
     null_hyp = "die Werte übereinstimmen."

print("In das Tabelle \\ref{tab:SignTest_} kann man die wichtigen Größen des Testes lesen. Die Nullhypothese ist, dass", null_hyp ,"Laut der Normalverteilung ist die Wahrscheinlichkeit, dass die Differenz $d$ meinstens $t$ Standartabweichung von der erwartet Differenz $d_{erw}$ liegt, ist mittels der Gauss'sche Fehlerintegral berechnet. Wir erhalten eine Übereinstimmung von", round(proba_good,3), "\% zwischen die Werten.\\newline", ET.bcolors.ENDC)