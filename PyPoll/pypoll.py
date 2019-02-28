import os
import csv

total_votes=0
candidates_total=[]
candidates_uniq=[]

file_path=os.path.join("..","Resources","election_data.csv")

with open(file_path,newline="") as election_data:
    election_reader=csv.reader(election_data,delimiter=",")
    #remove header
    election_header=next(election_reader)

    #make list of data in csv + total number of votes cast
    for line in election_reader:
        total_votes+=1
        candidates_total.append(line[2])

#remove duplicates from candidates list
for i in candidates_total:
    if i not in candidates_uniq:
        candidates_uniq.append(i)


#counting votes for each candidate
votes=[0]*len(candidates_uniq)

for i in candidates_total:
    for j in candidates_uniq:
        if i in candidates_uniq:
            cand_index=candidates_uniq.index(i)
            votes[cand_index]=votes[cand_index]+1
        break

#percentage of votes for each candidate
percentage_votes=[]

for i in range(len(votes)):
    percentage_votes.append(round((votes[i]/total_votes)*100,3))

#winner based on popular vote
max_votes=max(votes)
max_index=votes.index(max_votes)
winner=candidates_uniq[max_index]

#print results
print("Elections Results")
print("-------------------------")
print(f'Total Votes: {total_votes}')
print('-------------------------')
print(f'{candidates_uniq[0]}: {percentage_votes[0]}% ({votes[0]})')
print(f'{candidates_uniq[1]}: {percentage_votes[1]}% ({votes[1]})')
print(f'{candidates_uniq[2]}: {percentage_votes[2]}% ({votes[2]})')
print(f'{candidates_uniq[3]}: {percentage_votes[3]}% ({votes[3]})')
print('-------------------------')
print(f'Winner: {winner}')
print('-------------------------')

#create txt file with results
file=open("elections_results.txt","w")
file.write("Elections Results\n")
file.write("-------------------------\n")
file.write(f'Total Votes: {total_votes}\n')
file.write('-------------------------\n')
file.write(f'{candidates_uniq[0]}: {percentage_votes[0]}% ({votes[0]})\n')
file.write(f'{candidates_uniq[1]}: {percentage_votes[1]}% ({votes[1]})\n')
file.write(f'{candidates_uniq[2]}: {percentage_votes[2]}% ({votes[2]})\n')
file.write(f'{candidates_uniq[3]}: {percentage_votes[3]}% ({votes[3]})\n')
file.write('-------------------------\n')
file.write(f'Winner: {winner}\n')
file.write('-------------------------\n')
file.close()
