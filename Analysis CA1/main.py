                                            # Olympic Records Management System

####################################################################################################################################
#                                                  Swimming 

# dictionary to store records
from records import records, AusRecords

def add_record():
    ch=int(input("Enter 1:To add record for Australia Swimming\nEnter 2:To add record for Olympics Swimming"))
    if(ch==1):
        year = int(input("Enter the year: "))
        event = input("Enter the event name: ")
        medal=input("Enter the medal won(Gold/Bronze/Silver/None) ")
        AusRecords.append({'year':year,
        'Event':event,
        'Medal':medal})
        print("Record added successfully!")
    else:
        year = int(input("Enter the year: "))
        winner_name = input("Enter the winner's name: ")
        country=input("Enter the winner's country: ")
        records[year] = {"winner": {"name":winner_name,"country":country}}
        print("Record added successfully!")

def delete_record():
    ch=int(input("Enter 1:To delete record for Australia Swimming\nEnter 2:To delete record for Olympics Swimming "))
    if(ch==1):
        index=1
        print("INDEX\tYEAR\t\tEVENT\t\t\t\tMEDAL")
        for record in AusRecords:
            print(f'{index}\t{record["year"]}\t{record["Event"]:40s}{record["Medal"]:10s}')
            index+=1
        n = int(input("Enter the index of record to delete "))
        del AusRecords[n-1]
        print("Record deleted successfully!")
        
    else:
        year = int(input("Enter the year of the record to delete: "))
        if year in records:
            del records[year]
            print("Record deleted successfully!")
        else:
            print("Record not found!")

def view_all_records():
    print("Olympics Record")
    print("YEAR\tWINNER NAME\tCOUNTRY")
    for year, record in records.items():
        print(f'{year}\t{record["winner"]["name"]:20s}{record["winner"]["country"]:10s}')
    print("\n\nAustralia Swimming Record") 
    print("YEAR\t\tEVENT\t\t\tMEDAL")   
    for record in AusRecords:
        print(f'{record["year"]}\t{record["Event"]:30s}\t{record["Medal"]:10s}')

def view_last_5_year_winners():
    last_5_years = sorted(records.keys())[-5:]
    for year in last_5_years:
        print(f'Year: {year},Winner Name: {records[year]["winner"]["name"]}, Country:{records[year]["winner"]["country"]}')

def count_medals():
    # medal count for Olympics Format
    # med_count={
    #     year:{
    #         'GOLD':5,
    #         'SILVER':6,
    #         'BRONZE':7
    #     }
    # }
    med_count={}
    for record in AusRecords:
        if(record['year'] not in med_count.keys()):  
           med_count[record['year']]={
            'GOLD':0,
            'SILVER':0,
            'BRONZE':0
            }
        if(record["Medal"]=="Gold"):
            med_count[record['year']]['GOLD']+=1
        elif(record["Medal"]=="Silver"):
            med_count[record['year']]['SILVER']+=1
        elif(record["Medal"]=="Bronze"):
            med_count[record['year']]['BRONZE']+=1  
    for year,value in med_count.items():    
        print(f'Medal count for Year:{year}')      
        print(f'Gold Medals: {value["GOLD"]}, Silver Medals: {value["SILVER"]}, Bronze Medals:{value["BRONZE"]}, Total Medals:{value["GOLD"]+value["SILVER"]+value["BRONZE"]}')


while True:
    print("\nOlympic Records Management System")
    print("1. Add a new record")
    print("2. Delete a record")
    print("3. View all records")
    print("4. View last 5 year winners")
    print("5. Count All Medals for Australia(YEAR WISE)")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        add_record()
    elif choice == 2:
        delete_record()
    elif choice == 3:
        view_all_records()
    elif choice == 4:
        view_last_5_year_winners()
    elif choice == 5:
        count_medals()    
    elif choice == 6:
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")