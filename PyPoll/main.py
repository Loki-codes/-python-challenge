import os
import csv



Voter_info = os.path.join( "Resources", "election_data.csv")
vtrCount = -1
CandList = []
kVote = 0
cVote = 0
lVote = 0 
oVote = 0
kPercentage = 0
cPercentage = 0
lPercentage = 0
oPercentage = 0
with open(Voter_info) as cvs_file:
    csv_reader = csv.reader(cvs_file, delimiter= ",")
    cvs_header = next(cvs_file)

    for row in csv_reader:
        vtrCount +=1 
        if row[2] not in CandList:
            CandList.append(row[2])
        if row[2] == CandList[0]:
            kVote += 1
            if (kVote == 0) or (vtrCount == 0):
                pass
            else:
                kPercentage = kVote / vtrCount
        elif row[2] == CandList[1]:
            cVote += 1
            cPercentage = cVote / vtrCount
        elif row[2] == CandList[2]:
            lVote += 1
            lPercentage = lVote / vtrCount
        elif row[2] == CandList[3]:
            oVote += 1
            oPercentage = oVote / vtrCount
    

    kPercentage = round(kPercentage, 2)
    cPercentage = round(cPercentage, 2)
    lPercentage = round(lPercentage, 2)
    oPercentage = round(oPercentage, 2)
    print("Election Results")
    print("-----------------------------")
    print(f"Total Votes: {vtrCount}")
    print("-----------------------------")
    print(f"{CandList[0]}: {kPercentage * 100}% ({kVote})")
    print(f"{CandList[1]}: {cPercentage * 100}% ({cVote})")
    print(f"{CandList[2]}: {lPercentage * 100}% ({lVote})")
    print(f"{CandList[3]}: {oPercentage * 100}% ({oVote})")
    print("-----------------------------")
    print(f"Winner: {CandList[0]}")
    print("-----------------------------")
