import csv

#opens the given csv file and returns it as a matrix
def open_csv(path: str) -> list:
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        return list(csv_reader)

#generate a line latex command with a delimiter § for each new line 
def generate_latex(csv_data: list) -> str:
    out_latex: str = ""

    #exit if csv empty
    if len(csv_data) == 0:
        return []
    
    else:
        #init the table
        out_latex = "§\\begin{table}[H]§  \\centering§    \\begin{tabular}{"

        #number of columns and delimiters
        latex_collumn_setup: str = "|"
        latex_collumn_name: str = "     "
        for i in range(0, len(csv_data[0])-1):
            #add a column parameter
            latex_collumn_setup += "c|"
            #add the column name
            latex_collumn_name += csv_data[0][i] + " & "

       

        #add last collumn name without the "&"
        latex_collumn_setup += "c|"
        out_latex += latex_collumn_setup
        
        latex_collumn_name += csv_data[0][len(csv_data[0])-1] + " "

        #end init
        out_latex += "}\hline§"+latex_collumn_name+"\\\\ \\hline\\hline"

        for row in range(1, len(csv_data)):
            latex_collumn_elem: str = ""
            for i in range(0, len(csv_data[row])-1):
                #adds an entry with a column delimiter
                latex_collumn_elem += csv_data[row][i] + " & "
            try:
                #adds the last entry of a row without the delimiter
                latex_collumn_elem += csv_data[row][len(csv_data[row])-1] + " "
            except:
                csv_data[row][len(row)-1]
                pass
            #close the latex table environment
            out_latex += "§     " + latex_collumn_elem + "\\\\ \\hline"
        out_latex += "§     \end{tabular}§   \label{tab:}§   \\caption{}§ \\end{table}"

        return out_latex

#Transforms a §-Latex-Format to a copiable and alligned latex command
def print_latex(latex_command: str):
    out_latex = latex_command.split("§")
    for i in out_latex:
        print(i)


print_latex(generate_latex(open_csv(
   "C:\\Users\\Tamwyn\\Documents\\Physik\\AP\\AP4\\Quantenmodelle\\AusgewerteDaten_QM1\\Rohr_ZehnReso.csv")))
