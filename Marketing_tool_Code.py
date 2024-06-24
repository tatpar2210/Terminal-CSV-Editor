# Marketing Tool.........

import pandas as pd
import socket
import sys
import time

print("Add --To add data in a file or create new one")
print("Update --To update product list as a CSV file")
print("Bill --Billing")
print("Chat --Chat with Server room")
print("Quit --To exit Marketing Tool\n")

# Taking input what user wanna do
choice = str(input("What u wanna do: "))

# To add data(making of CSV file).
if choice == "Add":
    print("\n")
    print("CSV --add through CSV_file")
    print("New --To make a new product list \n")

    # How user wanna input data like, in a existing file or by creating a new file.
    choice_2 = str(input("By what u wanna add: "))

    # Creating a new csv with pre-defined column names for now.
    if choice_2 == "New":
        columns = int(input("Give no. of columns to be created: "))
        str_1 = "Name of Column {} = : "
        # Empty Dictionary for CSV file
        dct_1 = {}
        # Empty list of sub lists of dictionary fields
        lst = []
        for i in range(0, columns):
            # Taking column name from the user
            col_name = str(input(str_1.format(i)))
            # Giving name to the list for the dictionary
            lst_name = str(i)
            # Auto-formation of list for dictionary
            lst_name = []
            # Auto-formation of dictionary
            z = {col_name: lst_name}
            # Adding all z in empty dictionary x
            dct_1.update(z)
            # Adding every lst_name as sub list in empty list y
            lst.append(lst_name)
        # These lst and dct_1 are only to get field names and their respective list.

        # Getting field name from dct_1
        field_no = list(dct_1.keys())

        # Final and main empty dictionary.
        dct_2 = {}

        data_length = int(input("How many data to be entered in CSV file:  "))
        str_2 = "Feed data in {}: "
        for s in range(0, data_length):
            for a in range(0, len(field_no)):
                # ??
                if field_no[a] == str(field_no[a]):
                    entry = str(input(str_2.format(field_no[a])))
                    # entering data acc. to its datatype
                    if type(entry) == str:
                        lst[a].append(entry)
                    elif type(entry) == int:
                        int_entry = int(entry)
                        lst[a].append(int_entry)
                    # Saving final fields in main dictionary with their respective list.
                    z = {field_no[a]: lst[a]}
                dct_2.update(z)
                a += 1
            # print(dct_2)
            print("\n")
            s += 1
        # converting final dictionary to Dataframe.
        df = pd.DataFrame(dct_2)
        print("Showing result for created CSV file...")
        print(df, "\n")

        # Sorting of CSV (Optional)
        sort_ch = str(input("Wanna do sorting in csv file(Y/N): "))
        if sort_ch == "Y":
            sort_by = str(input("Sort by(Give parameters, if more than 1 separate them by coma's: "))
            df.sort_values(by=sort_by, ascending=True, inplace=True)
        else:
            pass

        # Saving of CSV file.
        print("If Yes then, save with name (Eg:/home/linux/code/Billing.csv)")
        choice_3 = str(input("Wanna save the dataframe as a CSV_File (Y/N): "))
        if choice_3 == "Y":
            location = str(input("Give a location to save: "))
            sep = str(input("Provide separator in CSV file: "))
            edf = df.to_csv(location, sep, index=False)
            print("Done...Saved")
        else:
            pass
        print("############################################################################")
    # Adding in existed CSV file.
    elif choice_2 == "CSV":
        location = str(input("Enter the CSV file location: "))
        sep = str(input("Provide separator used: "))
        csv_f = pd.read_csv(location, sep)
        df = pd.DataFrame(csv_f)
        # Original Dataframe
        print(df)
        dict_df = dict(df)
        # Name of columns of dictionary
        dict_df_head = list(dict_df.keys())

        # will contain list of column values as sub list in list.
        x = []
        for i in range(0, len(dict_df_head)):
            lst = list(dict_df.get(dict_df_head[i]))
            x.append(lst)
        # print(x)

        data_strength = int(input("How many more data to be entered: "))
        str_1 = "Add in {}: "

        # Final dictionary.
        dict_2 = {}
        for a in range(0, data_strength):
            for s in range(0, len(dict_df_head)):
                if dict_df_head[s] == dict_df_head[s]:
                    entry = str(input(str_1.format(dict_df_head[s])))
                    # entering data acc. to its datatype
                    if type(entry) == str:
                        x[s].append(entry)
                    elif type(entry) == int:
                        int_entry = int(entry)
                        x[s].append(int_entry)
                    z = {dict_df_head[s]: x[s]}
                    dict_2.update(z)
                s += 1
            print("\n")
            a += 1

        df = pd.DataFrame(dict_2)
        # Updated Dataframe
        print(df, "\n")

        # Sorting of CSV (Optional)
        sort_ch = str(input("Wanna do sorting in csv file(Y/N): "))
        if sort_ch == "Y":
            sort_by = str(input("Sort by(Give parameters, if more than 1 separate them by coma's: "))
            df.sort_values(by=sort_by, ascending=True, inplace=True)
        else:
            pass
        # Saving of CSV file.
        choice_3 = str(input("Wanna save the dataframe as a CSV_File (Y/N): "))
        if choice_3 == "Y":
            location = str(input("Give a location to save: "))
            sep = str(input("Provide separator in CSV file"))
            edf = df.to_csv(location, sep, index=False)
            print("Done...Saved")
        else:
            print("Ok...NOT SAVED")
        print("############################################################################")
