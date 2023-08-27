def open_data(path : str) -> list :
    out_data = []
    out_it_line = []
    with open(path,'r') as entry_file:
        lines: list = entry_file.readlines() #raw data in a list of a string for each lime

        for line in lines:
            ordered_line : list = line.strip().split(" ") #removes the \n and split each entry of the line in a list of str
            out_it_line = []
            #print(ordered_line)
            for value in ordered_line: #convert all data from a line into a float
                out_it_line.append(float(value))
            out_data.append(out_it_line) #add the line to the end list
    return out_data

def write_data_to_file(path : str, data: list) -> None: #send [['2.3','3.4'], ['2.3','3.4']]
    to_write : str = ""
    to_write_line : str = ""
    f_out = open(path, 'w')
    for line in data:
        for value in line:
            to_write_line += str(value) + " "
        to_write += to_write_line + "\n"
        to_write_line = ""

    f_out.write(to_write)
    f_out.close()