import pandas as pd

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
            # entering data acc. to its datatype.
            entry = str(input(str_2.format(field_no[a])))
            try:
                entry_int = int(entry)
                lst[a].append(entry_int)
            except ValueError:
                lst[a].append(entry)

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
    str_4 = "Sort by({}): "
    sort_by = str(input(str_4.format(field_no)))
    df.sort_values(by=sort_by, ascending=True, inplace=True)
    print(df)
else:
    pass

# Saving of CSV file.
print("\nIf Yes then, save with name (Eg:/home/linux/code/Billing.csv)")
choice_3 = str(input("Wanna save the dataframe as a CSV_File (Y/N): "))
if choice_3 == "Y":
    location = str(input("Give a location to save: "))
    sep = str(input("Provide separator in CSV file: "))
    edf = df.to_csv(location, sep, index=False)
    print("Done...Saved")
else:
    pass
