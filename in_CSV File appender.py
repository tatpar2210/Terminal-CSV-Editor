import pandas as pd

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
            # entering data acc. to its datatype
            entry = str(input(str_1.format(dict_df_head[s])))
            try:
                entry_int = int(entry)
                x[s].append(entry_int)
            except ValueError:
                x[s].append(entry)

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
    str_5 = "Sort by({}): "
    sort_by = str(input(str_5.format(dict_df_head)))
    df.sort_values(by=sort_by, ascending=True, inplace=True)
    print(df)
else:
    pass

print("\n")
# Saving of CSV file.
choice_3 = str(input("Wanna save the dataframe as a CSV_File (Y/N): "))
if choice_3 == "Y":
    location = str(input("Give a location to save: "))
    sep = str(input("Provide separator in CSV file"))
    edf = df.to_csv(location, sep, index=False)
    print("Done...Saved")
else:
    print("Ok...NOT SAVED")
