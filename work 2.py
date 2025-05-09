import csv

EmployeeName = input("Employee Name:")
EmployeeName = EmployeeName.upper()
found = False
matched_row = []

with open('Total.csv', 'r', newline='') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        if EmployeeName in [cell.upper() for cell in row]:
            found = True
            matched_row = row
            break

if found:
    print("Found")
    print("Employee Details:")
    for i, value in enumerate(matched_row):
        print(f"Field {i+1}: {value}")
    output_filename = f"{EmployeeName.strip().replace(' ', '_')}_data.csv"
    with open(output_filename, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        with open('Total.csv', 'r', newline='') as file:
            header = next(csv.reader(file))
            writer.writerow(header)
        writer.writerow(matched_row)
    
    print(f"\nEmployee data has been exported to {output_filename}")
else:
    print("Not Found")
