import pandas as pd
location = str(input("Give Location of the CSV file: "))
sep = str(input("Provide Separator used in CSV file: "))
df = pd.read_csv(location, sep)

print(df)


def mid_row(df):
    length = len(df)
    if length % 2 == 0:
        p = length/2
        return int(p)
    else:
        p = (length+1)/2
        return int(p)


Mid_row = df.tail(mid_row(df))
print("\n")
mid_r = Mid_row.head(1)
print("Mid row is:\n", mid_r)

