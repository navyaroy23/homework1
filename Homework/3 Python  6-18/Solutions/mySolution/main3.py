
import os
import csv

budget_data = os.path.join("C:/Users/navya/python-challenge/PyBank/budget_data.csv")

total_months = 0
total_pl = 0
row_value = 0
change = 0
dates = []
profits = []

with open(budget_data, 'r') as f:
    read = csv.reader(f)
    next(read)
    previousval = 0
    totalmonth = 0
    nettotal = 0
    averageRow = 0
    highestval = 0
    lowestval = 0
    maxmonth = ""
    minmonth = ""
    for row in read:       
        columns = row[0]        
        month, row_value = columns.split(",")
        nettotal = nettotal + int(row_value)
        totalmonth = totalmonth + 1
        print(month, row_value)
        print (row)
        
        if previousval == 0:
            previousval = row_value
            highestval = previousval
            lowestval = previousval
            maxmonth = month
            minmonth = month
            continue           
        if int(highestval) > int(row_value):
            highestval = highestval 
            maxmonth = maxmonth        
        else:
                highestval = row_value
                maxmonth = month

        if int(lowestval) < int(row_value):
            lowestval = highestval 
            minmonth = minmonth       
        else:
                lowestval = row_value   
                minmonth = month
        
        previousval = row_value
        total_net = len(nettotal)
        averageRow = total_net/totalmonth
    
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(totalmonth)}")
print(f"Total: ${str(nettotal)}")
print(f"Average Change: ${str(round(averageRow,2))}")
print(f"Greatest Increase in Profits: {maxmonth} (${str(highestval)})")
print(f"Greatest Decrease in Profits: {minmonth} (${str(lowestval)})")

output = open("output.txt", "w")

line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str(f"Total Months: {str(totalmonth)}")
line4 = str(f"Total: ${str(nettotal)}")
line5 = str(f"Average Change: ${str(round(averageRow,2))}")
line6 = str(f"Greatest Increase in Profits: {maxmonth} (${str(highestval)})")
line7 = str(f"Greatest Decrease in Profits: {minmonth} (${str(lowestval)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))