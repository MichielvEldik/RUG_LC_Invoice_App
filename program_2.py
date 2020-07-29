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
            print("\n")
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


def function_add_id (biglist):
    factuur = []
    if len(biglist) <=1:
        newid = 1
    if len(biglist) > 1:
        newid = 1 + int(biglist[-1][0])

    factuur.append(newid)
    return(factuur)

def function_add_company_address (factuur):
    print("\n")
    print("-----------------------------------")
    print("| What's the name of the company? |")
    print("-----------------------------------")
    print("\n")
    company = input("Name:")
    factuur.append(company)
    truthlist = []
    for i in biglist:
        tflist = (i[1]) == company
        truthlist.append(tflist)
        # print(tflist)
        # print(truthlist)
    # print(any(truthlist))
    anytruthlist = (any(truthlist))

    if anytruthlist:
        print("\n")
        print("This company is already in our directory. The address will be updated automatically.")
        print("\n")
        index = (truthlist.index(True))
        indexname = biglist[index][2]
        factuur.append(indexname)
    else:
        print("\n")
        print("This company is new to our directory.")
        print("\n")
        print("-----------------------")
        print("| What is the address? |")
        print("-----------------------")
        print("\n")
        new_adress = input("Address:")
        print("\n")
        factuur.append(new_adress)

    return(factuur)

def function_item_info(factuur):
    print("\n")
    print("Now, we will ask a few questions about the order.")
    while True:
        print("---------------------------------------")
        print("| Quantity of apples ($4) purchased. |")
        print("---------------------------------------")
        print("\n")
        apples = (input("Answer:"))
        if apples.isdigit()==False:
            print("\n")
            print("Invalid answer. Please only use digits")
        else:
            apples = int(apples)
            factuur.append(apples)
            price_apples = apples * 4
            print("\n")
            print("That's equal to $", price_apples, "worth of apples")
            factuur.append(price_apples)
            print("\n")
            break
    while True:
        print("---------------------------------------")
        print("| Quantity of oranges ($2) purchased. |")
        print("---------------------------------------")
        print("\n")
        oranges = (input("Answer:"))
        if oranges.isdigit() == False:
            print("\n")
            print("Invalid answer. Please only use digits")
        else:
            oranges = int(oranges)
            factuur.append(oranges)
            price_oranges = oranges * 2
            print("\n")
            print("That's equal to $", price_oranges, "worth of oranges")
            factuur.append(price_oranges)
            print("\n")
            break

    total_amount = price_oranges + price_apples
    vat = float(total_amount)*0.15
    net_amount = total_amount + vat
    print("The total amount spent is $", total_amount)
    print("The VAT amount is $", vat)
    print("The net amount is $", total_amount,"+",vat, "=", net_amount)
    factuur.append(total_amount)
    factuur.append(vat)
    factuur.append(net_amount)

    return (factuur)

def function_add_date(factuur):
    print(factuur)
    print("\n")
    print("-----------------------------------------------------------------------------")
    print("| We can add today's date to the invoice but you may also enter it manually. | \n"
          "| Type 'yes' if you want us to automatically add today's date.               | \n"
          "| Type anything if you want to add the date manually.                        | ")
    print("-----------------------------------------------------------------------------")
    print("\n")
    which_date = input("Answer:")
    if which_date == "yes":
        from datetime import date
        today = str(date.today())
        factuur.append(today)
        print("\n")
        print("Today's date has been added to the invoice")
    else:
        while True:
            print("\n")
            print("--------------------------------------------------------")
            print("| What's the year? (please answer in four digits only) |")
            print("--------------------------------------------------------")
            print("\n")
            year = input("Answer:")
            if len(year) != 4 or year.isdigit() == False:
                print("\n")
                print("Answer is invalid, please try again.")
            else:
                print("\n")
                print("--------------------------------------------------------")
                print("| What's the month? (please answer in two digits only) |")
                print("--------------------------------------------------------")
                print("\n")
                month = input("Answer:")
                if len(month) != 2 or month.isdigit() == False:
                    print("\n")
                    print("Answer is invalid, please try again.")
                else:
                    print("\n")
                    print("--------------------------------------------------------")
                    print("| What's the day? (please answer in two digits only)   |")
                    print("--------------------------------------------------------")
                    print("\n")
                    day = input("Answer:")
                    if len(day) != 2 or day.isdigit() == False:
                        print("\n")
                        print("Answer is invalid, please try again.")
                    else:
                        listy = year + "-" + month + "-" + day
                        factuur.append(listy)
                        print("\n")
                        print("the date", listy, "has been added to your invoice")
                        break
    return (factuur)


