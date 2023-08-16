import os
import csv
from statistics import mode

#Get the number of lines in the file (total votes)
with open('Resources\election_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = -1
    for line in csv_reader:
         line_count += 1
      
#Get the list of candidates
with open('Resources\election_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    candidates = []
    for index, row in enumerate(csv_reader):
      if index > 0 and row[2] not in candidates:
         candidates.append(row[2])


#Get the list of all votes by candidate
with open('Resources\election_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    candidate_votes = []
    for index, row in enumerate(csv_reader):
      if index > 0:
         candidate_votes.append(row[2])

#Get most common candidate
def most_common(List):
    return(mode(List))

print("Election Results")
print('-' * 40)
print(f"Total Votes: {line_count}")
print('-' * 40)

for candidate in candidates:
   candidate_count = candidate_votes.count(candidate)
   candidate_percentage = (candidate_count / line_count) * 100
   print(f"{candidate}: {round(candidate_percentage,2)}% ({candidate_count})")

print('-' * 40)
print(f"Winner: {most_common(candidate_votes)}")
print('-' * 40)


output_file_path = 'election_results.txt'

# Open the output file in write mode
with open(output_file_path, 'w') as output_file:
    output_file.write("Election Results\n")
    output_file.write('-' * 40 + "\n")
    output_file.write(f"Total Votes: {line_count}\n")
    output_file.write('-' * 40 + "\n")

    for candidate in candidates:
        candidate_count = candidate_votes.count(candidate)
        candidate_percentage = (candidate_count / line_count) * 100
        output_file.write(f"{candidate}: {round(candidate_percentage, 2)}% ({candidate_count})\n")

    output_file.write('-' * 40 + "\n")
    output_file.write(f"Winner: {most_common(candidate_votes)}\n")
    output_file.write('-' * 40 + "\n")