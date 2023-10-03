import csv
import os

# Open the input and output file paths
csvpath = os.path.join("..", "Resources", "election_data.csv")
textoutput = os.path.join("..","Analysis","election_analysis.txt")

# Set the variables to store data
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Read and process the CSV file
with open(csvpath, "r") as file:
    csv_reader = csv.reader(file)
    
    # Skip the header row
    next(csv_reader)
    
    for row in csv_reader:
        total_votes += 1
        candidate = row[2]
        
        # Count candidate votes
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Find the winner
for candidate, votes in candidates.items():
    if votes > winner_votes:
        winner_votes = votes
        winner = candidate

# Calculate and format the percentages
percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidates.items()}

# Print to terminal

print(f"Election Results")
print(f"Total Votes: {total_votes}")
for candidate, votes in candidates.items():
    print(f"{candidate}: {percentages[candidate]:.3f}% ({votes})")
print(f"Winner: {winner}")


# Print the results to analysis file
with open(textoutput, "w") as txt_file:


# Print the results to Analysis file
 with open(textoutput, "w") as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("--------------------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("--------------------------------------\n")
    for candidate, votes in candidates.items():
     txt_file.write(f"{candidate}: {percentages[candidate]:.3f}% ({votes})\n")
    txt_file.write("-------------------------------------\n")
    txt_file.write(f"Winner: {winner}\n")
    txt_file.write("-------------------------------------\n")





       