def function_return_appendedbiglist(biglist, function_add_id, function_add_company_address, function_item_info, function_add_date):
    function_add_id(biglist)
    factuur = function_add_id(biglist)
    print("\n")
    print("Invoice ID number is", factuur)

    function_add_company_address(factuur)
    print("Current file:", file_select_csv)
    print("Invoice so far:")
    print("\n")
    print("[ID, Name, Address]")
    print(factuur)

    function_item_info(factuur)
    print("\n")
    print("Your invoice data including item info:")
    print("\n")
    print("[ID, Name, Address, #_apples, $_apples, #_oranges, $_ranges, $_total_amount, VAT(15%), $_net_total]")

    function_add_date(factuur)
    print("\n")
    # print("Your invoice data including the date:")
    #print("[ID, Name, Address, #_apples, $_apples, #_oranges, $_ranges, $_total_amount, VAT(15%), $_net_total, date]")
    #print(factuur)

    return factuur

def function_save (file_select_csv, biglist):
    print("\n")
    print("------------------------------------------------------")
    print("| Would you like to save the data file? ('yes'/'no') |")
    print("------------------------------------------------------")
    print("\n")
    safe = str(input("Would you like to save the data file?"))
    if safe == "yes":
        with open(file_select_csv, 'w', newline='') as fp:
            a = csv.writer(fp, delimiter=',')
            data = biglist
            a.writerows(data)
        print("Your invoice(s) have been added to the existing file.")
        print("\n")
    else:
        print("\n")
        print("That's fine. We'll return to the main menu.")



print("\n")
print("------------------------------------------------------------------------------------------------------------------------------------")
print("| Welcome to program 2.                                                                                                            | \n"
      "| This application lets you add the data of an invoice to a csv file of your choice within the working directory of this Py. file! |")
print("------------------------------------------------------------------------------------------------------------------------------------")
print("\n")
print("This program works with the following steps: \n\n"
      "1. Select an existing csv file from this working directory (If no csv files are present, please use program 1 to create a new file.)\n"
      "2. View the selected file and decide if you want to use this file for the current session or access a different file. \n"
      "3. Once you made your decision, the list contained in the csv will be used as the list for the current session. \n"
      "4. You will be taken into the 'main menu', from here you can add new invoices to the session list, save the session to the initial csv file, or terminate the session. \n\n"
      "* Please note. Once you arrive at the main menu, you can't go back to steps 1 or 2. If you change your mind, terminate the session and restart the program.")
display = (function_files_display())
file_select_csv = function_file_select(display)
biglist = function_file_load(file_select_csv)
print("\n")
print("The list for the current session now looks as follows:")
print("\n")
print(*biglist, sep='\n')

while True:
    print("\n")
    print("Current file:", file_select_csv)
    print("--------------------------------------------------------------------------------------")
    print("| Welcome to the main menu. From here you can do three things.                        |\n"
          "| You can add an(other) invoice --> type 'yes'                                        |\n"
          "| You can save all of the invoices that were created in this session --> type 'save'  |\n"
          "| You can terminate the session --> type anything                                     |\n"
          "| You can view the current session's list --> type 'view'                             |")
    print("--------------------------------------------------------------------------------------")
    print("\n")
    answer = str(input("Answer:"))
    while True:
        if answer == "yes":
            factuur_new = function_return_appendedbiglist(biglist, function_add_id, function_add_company_address,
                                                          function_item_info, function_add_date)
            print("The new invoice now looks as follows:")
            print("\n")
            print(
                "[ID, Name, Address, #_apples, $_apples, #_oranges, $_ranges, $_total_amount, VAT(15%), $_net_total, date]")
            print(factuur_new)
            print("\n")
            print("----------------------------------------------------------------------")
            print("| Are you happy with the invoice or do you want to start over again? |\n"
                  "| Type 'yes' to confirm and add invoice to session list.             |\n"
                  "| Type 'no' to start from scratch.                                   |")
            print("----------------------------------------------------------------------")
            print("\n")
            add_no = input("Answer:")
            if add_no == "yes":
                print("\n")
                print("alright, it will be added to the session list.")
                biglist.append(factuur_new)
                print("\n")
                print("The list for this session has been updated and now looks as follows:")
                print("\n")
                print(*biglist, sep='\n')
                break
            elif add_no == "no":
                print("\n")
                print("Ok. let's start again from scratch.")
            else:
                print("\n")
                print("That was an invalid answer.")

        elif answer == "save":
            print("\n")
            print("We will now move on to save the file!")
            function_save(file_select_csv, biglist)
            print("\n")
            print("file has been saved successfully.")
            break
        elif answer == "view":
            print("\n")
            print("The current session list looks as follows.")
            print("\n")
            print(*biglist, sep='\n')
            break
        else:
            print("Goodbye. See you again soon!")
            sys.exit(0)