# Doing modification in CSV file like delete or add data in it.
elif choice == "Update":
    location = str(input("Enter the CSV file location: "))
    sep = str(input("Provide separator used: "))
    csv_file = pd.read_csv(location, sep)
    print("1 --Update any value or string")
    print("2 --Delete data ")

    choice_1 = int(input("What u wanna do: "))

    # Updating  data in CSV file
    if choice_1 == 1:
        dct_1 = dict(csv_file)
        dct_1_keys = list(dct_1.keys())

        # Making of empty dictionary to bring dataframe dictionary to normal dictionary,
        # otherwise will get an error.
        dct_2 = {}

        # ???????
        for a in range(0, len(dct_1_keys)):
            s = {dct_1_keys[a]: list(dct_1.get(dct_1_keys[a]))}
            # adding up dct_1(CSV file dictionary) elements to dct_2(normal dictionary).
            dct_2.update(s)
        # print(dct_2)

        dct_2_keys = list(dct_2.keys())
        # print(dct_2_keys)

        choice_2 = ""
        str_1 = "Change can be done in {} select any one: "
        while choice_2 != "Done":
            # getting product_name list to show up in input string.
            print("If finished type [Done]")
            choice_2 = str(input(str_1.format(dct_2_keys)))
            dct_3 = {}

            for i in range(0, len(dct_2_keys)):
                # matches user input with dictionary field name in which changes to be made.
                if choice_2 == dct_2_keys[i]:
                    print(csv_file)

                    # What element user wanna changes.
                    index = int(input("Give index that to be changed="))

                    # Assigning variable for the position of the element in changing field.
                    change_at = dct_2.get(dct_2_keys[i])[index]
                    # print(change_at)
                    # Changing of elements
                    str_2 = "Change {} by="
                    if type(change_at) == str:
                        dct_2.get(dct_2_keys[i])[index] = str(input(str_2.format(change_at)))

                    elif type(change_at) == int:
                        dct_2.get(dct_2_keys[i])[index] = int(input(str_2.format(change_at)))

                    else:
                        "Invalid Data Type!!"
                x = {dct_2_keys[i]: list(dct_2.get(dct_2_keys[i]))}
                # Fully-Final dictionary##
                i += 1
                dct_3.update(x)
        print("\n")
        # print(dct_3)
        # print(dct_2.get(dct_2_keys[i]))

        df_2 = pd.DataFrame(dct_3)

        # Sorting of CSV (Optional)
        sort_ch = str(input("Wanna do sorting in csv file(Y/N): "))
        if sort_ch == "Y":
            sort_by = str(input("Sort by(Give parameters, if more than 1 separate them by coma's: "))
            df_2.sort_values(by=sort_by, ascending=True, inplace=True)
        else:
            pass

        # Saving of dataframe to csv
        str_3 = "Wanna over-right to {} or to save with different name(Y/N): "
        save = str(input(str_3.format(location)))
        if save == "Y":
            csv_2 = df_2.to_csv(location, sep, index=False)
        elif save == "N":
            location_2 = str(input("Give new location to save updated CSV: "))
            sep_2 = str(input("Provide separator="))
            csv_2 = df_2.to_csv(location_2, sep_2, index=False)
        else:
            print("Invalid Input!!")

        print("Saved...ThankYou")
        print("############################################################################")
        # To delete data in CSV file.

    elif choice_1 == 2:
        print(csv_file)
        print("\n")
        print("1 --To delete complete Column ")
        print("2 --To delete specific rows")
        choice_2 = int(input("What u wanna delete from the given options above"))

        x = []

        if choice_2 == 1:
            col_label_del = ""
            while col_label_del != "Done":
                col_label_del = str(input("Give Column name from above dataframe: "))

                if col_label_del == "Done":
                    pass
                else:
                    x.append(col_label_del)
                    print(x)
                print("If finished type [Done]")
            # Axis=1 means columns.
            csv_file.drop(x, axis=1, inplace=True)
            print(csv_file)

        elif choice_2 == 2:
            index_csv_del = ""
            while index_csv_del != "Done":
                index_csv_del = str(input("Give row no./index to be deleted="))

                if index_csv_del == "Done":
                    pass
                else:
                    x.append(int(index_csv_del))
                    print(x)
                    print("If finished type [Done]")
            # Axis=0 means row.
            csv_file.drop(x, axis=0, inplace=True)
            print("\n")
            print(csv_file)

        # Sorting of CSV (Optional)
        sort_ch = str(input("Wanna do sorting in csv file(Y/N): "))
        if sort_ch == "Y":
            sort_by = str(input("Sort by(Give parameters, if more than 1 separate them by coma's: "))
            csv_file.sort_values(by=sort_by, ascending=True, inplace=True)
        else:
            pass

        # Saving of csv file
        choice_3 = str(input("Wanna save the dataframe as a CSV_File (Y/N): "))

        if choice_3 == "Y":
            location = str(input("Give a location to save: "))
            sep = str(input("Provide separator in CSV file"))
            edf = csv_file.to_csv(location, sep, index=False)
            print("Done...Saved")
        else:
            pass
        print("############################################################################")
