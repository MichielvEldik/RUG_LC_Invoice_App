import csv
import sys

def function_files_display():
    files = []
    import os
    current_directory_path = os.path.abspath(os.getcwd())
    for r, d, f, in os.walk(current_directory_path):
        for file in f:
            if '.csv' in file:
                files.append(file)
    #print(files)
    #files = display
    print("\n")
    #print("csv files in the current working directory: ")
    #for f in files:
        #print(f)
        #display = f
    return(files)

def function_file_select (display):
    while True:

        print("Available files in this directory:")
        print("\n")
        print(*display, sep='\n')
        print("\n")
        print("-----------------------------------------------------------------")
        print("| Please enter the name of the csv file you want to access.      |\n"
              "| There is no need to add '.csv' to your answer.                 |\n"
              "| However, be careful with upper/lowercase letters!              |")
        print("-----------------------------------------------------------------")
        print("\n")
        file_select = input("Answer:")
        file_select_csv = file_select + ".csv"
        with open(file_select_csv, newline= '') as f:
            reader = csv.reader(f)
            data1 = list(reader)
        biglist = data1
        print("\n")
        print("Current file:", file_select_csv)
        print("-----------------------------------------------------------------")
        print("| Do you want to view the content of this file before continuing?|\n"
              "| Type 'yes' to view content.                                    |\n"
              "| Type anything to skip this part.                               |")
        print("-----------------------------------------------------------------")
        print("\n")
        view = input("Answer:")
        if view == "yes":
            print("Current file looks as follows:\n")
            print(*biglist, sep='\n')
        else:
            print("OK. We'll continue.")
        print("\n")
        print("Current file:", file_select_csv)
        print("----------------------------------------------------------------------------------------")
        print("| Would you like to use this file to create a session list or access a different file? |\n" 
              "| Type 'yes' to use this file.                                                         |\n"
              "| Type anything to access a different file.                                            |")
        print("----------------------------------------------------------------------------------------")
        print("\n")
        yes_no = input("Answer:")
        if yes_no == "yes":
            break
        else:
            print("Ok. Let's try it again!")
    return (file_select_csv)

def function_file_load (files_select_csv):
    with open(file_select_csv, newline='') as f:
        reader = csv.reader(f)
        data1 = list(reader)
        biglist = data1
    return (biglist)


a = ""
def function_filename(a):
    while True:
        print("\n")
        print("----------------------------------------------------------------------")
        print("| The final invoice will be saved as a txt file.                     |\n"
              "| Please specify a name for the new txt file.                        |\n"
              "| The file name will only include lowercase alphabetical characters. |")
        print("----------------------------------------------------------------------")
        print("\n")
        name_file = str(input("File name:"))
        lowercase_file = str.lower(name_file)
        for letter in lowercase_file:
            if str.isalpha(letter) == True:
                a += letter
        if len(a) < 1:
            print("You did not write anything, please try again.")
        else:
            print("Your csv file name is:", a)
            return(a)

def function_happy(a):
    while True:
        print("\n")
        print("--------------------------------------")
        print("| Are you happy with this file name? |\n"
              "| Answer 'yes' or 'no'               |")
        print("--------------------------------------")
        print("\n")
        happy = input("Answer")
        if happy == "yes":
            print("\n")
            print("It sounds good indeed!")
            return happy

        elif happy == "no":
            return happy
        else:
            print("\n")
            print("This is not a valid answer, please try again.")


print("\n")
print("--------------------------------------------------------------------------------------------------")
print("| Welcome to program 3.                                                                          |\n"
      "| This program allows you to produce a 'real' comprehensible invoice from the invoice data file. |\n"
      "| This is done by turning it into a structured text file.                                        |")
print("--------------------------------------------------------------------------------------------------")
print("\n")
print("Structure-wise this program is similar to program 2. \n"
      "First, you get to pick out the csv file of your choice (within this directory. \n"
      "Once you've viewed it and made your choice, you get to pick the invoice you want to turn into a text file with a name of your choice.\n"
      "The text file will then be saved to this directory.")



