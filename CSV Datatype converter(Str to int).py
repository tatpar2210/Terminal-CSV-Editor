import pandas as pd

location = str(input("Provide location of CSV file: "))
sep = str(input("Provide separator used in CSV file: "))

dct = pd.read_csv(location, sep)

print(dct, "\n")
fields = list(dct.keys())

print("Columns in CSV file= ", fields)
col_to_convert = str(input("Which column to convert in only int type: "))

lst = list(dct.get(col_to_convert))

# Converting data type
output_lst = []
for i in range(0, len(lst)):
    output = int(lst[i])
    output_lst.append(output)

# Replacing Converted Column
df = dct.replace({col_to_convert: output_lst})
print("Done...")
print("\n")

# Sort
sort_choice = str(input("Wanna Sort CSV (Y/N): "))
if sort_choice == "Y":
    str_1 = "Sort by from({}): "
    sort_col = str(input(str_1.format(fields)))
    df.sort_values(by=sort_col, inplace=True)
    print(df)
else:
    print(df)

# Saving CSV
location_2 = str(input("Provide location of CSV file: "))
sep_2 = str(input("Provide separator used in CSV file: "))

df_save = df.to_csv(location_2, sep_2, index=False)
print("Done...Saved")
