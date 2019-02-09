#import libararies
import os
import csv

#create variables
total_months = 0
Profit_Loss = 0
num = 0
average_change = 0
pl_list = []
new = []
date = []

#-------------------
csvpath = os.path.join('Resources','budget_data.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    
    for row in csvreader:
        #count total months
        total_months += 1
        #count total net profit/loss
        Profit_Loss += int(row[1])
        #put profit/loss into a list
        pl_list.append(row[1])
        #put date into a list
        date.append(row[0])

  
for x in pl_list:
    #keep num <= to 84 to stay in list range
    if num <= 84:
        #check change by month and add to average_change
        check =  - int(pl_list[num]) + int(pl_list[(num+1)])
        average_change += check
        num += 1 
        #append averages by month to list
        new.append(check)

#round to two decimals
average_round = round((average_change/num), 2)

#Get the max and min
#print(max(new))
#print(min(new))

#now find the index for max and min numbers
#print(new.index(1926159))
#print(new.index(-2196167))

#find the corresponding dates and add 1, because the first cell is blank for new list
#print(date[(24+1)])
#print(date[(43+1)])

#print to terminal
print(f'Financial Analysis')
print(f'-----------------------------------')
print(f'Total Month: {total_months}')
print(f'Total: ${Profit_Loss}')   
print(f'Average Change: ${average_round}') 
print(f'Greatest Increase in Profits: {date[(24+1)]} (${max(new)})')
print(f'Greatest Decrease in Profits: {date[(43+1)]} (${min(new)})')

#------------------- 
file = 'output.txt'

with open(file, 'w') as text:

    text.write(f'Financial Analysis\n')
    text.write(f'-----------------------------------\n')
    text.write(f'Total Month: {total_months}\n')
    text.write(f'Total: ${Profit_Loss}\n')
    text.write(f'Average Change: ${average_round}\n')
    text.write(f'Greatest Increase in Profits: {date[(24+1)]} (${max(new)})\n')
    text.write(f'Greatest Decrease in Profits: {date[(43+1)]} (${min(new)})')