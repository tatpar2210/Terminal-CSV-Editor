import os
import pandas as pd
import shutil

print("1 --Rename a file")
print("2 --Find character in file name")
print("3 --Replace character in file name") 
print("4 --Search multi characters in file name")

choice_1 = int(input("What u wanna do: "))

direc = str(input("Give location of the folder containing file: "))
lst_direc = os.listdir(direc)
df = pd.Series(lst_direc)

os.chdir(direc)

print(df)

if choice_1 == 1:
    
    file = int(input("Give index of the file to br renamed: "))

    new_name = str(input("Enter new name of the with extension: "))

    os.rename(df[file], new_name)
    
    print("Done")

elif choice_1 == 2:
    # str1="Search for in {}: "
    search_for = str(input("Search for: "))
    x = []
    for a in range(0, len(df)):
        
        if search_for in df[a]:
            x.append(df[a])
            print(df[a])
            a += 1
            
    print(x)
    print("n", len(x), "Results Found")
    if len(x) != 0:
        choice_2 = str(input("Wanna separate out the files(Y/N): "))
        if choice_2 == "Y":
            print("1 --Make a separate folder in the same directory")
            print("2 --Save it at a new location")
        
            choice_3 = int(input("How u wanna save: "))
            str2 = "Give name to your new folder in {}/: "
        
            # Saving files in a new folder in same directory
            if choice_3 == 1:
                new_folder = str(input("Give new folder a name: "))
                dst_path = direc+"/"+new_folder
                os.mkdir(dst_path)
                
                for i in range(0, len(x)):
                    src_path = direc + "/" + x[i]
                    shutil.copy(src=src_path, dst=dst_path)
                print("Done!!")

            elif choice_3 == 2:
                location = str(input("Give a new location to save output(s): "))
                choice_4 = str(input("Wanna make a folder in it(Y/N): "))
            
                if choice_4 == "Y":
                    name_folder = str(input(str2.format(location)))
                    dst_path = location + "/" + name_folder
                    os.mkdir(dst_path)
                
                    for i in range(0, len(x)):
                        src_path = direc + "/" + x[i]
                        shutil.copy(src=src_path, dst=dst_path)
                    print("Done")
                    
                elif choice_4 == "N":
            
                    for i in range(0, len(x)):
                        src_path = direc + "/" + x[i]
                        shutil.copy(src=src_path, dst=location)
                    print("Done")
            
                else:
                    print("Failed")
        
        else:
            print("OK")
    else:
        print("\n")
        print("No results found...")
            
elif choice_1 == 3:
    replace = str(input("What u wanna replace: "))
    replace_to = str(input("Replace by: "))
    for a in range(0, len(df)):
        if replace in df[a]:
            p = df[a].replace(replace, replace_to)
            os.rename(df[a], p)

    print("Replaced Successfuly!!")

elif choice_1 == 4:
    search_for = ""
    print("If finished Type [Done]")
    list_df = list(df)
    # print(list_df)
    x = []
    while search_for != "Done":
        search_for = str(input("Enter search conditions one by one by pressing [Enter]: "))
        x.append(search_for)
    # print(x)
    y = []
    for i in range(0, len(list_df)):
        for a in range(0, len(x)):
            if x[a] in list_df[i]:
                print(list_df[i])
                y.append(list_df[i])
                break
            else:
                pass
    if len(y) == 0:
        print("\n")
        print("No results found...")
    else:
        print("\n")
        print(len(y), "Results Found...")
        print("\n")
        choice_2 = str(input("Wanna separate out the files(Y/N): "))
        if choice_2 == "Y":
            print("1 --Make a separate folder in the same directory")
            print("2 --Save it at a new location")

            choice_3 = int(input("How u wanna save: "))
            str2 = "Give name to your new folder in {}/: "

            # Saving files in a new folder or in same directory
            if choice_3 == 1:
                new_folder = str(input("Give new folder a name: "))
                dst_path = direc + "/" + new_folder
                # print(dst_path)
                os.mkdir(dst_path)

                for i in range(0, len(y)):
                    src_path = direc + "/" + y[i]
                    # print(src_path)
                    shutil.copy(src=src_path, dst=dst_path)
                print("Done!!")

            elif choice_3 == 2:
                location = str(input("Give a new location to save output(s): "))
                choice_4 = str(input("Wanna make a folder in it(Y/N): "))

                if choice_4 == "Y":
                    name_folder = str(input(str2.format(location)))
                    dst_path = location + "/" + name_folder
                    os.mkdir(dst_path)

                    for i in range(0, len(y)):
                        src_path = direc + "/" + y[i]
                        shutil.copy(src=src_path, dst=dst_path)
                    print("Done")

                elif choice_4 == "N":

                    for i in range(0, len(y)):
                        src_path = direc + "/" + y[i]
                        shutil.copy(src=src_path, dst=location)
                    print("Done")

                else:
                    print("Failed")

        else:
            print("OK")
