import csv
import os

def fixPercent(num):
    num = "{:.3%}".format(num)
    return num

inputfile = os.path.join("Resources", "election_data.csv")
outputfile = os.path.join("Analysis", "pyPoll_analysis.txt")

UniqueCandidates = []
VoteCounts = []
VotePercent = []
TotalVotes = 0
WinnerCount = 0
with open(inputfile, 'r') as electiondata:
    reader = csv.reader(electiondata, delimiter=",")

    
    Headers = next(reader)

  

    for row in reader:
        TotalVotes += 1
    
       
        if row[2] not in UniqueCandidates:

            UniqueCandidates.append(row[2])
            VoteCounts.append(1)

        
        else:
            CandidateIndex = UniqueCandidates.index(row[2])
            VoteCounts[CandidateIndex] += 1
        


for i in range(len(VoteCounts)):
    VotePercent.append(VoteCounts[i] / TotalVotes)


for i in range(len(VoteCounts)):

  
    if VoteCounts[i] > WinnerCount:
           
        WinnerCount = VoteCounts[i]

        Winner = UniqueCandidates[i]

with open(outputfile, 'w') as textfile:
    textfile.write(f"Election Results\n"
                   f"----------------------------\n"
                   f"Total Votes: {TotalVotes}\n"
                   f"----------------------------\n"
                   )

   
    for i in range(len(UniqueCandidates)):
        textfile.write(f"{UniqueCandidates[i]}: {fixPercent(VotePercent[i])} ({VoteCounts[i]})\n")

    textfile.write(f"----------------------------\n"
                   f"Winner: {Winner}\n"
                   f"----------------------------\n"
                  )

with open (outputfile, 'r') as analysis:
    contents = analysis.read()
    print(contents)