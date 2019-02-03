import os 
import csv
from collections import Counter

poll_csv = os.path.join("..", "PyPoll", "election_data.csv")

voter = []
county = []
candidate = []
d = []

# Open and read csv
with open(poll_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # counting rows 
    next(csvreader)
    for row in csvreader:
        voter.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
        
d = Counter(candidate)
votes_count = len(voter)
alpha = list(d.keys())
beta = list(d.values())
top_count = max(beta)
winner_index = beta.index(top_count)
winner = alpha[winner_index]

print(f"")
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {(votes_count)}")
print(f"-------------------------")
for i in range(len(alpha)):
    per = (beta[i]/votes_count)*100
    print(f"{(alpha[i])} : {format(per,'.3f')}% ({beta[i]})")
print(f"-------------------------")
print(f"Winner: {(winner)}")
print(f"-------------------------")

output_path = os.path.join("..", "PyPoll", "newexport.txt")

with open(output_path, 'w', newline='') as datafile:

    csvwriter = csv.writer(datafile, delimiter=',')

    csvwriter.writerow([(f"")])
    csvwriter.writerow([(f"Election Results")])
    csvwriter.writerow([(f"-------------------------")])
    csvwriter.writerow([(f"Total Votes: {(votes_count)}")])
    csvwriter.writerow([(f"-------------------------")])
    for i in range(len(alpha)):
        per = (beta[i]/votes_count)*100
        csvwriter.writerow([(f"{(alpha[i])} : {format(per,'.3f')}% ({beta[i]})")])
    csvwriter.writerow([(f"-------------------------")])
    csvwriter.writerow([(f"Winner: {(winner)}")])
    csvwriter.writerow([(f"-------------------------")])

