cases = open("confirmed_global.csv")
recoveries = open("recovered_global.csv")
deaths = open("deaths_global.csv")

cases_data = cases.read().splitlines()
recoveries_data = recoveries.read().splitlines()
deaths_data = deaths.read().splitlines()


required_date = input("Please enter date you want to export \nIn the format d/m/y : ")


# STEP 1 SPLIT LINE INTO INDIVIDUAL VALUES
values = cases_data[0].split(",")

# print(values[4])

# STEP 3 SEARCH FOR REQUIRED DATE'S POSITION IN THE FILE

index = 0
if required_date in values:
    
    for value in values:

        if value == required_date:
            print(index)
            break
            
        index += 1

# STEP 4 : USE RETRIEVED INDEX TO FIND VALUES FROM OTHER FILES

zipped_files = zip(cases_data, recoveries_data, deaths_data) # THIS WILL ZIP THE ROWS OF ALL THE DATA INTO ONE

output_file = open("result.csv", "w") # OPEN A NEW CSV FILE FOR WRITING FOR THE PURPOSE OF WRITING OUR VALUES INTO

for cases, deaths, recoveries in zipped_files: # LOOP THROUGH ALL VALUES OF OR ZIPPED DATA

    country_name_value = cases.split(",")[1]
    cases_value = cases.split(",")[index]
    deaths_value = deaths.split(",")[index]
    recovery_value = recoveries.split(",")[index]
    
    output_file.write(f'{country_name_value},{cases_value},{deaths_value},{recovery_value}\n')
