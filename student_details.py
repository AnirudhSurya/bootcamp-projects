import csv

for i in range(0,3):
    name = input("enter the name:")
    usn = input("enter the usn:")

    with open('student_details.csv',newline='') as csvfile:
        details = csv.reader(csvfile)
        

        for row in details:
        	print(row)