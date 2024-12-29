import csv

with open("output_dict.csv", mode="w", newline="") as file:
    fieldnames = ["Name", "Age", "City"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(data)

print("CSV file written successfully!")

def writeIntoFile(){
    data = [
        {"Name": "Alice", "Age": 30, "City": "New York" },
        {"Name": "Bob", "Age": 25, "City": "Los Angeles"},
         {"Name": "Charlie", "Age": 35, "City": "Chicago"}
        ]
    
}

if __name__ == '__main__':
    writeIntoFile()
