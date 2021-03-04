#Import needed tools
import os
import csv
from contextlib import redirect_stdout


#Establish path to the CSV file I will be using
Voter_info = os.path.join( "Resources", "election_data.csv")
#Establish voter count variable with -1 to counter the first +1
vtrCount = -1
#Establish a list of candidates
CandList = []
#Establish variables to count candidate votes
vote0 = 0
vote1 = 0
vote2 = 0 
vote3 = 0
#establish variables to hold percantage of total votes for candidates
percentage0 = 0
percentage1 = 0
percentage2 = 0
percentage3 = 0
#Open cvs file
with open(Voter_info) as cvs_file:
    csv_reader = csv.reader(cvs_file, delimiter= ",")
    #Skip header line
    cvs_header = next(cvs_file)
    #Loop through the data in the CVS file
    for row in csv_reader:
        #count the rows
        vtrCount +=1 
        #populate the candidate list
        if row[2] not in CandList:
            CandList.append(row[2])
        #Count votes for first candidate
        if row[2] == CandList[0]:
            vote0 += 1
            #Skip through if count is zero for anything
            if (vote0 == 0) or (vtrCount == 0):
                pass
            else:
                #calculate 1st candidate percentage
                percentage0 = vote0 / vtrCount
        elif row[2] == CandList[1]:
            #Count votes for second candidate
            vote1 += 1 
            #calculate 2nd candidate percentage
            percentage1 = vote1 / vtrCount
        elif row[2] == CandList[2]:
            #Count votes for third candidate
            vote2 += 1
            #calculate 2nd candidate percentage
            percentage2 = vote2 / vtrCount
        elif row[2] == CandList[3]:
            #Count votes for fourth candidate
            vote3 += 1
            #calculate 2nd candidate percentage
            percentage3 = vote3 / vtrCount
    
    #Round all percanteges to two decimal places
    percentage0 = round(percentage0, 2)
    percentage1 = round(percentage1, 2)
    percentage2 = round(percentage2, 2)
    percentage3 = round(percentage3, 2)
    #print all results
    print("Election Results")
    print("-----------------------------")
    print(f"Total Votes: {vtrCount}")
    print("-----------------------------")
    print(f"{CandList[0]}: {percentage0 * 100}% Votes:({vote0})")
    print(f"{CandList[1]}: {percentage1 * 100}% Votes:({vote1})")
    print(f"{CandList[2]}: {percentage2 * 100}% Votes:({vote2})")
    print(f"{CandList[3]}: {percentage3 * 100}% Votes:({vote3})")
    print("-----------------------------")
    print(f"Winner: {CandList[0]}")
    print("-----------------------------")

    #send all printed lines to outside file calles PyPoll.txt
    sendOut = open('Analysis/PyPoll.txt', 'w')
    sendOut.write("\n""Election Results")
    sendOut.write("\n""-----------------------------")
    sendOut.write(f"\n""Total Votes:")
    sendOut.write(str(vtrCount))
    sendOut.write("\n""-----------------------------")
    sendOut.write(f"\n")
    sendOut.write(str(CandList[0]))
    sendOut.write(f": ")
    sendOut.write(str(percentage0 * 100))
    sendOut.write(f" Votes:")
    sendOut.write(str(vote0))
    sendOut.write(f"\n")
    sendOut.write(str(CandList[1]))
    sendOut.write(f": ")
    sendOut.write(str(percentage1 * 100))
    sendOut.write(f" Votes:")
    sendOut.write(str(vote1))
    sendOut.write(f"\n")
    sendOut.write(str(CandList[2]))
    sendOut.write(f": ")
    sendOut.write(str(percentage2 * 100))
    sendOut.write(f" Votes:")
    sendOut.write(str(vote2))
    sendOut.write(f"\n")
    sendOut.write(str(CandList[3]))
    sendOut.write(f": ")
    sendOut.write(str(percentage3 * 100))
    sendOut.write(f" Votes:")
    sendOut.write(str(vote3))
    sendOut.write("\n""-----------------------------")
    sendOut.write(f"\n""Winner: ")
    sendOut.write(str(CandList[0]))
    sendOut.write("\n""-----------------------------")

