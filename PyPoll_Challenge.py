# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
## Do not change this code. Import csv and os modules using import statement
## Do I need to type dir(csv) after import csv? same for os
import csv
import os


# Add a variable to load a file from a path.
## Do not change this code. The .. says to go one folder up. os.path.join is to not have inbuilt syntax based on your OS
file_to_load = os.path.join("./Resources", "election_results.csv")
# Add a variable to save the file to a path.
## Do not change this code; I created analysis folder in the Resources folder.
file_to_save = os.path.join("./analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
    # candidate_options is a list
candidate_votes = {}
    # candidate_vote is a dictionary
    # dictionaries can be created using curly braces {} or the dict() function

# 1: Create a county list and county votes dictionary.
# The names are arbitrary.
county_options = []
county_names = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
    # The empty double quotes delineate an empty string. That is, a string that contains nothing. C
    # It could also have been set to None but None is not equivalent to a blank string.
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
# Names are arbitrary here but chose these 
winning_county = ""
winning_county_count = 0
winning_county_percentage = 0


# Read the csv and convert it into a list of dictionaries
# Use the csv module to read and write into csv file. We will read the contents with this code.
# I do not have a election_data csv file in my '../Resources/elections_results.csv'. 
# Do I need to create this csv file?
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
        # the csv.reader function returns a “generator” function for iterating over the contents of the CSV file.

    # Read the header
    header = next(reader)
        # The line: header = next(reader) reads the next (or in this case, first) line of the CSV file which contains the column headers.
        # The rest of the lines contain data.

    # For each row in the CSV file.
    for row in reader:
        print(row)

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_names:

            # 4b: Add the existing county to the list of counties.
            county_options.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_names[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_names[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    winning_county = ""
    winning_county_count = 0
    winning_county_percentage = 0
    for county_name in sorted(county_names.keys()):
        
        # 6b: Retrieve the county vote count.
        vote_count = county_names[county_name]

        # 6c: Calculate the percentage of votes for the county.
        pct = float(vote_count * 100) / float(total_votes)

         # 6d: Print the county results to the terminal.
        print(county_results, end="")

         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)
        
         # 6f: Write an if statement to determine the winning county and get its vote count.
        if vote_count > winning_county_count:
            winning_county = county_name
            winning_county_count = vote_count

    # 7: Print the county with the largest turnout to the terminal.
    largest_turnout = (f"-------------------------\n"
                       f"County with largest turnout: {winning_county}\n")

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(largest_turnout)

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
