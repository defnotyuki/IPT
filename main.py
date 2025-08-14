import json

def readData():
    with open("data.json", "r") as file:
        data = json.load(file)
    for row in data:
        print(f"Emp Num: {row['emp_num']}")
        print(f"Name: {row['name']}")
        print(f"Designation: {row['designation']}")
        print(f"Rate: {row['rate']}")
        print(f"Address: {row['address']['city']}, {row['address']['brgy']}, {row['address']['street']}")
        print("--" * 10)
        

def writeData():
    with open('data.json', 'r') as file:
        data = json.load(file)

    empnum = input("Enter Employee Number: ")
    name = input("Enter your name: ")
    designation = input("Enter your designation: ")
    rate = int(input("Enter your rate: "))
    city = input("Enter your city: ")
    brgy = input("Enter your brgy: ")
    street = input("Enter your street: ")

    new_rec = {
        "emp_num" : empnum,
        "name" : name,
        "designation" : designation,
        "rate" : rate,
        "address" : {
            "city" : city,
            "brgy" : brgy,
            "street" : street
        }
    }
    data.append(new_rec)
    with open('data.json', 'w') as file:
        json.dump(data, file, indent = 4)
    print("Saved Successfully")


if __name__ == "__main__":
    #writeData()
    readData()
