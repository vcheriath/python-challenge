#PyPoll Main File
#Rutgers DataScience Bootcamp
#Module 3 Homework
#By: Vigneshwar Cheriath

#Task:
#Analyze poll data called 'election_data.csv'
#Calculate:
#-total number of votes cast
#-complete list of candidates who recieved votes
#-percentages of votes each candidate won
#-total number of votes each candidate won
#-thewinner of the election based on the popular vote

#-----------------------------------------------------------------------------------------------

#import os & csv
import os
import csv

#read the election_data
csvpath = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')

#initialize totalVotes
totalVotes = 0

#initialize CandidateList
CandidateList = {}

#initialize winner
winner = ''

with open(csvpath) as csvfile:

	#specify delimiter and variable that holds data
	csvreader = csv.reader(csvfile, delimiter=',')

	#read the header first
	csv_header = next(csvreader)

	#loop through each row
	for row in csvreader:
		#increment the totalVotes
		totalVotes += 1

		#initialize variable inList to see if the candidate is in the list
		inList = False
		#if CandidateList is empty, add candidate w/ 1 vote
		if len(CandidateList) == 0:
			CandidateList.update({row[2]:1})
		else:
			#if CandidateList is not empty check if candidate is in candidate list
			for candidate in CandidateList.keys():
				if candidate == row[2]:
					inList = True
			if inList:
				#if the candidate is in the list, add 1 to their vote total
				CandidateList[row[2]] += 1
			else:
				#if the candidate is not in the list, add them to the list w/ a vote total of 1
				CandidateList.update({row[2] : 1})
				

#print header
print('Election Results' + '\n')
print('-------------------------' + '\n')
print(f'Total Votes: {totalVotes}' + '\n')
print('-------------------------' + '\n')
#loop through the CandidateList to print all the candidates, their percentages of the vote, and their vote totals
for candidate in CandidateList.keys():
	print(f'{candidate}: {round((CandidateList[candidate] / totalVotes) * 100, 3)}% ({CandidateList[candidate]})' + '\n')
	#determine the winner
	if winner == '' or CandidateList[winner] < CandidateList[candidate]:
		winner = candidate
print('-------------------------' + '\n')
print(f'Winner: {winner}' + '\n')
print('-------------------------')

#create output file path
output_file = os.path.join('..', 'PyPoll', 'analysis',"results.txt")

#open file to write
output = open(output_file, "w")

#write out results
output.write('Election Results' + '\n')
output.write('-------------------------' + '\n')
output.write(f'Total Votes: {totalVotes}' + '\n')
output.write('-------------------------' + '\n')
#loop through the CandidateList to print all the candidates, their percentages of the vote, and their vote totals
for candidate in CandidateList.keys():
	output.write(f'{candidate}: {round((CandidateList[candidate] / totalVotes) * 100, 3)}% ({CandidateList[candidate]})' + '\n')
	#determine the winner
	if winner == '' or CandidateList[winner] < CandidateList[candidate]:
		winner = candidate
output.write('-------------------------' + '\n')
output.write(f'Winner: {winner}' + '\n')
output.write('-------------------------')