import csv
import pandas as pd
location=str(input("Give loacation of the CSV file: "))
seps=str(input("Mention the seprator which CSV file is having: "))
df=pd.read_csv(location,sep=seps)
print(df)
edf=df.head(1)
list_edf=list(edf)

def search():
    csv_file=csv.reader(open(location,"r"))            
    search_for=str(input("Search here: "))
    for row in csv_file:
        if search_for in row[search_by]:
            print(row)
        else:
            print("\n")
            print("Given data doesn't exist in the file !!")
            break

print("\n")
for i in range(0,len(list_edf)):
    srch_by=" --Search By {}: "
    print(i,srch_by.format(list_edf[i]))

print("\n")    
search_by=int(input("Search by(GIVE INDEX HERE): "))

search()
