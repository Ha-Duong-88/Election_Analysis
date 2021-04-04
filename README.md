# Election_Analysis
Module 3 - Python 3.7.6 and Visual Studio Code
PyPoll Challenge

# Overview of Election Audit

This project is to conduct an election audit for the Colorado Board of Elections. The objective to analyze the election data and determine the following information for the election:
  1) Total number of votes cast
  2) A complete list of candidates who received votes
  3) Total number of votes each candidate received
  4) Percentage of votes each candidate won
  5) The winner of the election based on popular vote

# Election-Audit Results

  * The total number of votes cast was 369, 711
  
  * The following is a print-out from the command line of the break-down of the number of votes and the percentage of the votes for each county and candidate in the precinct

### Election Results
-------------------------
### Total Votes: 369,711
-------------------------

### County Votes:
Jefferson: 10.5% (38,855)
Denver: 82.8% (306,055)
Arapahoe: 6.7% (24,801)

-------------------------
### Largest County Turnout: Denver
-------------------------

Charles Casper Stockham: 23.0% (85,213)

Diana DeGette: 73.8% (272,892)

Raymon Anthony Doane: 3.1% (11,606)

-------------------------
### Winner: Diana DeGette
### Winning Vote Count: 272,892
### Winning Percentage: 73.8%
-------------------------
  
Attached is an image of the terminal print out: (https://user-images.githubusercontent.com/80140082/113513932-c1eda080-9520-11eb-87e9-b9198b347248.png)

   * The county with the largest vote was Denver with 82.8% (306,055) of the total votes.

   * Below is a summary of the number of votes and the percentage of the total votes each candidate received.
    
        * Charles Casper Stockham: 23.0% (85,213)
        * Diana DeGette: 73.8% (272,892)
        * Raymon Anthony Doane: 3.1% (11,606)

   * The winning candidate was Diana DeGette with 73.8% or 272, 892 of the total votes for the county.
    
Attached is a link to the elections_analysis.txt for the elections results.
https://github.com/Ha-Duong-88/Election_Analysis/blob/main/analysis/election_analysis.txt

# Election-Audit Summary

This Python elections audit analysis script can be leveraged for any elections with some minor modifcations. To enable re-use of the script, the following modifications to this script are proposed:

    1) Remove the print statements and only print to a text file to optimize the code run-time performance. 
    2) Modify the county name for state elections to state name for congressional elections.