# Start billing
elif choice == "Bill":
    print("Let's start the goddamn business!!")
    location = str(input("Give location of Product_list: "))
    sep = str(input("Give separator used: "))
    df = pd.read_csv(location, sep)

    dict_df = dict(df)
    name = list(dict_df.get("Product_Name"))
    code = list(dict_df.get("Product_Code"))
    price = list(dict_df.get("Product_Price"))
    stock = list(dict_df.get("Product_in_stock"))
    print(code)
    print("\nProduct List")
    print(df)
    print("\n")
    prd_code = ""
    x = []
    while prd_code != "Done":
        prd_code = str(input("Scan the bar code or Feed the code manually from above: "))
        if "Done" not in prd_code:
            for a in range(0, len(code)):
                if prd_code == str(code[a]):
                    x.append(prd_code)
            print(x)
            print("Type Done --if done listing of selling products")
        else:
            # Price list
            p = []
            print("\nCode         Product         Price")
            for i in range(0, len(x)):
                # Element of list x list
                c = int(x[i])
                # Index at which a particular element in x list is in present in code list
                y = code.index(c)
                #
                p.append(price[y])
                #
                str_1 = "{}        {}      {}"
                print(str_1.format(code[y], name[y], price[y]))
                #
                i += 1
            net_amt = sum(p)
            print("NET AMOUNT=", net_amt)
            rec = int(input("Amt Received: "))

            while rec < net_amt:
                print("U need more i.e=", net_amt - rec)
                net_amt = net_amt - rec
                rec = int(input("Enter money received now="))
            else:
                print("Return=", rec - net_amt)
            print("ThankYou")
    print("############################################################################")
elif choice == "Chat":
    s = socket.socket()
    host = input(str("Enter the hostname of the server:"))
    port = 8080
    s.connect((host, port))
    print("Connected to chat server")
    while 1:
        incoming_message = s.recv(1024)
        incoming_message = incoming_message.decode()
        print(" Server :", incoming_message)
        message = input(str(">>"))
        message = message.encode()
        s.send(message)
        print(" message has been sent...")
        print("")
else:
    print("Invalid input!!")
