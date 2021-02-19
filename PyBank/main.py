#Import needed tools
import os
import csv
from contextlib import redirect_stdout


#path to the file being used for data
profit_CVS = os.path.join( "Resources", "budget_data.csv")
#establish Variables
#total row count of CSV file
rowCount= 0
#total of all prifit column 
netTotal= 0
#sum of change
totalChange= 0
#Average of all changes froim month to month
averageChange= 0
#Variables used to calculate the change
new_row = 0
old_row = 0
#Variables used to store the largest and smalles changes
bgstIncrease = 0
bgstDecrease = 0
#Variable used to store the months for the biggest and smallest changes
bgstDecreaseMonth = 0
bgstIncreaseMonth = 0 
with open(profit_CVS) as cvs_file:
    #This is to read through the file seperating data by comma.
    csv_reader = csv.reader(cvs_file, delimiter= ",")
    #this is to skip the header during the for loop below.
    cvs_header = next(cvs_file)
    #This for loop goes through each line of the csv file and collects all the details needed.
    for row in csv_reader:
        #This counts the toal rows.
        rowCount += 1
        #sum the profit column
        netTotal = int(row[1]) + netTotal
        #set old row to the first profit during the first time going through the for loop.
        if old_row == 0:
            old_row = int(row[1])
        else:
            #collect new monthly profit number.
            new_row = int(row[1])
            #find the difference between the new and old.
            change = (new_row - old_row)
            #add the difference to the previous differences.
            totalChange = change + totalChange
            #store the highest change
            if change > bgstIncrease:
                bgstIncrease = change
                bgstIncreaseMonth = row[0]
            #store the most negative change
            if change < bgstDecrease:
                bgstDecrease = change
                bgstDecreaseMonth = row[0]   
            #take the new profit and make it the old profit for the next loop.
            old_row = new_row
    
    #round average change to 2 decimals
    averageChange = round(totalChange / (rowCount - 1), 2)
    #print all info
    print("Financial Analysis")
    print("--------------------------")
    print(f"Total Months: {rowCount}")
    print(f"Total: ${netTotal}")
    print(f"Average Change: ${averageChange}")
    print(f"Greatest Increase in Profits:{bgstIncreaseMonth} (${bgstIncrease})")
    print(f"Greatest Decrease in Profits: {bgstDecreaseMonth} (${bgstDecrease}")


    #send info with same layout to external file
    sendOut = open('Analysis/PyBank.txt', 'w')
    sendOut.write(str(totalChange));
    sendOut.write("\n""Financial Analysis");
    sendOut.write("\n""--------------------------");
    sendOut.write(f"\n""Total Months: {rowCount}");
    sendOut.write(f"\n""Total: ${netTotal}");
    sendOut.write(f"\n""Average Change: ${averageChange}");
    sendOut.write(f"\n""Greatest Increase in Profits:{bgstIncreaseMonth} (${bgstIncrease})");
    sendOut.write(f"\n""Greatest Decrease in Profits: {bgstDecreaseMonth} (${bgstDecrease}");


