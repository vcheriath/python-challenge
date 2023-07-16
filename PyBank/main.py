#PyBank Main File
#Rutgers DataScience Bootcamp
#Module 3 Homework
#By: Vigneshwar Cheriath

#Task:
#Analyze financial records given a financial dataset called 'budget_data.csv'
#Calculate:
#-total number of months included in the dataset
#-net total amount of "PRofit/Losses" Over the entire period
#-changes in "Profit/Losses" over the entire period, and then average those changes
#-greatest increase in profits (date and amount)
#-greatest decrease in profits (date and amount)

#-----------------------------------------------------------------------------------------------

#import os & csv
import os
import csv

#read the budget_data
csvpath = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

#initialize total months
TotalMonths = 0

#initialize total profits
TotalProfits = 0
#initialize variables used to calculate average change in profits
changeInProfit = 0
previousMonthsProfit = 0
TotalChanges = 0

#initialize greatest increase and greatest decrease amounts and months
GreatestIncreaseAmt = 0
GreatestIncreaseMonth = ''
GreatestDecreaseAmt = 0
GreatestDecreaseMonth = ''

with open(csvpath) as csvfile:

	#specify delimiter and variable that holds data
	csvreader = csv.reader(csvfile, delimiter=',')

	#read the header first
	csv_header = next(csvreader)
	#print(csv_header)

	#loop through each row
	for row in csvreader:
		#increment months to calculate the total number of months
		TotalMonths = TotalMonths + 1
		#add each month's profits to the running total
		TotalProfits = TotalProfits + int(row[1])
		#don't want to add the first month's profits to the changes
		if row[0] != 'Jan-10':
			#calculate the change in profits from the previous month, and add to a total for purposes of averaging
			changeInProfit = int(row[1]) - previousMonthsProfit
			TotalChanges = TotalChanges + changeInProfit

			#check if the change in profit is bigger than the current biggest. if so, set amount and date to this row
			if changeInProfit > GreatestIncreaseAmt:
				GreatestIncreaseAmt = changeInProfit
				GreatestIncreaseMonth = row[0]
			
			#check if the change in profit is smaller than the current smallest. if so, set amount and date to this row
			if changeInProfit < GreatestDecreaseAmt:
				GreatestDecreaseAmt = changeInProfit
				GreatestDecreaseMonth = row[0]

		
		previousMonthsProfit = int(row[1])

#print header
print('Financial Analysis' + '\n')
print('----------------------------' + '\n')

#print results
print(f'Total Months: {TotalMonths}' + '\n')
print(f'Total: ${TotalProfits}' + '\n')
print(f'Average Change: ${round(TotalChanges / (TotalMonths - 1),2)}' + '\n')
print(f'Greatest Increase in Profits: {GreatestIncreaseMonth} (${GreatestIncreaseAmt})' + '\n')
print(f'Greatest Decrease in Profits: {GreatestDecreaseMonth} (${GreatestDecreaseAmt})')

#create output file path
output_file = os.path.join('..', 'PyBank', 'analysis',"results.txt")

#open file to write
output = open(output_file, "w")
	
#write out results
output.write('Financial Analysis' + '\n')
output.write('----------------------------' + '\n')
output.write(f'Total Months: {TotalMonths}' + '\n')
output.write(f'Total: ${TotalProfits}' + '\n')
output.write(f'Average Change: ${round(TotalChanges / (TotalMonths - 1),2)}' + '\n')
output.write(f'Greatest Increase in Profits: {GreatestIncreaseMonth} (${GreatestIncreaseAmt})' + '\n')
output.write(f'Greatest Decrease in Profits: {GreatestDecreaseMonth} (${GreatestDecreaseAmt})')
