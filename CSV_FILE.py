import pandas as pd 
import csv

print("1 --For extracting middle row of CSV file")
print("2 --For fnding data in a CSV file")

do=int(input("Enter from the option above: "))

location=str(input("Give loaction of CSV file: "))
sep=str(input("Give seprator CSV file is using: "))

if do==1:
    df=pd.read_csv(location,sep)
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
    csv_file=csv.reader(open("/home/tatpar2210/code/trial_csv.csv","r"))
    lst_csv=list(csv_file)
    
    search_by_op="{} --To search By {}"
    for a in range(0,len(lst_csv)):
        print(search_by_op.format(lst_csv[a],lst_csv[a]))
    
    search_by=str(input("Give index to search by: "))
    search_for=str(input("Search for: "))
    
    edf=list(lst_csv[search_by])
    #print(df)
    #print("\n")
    #print(lst_df)
    for i in range(0,len(lst_csv)):
        if search_for in edf:
            print(lst_csv[i])
            i+=1
        else:
            print("No data exist")
            
