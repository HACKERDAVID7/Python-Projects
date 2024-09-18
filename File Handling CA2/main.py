
                                            # Olympic Swimming Records Management System

####################################################################################################################################
#                                                   Swimming 

# dictionary to store records

from records import records

def add_record():
    year = int(input("Enter the year: "))
    winner_name = input("Enter the winner's name: ")
    country=input("Enter the winner's country: ")
    records[year] = {"winner": {"name":winner_name,"country":country}}
    save_all_records()
    print("Record added successfully!")

def delete_record():   
    year = int(input("Enter the year of the record to delete: "))
    if year in records:
        del records[year]
        save_all_records()
        print("Record deleted successfully!")
    else:
        print("Record not found!")

def save_all_records():
    # print("Olympics Record")
    # print("YEAR\tWINNER NAME\t    COUNTRY")
    with open("LPU/SEM3/CAP776/Project/CA2/txt/allRecords.txt", 'w') as file:
        file.writelines("YEAR\tWINNER NAME\t    COUNTRY \n")
        for year, record in records.items():
            v = f'{year}\t{record["winner"]["name"]:20s}{record["winner"]["country"]:10s}'
            # print(v)
            file.writelines(v + "\n")



def save_last_5_year_winners():
    last_5_years = sorted(records.keys())[-5:]
    with open("LPU/SEM3/CAP776/Project/CA2/txt/last5Records.txt", "w") as file:
        for year in last_5_years:
            v = f'Year: {year}, Winner Name: {records[year]["winner"]["name"]}, Country:{records[year]["winner"]["country"]}'
            # print(v)
            file.writelines(v + "\n")



def read_records(filename):
    try:
        with open(filename,'r') as file:
            content = file.read()
            print(content)
    except:
        print("Unable to find the file.")



while True:
    print("\nOlympic Swimming Records Management System")
    print("1. Add a new record")
    print("2. Delete a record")
    print("3. Save all records")
    print("4. Save last 5 year winners")
    print("5. View all records from text file")
    print("6. View last 5 year winners from text file")
    print("7. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        add_record()
        
    elif choice == 2:
        delete_record()
    elif choice == 3:
        save_all_records()
    elif choice == 4:
        save_last_5_year_winners() 
    elif choice == 5:
        f = "LPU/SEM3/CAP776/Project/CA2/txt/allRecords.txt"
        read_records(f)
    elif choice == 6:
        f = "LPU/SEM3/CAP776/Project/CA2/txt/last5Records.txt"
        read_records(f)
    elif choice == 7:
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")