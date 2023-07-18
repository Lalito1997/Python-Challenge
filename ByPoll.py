#Importing the dependancies needed
import os
import csv

#Accessing the csv file 
pypoll_csv = os.path.join('python_challenge', 'Starter_Code', 'PyPoll', 'Resources', 'election_data.csv')

#Creaeting variables as well as the empty lists that will be used for analysis
#Starting the total votes and winner votes as zero as they will be increaseing rather than being stored in a list
total_votes = 0
candidates = {}
winner_votes = 0
winner = ""

#The with statement reads the csv file and preps it for the for loop where data is then extracted
with open(pypoll_csv, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)

    #This for loop is coutning the number of votes by counting down the row 
    #In row 2 we are then adding by one if its the same candidate being picked
    for row in csv_reader:
        total_votes += 1
        candidate = row[2]
        #In this if statment if the candidates name is the same as the row below it is then counted
        #Else we move on to teh next candidate in the for loop
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

#Creating an empty list of the results to later be called in the print stement
results = []

#In this for loop we are making a percenatage of the candidates vote to the total votes
#and append it by candidate, vote and percentage
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    results.append((candidate, votes, percentage))
    
    #From the for loop we are then able to do an if statment to make sure that we are choosign the candidate 
    #by having the vote be greater than the winning vote and diplaying the variables that are tied to the candidate
    if votes > winner_votes:
        winner_votes = votes
        winner = candidate

#With these print statments we are calling from the varibales we defined above
#The with open as file, I am able t0 pruint out the results of the code in a seperate file
with open('election_results.txt', 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for candidate, votes, percentage in results:
        file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")