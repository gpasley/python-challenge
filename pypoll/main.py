import os
import csv

def get_votes(candidates, vote_selections, total_votes):
  people = []
  vote_count =[]
  indexes = []
  percentages = []
  i = 1
  for candidate in candidates:
    votes = vote_selections.count(candidate)
    indexes.append(i)
    people.append(candidate)
    vote_count.append(votes)
    percentages.append(round((votes/total_votes) * 100))
    i += 1
  return zip(indexes, people, vote_count, percentages)

election_file = os.path.join("election_data.csv")

vote_selections = []

with open(election_file, newline="") as csvfile:
  csv_reader = csv.reader(csvfile, delimiter=",")
  csv_header = next(csvfile)
  for row in csv_reader:
    vote_selections.append(row[2])

total_votes = len(vote_selections)
candidates = set(vote_selections)
winner = max(set(vote_selections), key = vote_selections.count)

election_results = get_votes(candidates, vote_selections, total_votes)
election_output = get_votes(candidates, vote_selections, total_votes)

results_file = os.path.join("results.csv")

with open(results_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Index", "Candidate", "Votes", "Percentage"])
    writer.writerows(election_output)

print(f"Total votes: {total_votes}")

for row in election_results:
  print(f"{row[1]}: {row[3]}% ({row[2]})")

print(f"Winner: {winner}")
