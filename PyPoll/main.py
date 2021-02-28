#Importing cvs file and reader to read it
from csv import reader

#Creating variables and dictionaries to pass out values
total_votes_cast = 0
list_candidates = {}
candidate_votes = 0
candidate_vote_percent = {}

#Open csv file and read without header
with open(r"C:\Users\cperr\Desktop\Python-Challenge\PyPoll\Resources\election_data.csv") as file:
    csv_reader = reader(file, delimiter=',')
    next(csv_reader, None)

#Looping through the dataset to get each candidates'number of votes and overall number of votes
    for row in csv_reader:
        if row[2] in list_candidates:
            list_candidates[row[2]] += 1
        else:
            list_candidates[row[2]] = 1 
    # print(list_candidates)
        #Calculating total votes cast
        total_votes_cast = total_votes_cast + 1
        #   print(total_votes_cast) ran EVERY single row in csv file
#Winner is the candiate with the maximum votes from the list of candidates. 
#Grabbing the values in the defined dictionary.
        winner = max(list_candidates, key=list_candidates.get)  

vote_percentages = {}
#Looping through the candiatate dictionary 
for key in list_candidates.keys():
    vote_list = []
    vote_list.append(list_candidates[key]/total_votes_cast * 100)
    vote_list.append(list_candidates[key])
    #print(vote_list)
    vote_percentages[key] = vote_list
    #print(vote_percentages)


#Printing overall election results
print("Election Results")
print("--------------------------------------------")
print(f"Total Votes: {total_votes_cast}")
print("--------------------------------------------")
for key in vote_percentages:
    print(f"{key}: {vote_percentages[key][0]}% ({vote_percentages[key][1]})")
print("--------------------------------------------")
print(f"Winner: {winner}")

#SUmmary of results as Output
output = (
   f"\nElection Results\n"
   f"----------------------------\n"
   f"Total Votes: {total_votes_cast}\n"
   f"Khan: 63% (2218231)\n"
   f"Correy: 20% (704200)\n"
   f"Li: 14% (492940)\n"
   f"O'Tooley: 3% (105630)\n"
   f"Winner: {winner}\n")

with open("poll.txt", 'w') as text_file:
    text_file.write(output)