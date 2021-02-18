import os
import csv
from contextlib import redirect_stdout


profit_CVS = os.path.join( "Resources", "budget_data.csv")
rowCount= 0
netTotal= 0
totalChange= 0
averageChange= 0
new_row = 0
old_row = 0
bgstIncrease = 0
bgstDecrease = 0
bgstDecreaseMonth = 0
bgstIncreaseMonth = 0 
with open(profit_CVS) as cvs_file:
    csv_reader = csv.reader(cvs_file, delimiter= ",")

    cvs_header = next(cvs_file)
    for row in csv_reader:
        rowCount += 1
        netTotal = int(row[1]) + netTotal
        if old_row == 0:
            old_row = int(row[1])
        else:
            new_row = int(row[1])
            change = (new_row - old_row)
            totalChange = change + totalChange
            if change > bgstIncrease:
                bgstIncrease = change
                bgstIncreaseMonth = row[0]
            if change < bgstDecrease:
                bgstDecrease = change
                bgstDecreaseMonth = row[0]   
            old_row = new_row
    print(totalChange)
    averageChange = round(totalChange / (rowCount - 1), 2)
    print("Financial Analysis")
    print("--------------------------")
    print(f"Total Months: {rowCount}")
    print(f"Total: ${netTotal}")
    print(f"Average Change: ${averageChange}")
    print(f"Greatest Increase in Profits:{bgstIncreaseMonth} (${bgstIncrease})")
    print(f"Greatest Decrease in Profits: {bgstDecreaseMonth} (${bgstDecrease}")


    
    sendOut = open('Analysis/PyBank.txt', 'w')
    sendOut.write(str(totalChange));
    sendOut.write("\n""Financial Analysis");
    sendOut.write("\n""--------------------------");
    sendOut.write(f"\n""Total Months: {rowCount}");
    sendOut.write(f"\n""Total: ${netTotal}");
    sendOut.write(f"\n""Average Change: ${averageChange}");
    sendOut.write(f"\n""Greatest Increase in Profits:{bgstIncreaseMonth} (${bgstIncrease})");
    sendOut.write(f"\n""Greatest Decrease in Profits: {bgstDecreaseMonth} (${bgstDecrease}");


