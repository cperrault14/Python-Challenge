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