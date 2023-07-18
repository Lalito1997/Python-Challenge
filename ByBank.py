#Importing the dependancies needed
import os
import csv

#Accessing the csv file 
pybank_csv = os.path.join('python_challenge', 'Starter_Code', 'PyBank', 'Resources', 'budget_data.csv')

#Creaeting variables as well as the empty lists that will be used for analysis
months = []
profit_losses = []
changes = []

#The with statement reads the csv file and preps it for the for loop where data is then extracted
with open(pybank_csv, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    #This line ignores the header row
    next(csv_reader)
    
    #extracting the dat from the csv file that was read in the code above
    for row in csv_reader:
        
        month = row[0]
        #The int() function is making sure that the data is in teh form of an integer
        profit_loss = int(row[1])
        
        #These lines make sure that the data is being stored
        months.append(month)
        profit_losses.append(profit_loss)

#Using the len() function we are essentially counting all of the months within the data set
total_months = len(months)

#In this code we are adding up all of the rows of data attributed to profit_loss which we have defined above and storing it in the variable 
#net_profit_loss to be later printed below
net_profit_loss = sum(profit_losses)

#In this for loop we are going through row by row and finds the difference between the months and appends it at the end
for i in range(1, len(profit_losses)):
    change = profit_losses[i] - profit_losses[i-1]
    changes.append(change)

#in order to find the average change you first have to sum the difference and diviing it by the length of the column
average_change = sum(changes) / len(changes)
#Easy to figure out that you are calling for the max and min value within the appended list of changes
greatest_increase = max(changes)
greatest_decrease = min(changes)

#From the code above you are also finding the corresponding month that is related to the max and min change
greatest_increase_month = months[changes.index(greatest_increase) + 1]
greatest_decrease_month = months[changes.index(greatest_decrease) + 1]

#With these print statments we are calling from the varibales we defined above
#The with open as file, I am able t0 pruint out the results of the code in a seperate file
with open('financial_analysis.txt', 'w') as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${net_profit_loss}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")