display = (function_files_display())
file_select_csv = function_file_select(display)
biglist = function_file_load(file_select_csv)



while True:
    print("The list for the current session now looks as follows:")
    print(*biglist, sep='\n')
    print("\n")
    print("-----------------------------------------------------------------------------------------")
    print("| Please specify for which element in the invoice list you want to create a txt invoice. |\n"
          "| You can specify by typing the ID number.                                               |")
    print("------------------------------------------------------------------------------------------")
    print("\n")
    id_number = int(input("ID number:"))
    print("\n")
    print("This is the invoice you selected.")
    print("\n")
    print(biglist[id_number])
    print("\n")
    print("----------------------------------------------")
    print("| Do you wish to continue with this invoice? | \n"
          "| answer 'yes' or 'no'                       |")
    print("----------------------------------------------")
    print("\n")
    cont = input("Answer:")
    if cont == "yes":
        session_list = (biglist[id_number])
        id = session_list[0]
        name = session_list[1]
        address = session_list[2]
        quantity_apples = session_list[3]
        price_apples = session_list[4]
        quantity_oranges = session_list[5]
        price_oranges = session_list[6]
        total_amount = session_list[7]
        vat_amount = session_list[8]
        net_total = session_list[9]
        date = session_list[10]

        name = function_filename(a)
        if function_happy(a) == "yes":
            name_txt = name + ".txt"
            print("\n")
            print("---------------------------------------------- ---")
            print("| Are you sure you want to save the invoice txt? |\n"
                  "| Answer 'yes' or 'no' please.                   |")
            print("--------------------------------------------------")
            print("\n")
            save = input("Answer:")
            if save == "yes":
                with open(name_txt, "w") as myfile:
                    myfile.write("\n")
                    myfile.write("General information.")
                    myfile.write("\n")
                    myfile.write("---------------------------------------------------------------- \n")
                    myfile.write("Invoice ID: ")
                    myfile.write(id)
                    myfile.write("\n")
                    myfile.write("Name company: ")
                    myfile.write(name)
                    myfile.write("\n")
                    myfile.write("Invoice date: ")
                    myfile.write(date)
                    myfile.write("\n")
                    myfile.write("\n")
                    myfile.write("\n")
                    myfile.write("Specific order information.")
                    myfile.write("\n")
                    myfile.write("---------------------------------------------------------------- \n")
                    myfile.write("Quantity of apples ordered: ")
                    myfile.write(quantity_apples)
                    myfile.write("\n")
                    myfile.write("Total $ amount for apples: ")
                    myfile.write(price_apples)
                    myfile.write("\n")
                    myfile.write("Quantity of oranges ordered: ")
                    myfile.write(quantity_oranges)
                    myfile.write("\n")
                    myfile.write("Total $ amount for oranges: ")
                    myfile.write(price_oranges)
                    myfile.write("\n")
                    myfile.write("\n")
                    myfile.write("\n")
                    myfile.write("Gross $ amount & VAT (15%) amount")
                    myfile.write("\n")
                    myfile.write("---------------------------------------------------------------- \n")
                    myfile.write("Gross $ amount :")
                    myfile.write(total_amount)
                    myfile.write("\n")
                    myfile.write("Gross VAT (15%) amount :")
                    myfile.write(vat_amount)
                    myfile.write("\n")
                    myfile.write("Net $ amount :")
                    myfile.write(net_total)
                    myfile.write("\n")
                    myfile.write("\n")
                    myfile.write("---------------------------------------------------------------- \n")
                print("\n")
                print("The file has been saved successfully!")
                print("\n")
                sys.exit(0)
            else:
                print("\n")
                print("Ok. Let's try this again.")
                print("\n")
    else:
        print("\n")
        print("Ok. Let's try this again.")
        print("\n")




