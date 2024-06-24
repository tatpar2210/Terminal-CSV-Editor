import pandas as pd 
import csv

print("1 --For extracting middle row of CSV file")
print("2 --For fnding data in a CSV file")

do=int(input("Enter from the option above: "))

location=str(input("Give loaction of CSV file: "))
sep=str(input("Give seprator CSV file is using: "))

if do==1:
    df=pd.read_csv(location,sep)
    print(df)
    if len(df)%2==0:
        length=int(len(df)/2)
        edf=df.head(length)
    else:
        length=int((len(df)+1)/2)
        edf=df.head(length)
    print("\n")
    print("No. of data in CSV file is",len(df))
    middle_df=edf.tail(1)
    print("\n")
    print("Middle row of the CSV file is\n",middle_df)
    
elif do==2:
    csv_file=csv.reader(open(location,"r"))
    lst_csv=list(csv_file)
    print(lst_csv)
    search_for=str(input("Search for: "))
    lst_final=[]
    for i in range(0,len(lst_csv)):
        if search_for in lst_csv[i]:
            lst_final.append(lst_csv[i])
    df=pd.Series(lst_final)
    print(df)    
