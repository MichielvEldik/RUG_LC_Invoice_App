import csv
headerrow = ["ID", "name", "address", "#_apples", "$_apples", "#_oranges",
"$_oranges", "$_total_amount", "VAT (15%)", "$_net_total", "date"]

a = ""
def function_filename(a):
    while True:
        print("\n")
        print("---------------------------------------------------------------------")
        print("| Please specify the file name.                                      |\n"
              "| The file name will only include lowercase alphabetical characters. |")
        print("---------------------------------------------------------------------")
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

def function_happy (a):
            while True:
                print("\n")
                print("------------------------------------------------------")
                print("| Are you happy with this file name?                 |\n"
                      "| Answer 'yes' or 'no'.                              |")
                print("------------------------------------------------------")
                print("\n")
                happy = input("Answer:")
                if happy == "yes":
                    print("It sounds good indeed!")
                    return happy

                elif happy == "no":
                    return happy
                else:
                    print("This is not a valid answer, please try again.")
print("\n")
print("------------------------------------------------------------------------------------")
print("| Welcome to program 1.                                                            | \n"
      "| This program creates csv files with a name of your choice.                       | \n"
      "| A csv file created with this app will always include an initial list of headers. |")
print("------------------------------------------------------------------------------------")
print("\n")
print(headerrow)

while True:
    print("\n")
    print("-------------------------------------")
    print("| Do you want to create a new file? |\n"
          "| Type 'yes' or 'no'                |")
    print("-------------------------------------")
    print("\n")
    answer_1 = input("Answer:")
    lowercase_answer_1 = str.lower(answer_1)
    if lowercase_answer_1 == "yes":
        name = function_filename(a)
        if function_happy(a) == "yes":
            name_csv = name + ".csv"
            #print("Your file name is:", name_csv, ".csv")
            print("\n")
            print("--------------------------------------------------------")
            print("| Do you want to save this file name to this directory? |\n"
                  "| Type 'yes' or 'no'                                    | ")
            print("--------------------------------------------------------")
            print("\n")
            save = input("Answer:")
            if save == "yes":
                with open(name_csv, 'w', newline='') as csv_file:
                    b = csv.writer(csv_file, delimiter=',')
                    b.writerow(headerrow)
                print(name_csv,"has been saved to this directory.")
                break
            else:
                print("Ok. Let's try this again.")
        else:
            print("Let's try this again.")
    elif lowercase_answer_1 == "no":
        print("We will proceed to quit the application.")
        break
    else:
        print("This is not a valid answer, please try again.")