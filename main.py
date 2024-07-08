import csv

def generate_fixed_width_file(spec_file, output_file):
    # Read specification
    with open(spec_file, 'r', encoding='utf-8') as spec:
        fields = []
        for line in spec:
            field_name, length = line.strip().split(': ')
            fields.append((field_name.strip(), int(length)))
    
    # Generate fixed width data
    data = [
        {'Field1': 'John Doe', 'Field2': '12345', 'Field3': '20230101'},
        {'Field1': 'Jane Smith', 'Field2': '67890', 'Field3': '20230202'},
    ]
    
    with open(output_file, 'w', encoding='utf-8') as out:
        for record in data:
            line = ''
            for field_name, length in fields:
                value = record.get(field_name, '')
                line += value.ljust(length)[:length]  # pad or truncate based on length
            out.write(line + '\n')

def parse_fixed_width_file(input_file, spec_file, output_csv):
    # Read specification
    with open(spec_file, 'r', encoding='utf-8') as spec:
        fields = []
        for line in spec:
            field_name, length = line.strip().split(': ')
            fields.append((field_name.strip(), int(length)))
    
    # Parse fixed width file
    parsed_data = []
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            record = {}
            for i, (field_name, length) in enumerate(fields):
                start = sum(length for _, length in fields[:i])  # calculate starting position
                end = start + length
                value = line[start:end].strip()
                record[field_name] = value
            parsed_data.append(record)
    
    # Write to CSV
    with open(output_csv, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=[field_name for field_name, _ in fields])
        writer.writeheader()
        writer.writerows(parsed_data)

# Generate fixed width file
generate_fixed_width_file('spec_file.txt', 'fixed_width.txt')

# Parse fixed width file to CSV
parse_fixed_width_file('fixed_width.txt', 'spec_file.txt', 'output.csv')



