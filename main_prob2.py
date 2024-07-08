import csv
import random
from datetime import datetime, timedelta

#function to generate DOB basis start and end dates
def generate_date_of_birth(start_date, end_date):
    start_datetime = datetime.strptime(start_date, '%Y-%m-%d')
    end_datetime = datetime.strptime(end_date, '%Y-%m-%d')
    random_datetime = start_datetime + timedelta(days=random.randint(0, (end_datetime - start_datetime).days))
    return random_datetime.strftime('%Y-%m-%d')

#generating data basis given fields
def generate_data(num_records):
    first_names = ['John', 'Jane', 'Michael', 'Emma', 'Oliver', 'Sophia']
    last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia']
    streets = ['Main St', 'Elm St', 'Oak Ave', 'Maple Rd', 'Cedar Ln']
    cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
    states = ['NY', 'CA', 'IL', 'TX', 'AZ']
    
    data = []
    for _ in range(num_records):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        address = f'{random.randint(1, 1000)} {random.choice(streets)}, {random.choice(cities)}, {random.choice(states)}'
        date_of_birth = generate_date_of_birth('1950-01-01', '2005-12-31')
        data.append((first_name, last_name, address, date_of_birth))
    
    return data

#Anonymising data with random integers
def anonymize_data(data):
    anonymized_data = []
    for record in data:
        anonymized_first_name = 'FirstName' + str(random.randint(100000, 999999))
        anonymized_last_name = 'LastName' + str(random.randint(100000, 999999))
        anonymized_address = 'Address' + str(random.randint(100000, 999999))
        anonymized_data.append((anonymized_first_name, anonymized_last_name, anonymized_address, record[3]))
    
    return anonymized_data

#Writing records to CSV
def write_to_csv(filename, data):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['first_name', 'last_name', 'address', 'date_of_birth'])
        csv_writer.writerows(data)

if __name__ == '__main__':
    num_records = 1000000 # Adjust this number based on your requirements
    filename = 'people.csv'
    data = generate_data(num_records)
    anonymized_data = anonymize_data(data)
    write_to_csv(filename, anonymized_data)
    print(f'CSV file "{filename}" generated successfully with anonymized data.')
