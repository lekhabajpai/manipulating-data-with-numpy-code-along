# --------------
import numpy as np
from collections import Counter
# Not every data format will be in csv there are other file formats also.
# This exercise will help you deal with other file formats and how toa read it.
data_ipl = np.genfromtxt(path, delimiter=',', skip_header=1, dtype=str)
#print(data_ipl[:,3])

# How many matches were held in total we need to know so that we can analyze further statistics keeping that in mind.
match_code_array = data_ipl[:,0]
match_code_list = []
for i in match_code_array:
    if (i not in match_code_list):
        match_code_list.append(i)
print(len(match_code_list))

num_unique_matches = len(set(match_code_array))
print('The number of unique matches', num_unique_matches)

# this exercise deals with you getting to know that which are all those six teams that played in the tournament.
team1 = set(data_ipl[:,3])
team2 = set(data_ipl[:,4])
unique = team1.union(team2)
print('The set of all unique team that played:', unique)

# An exercise to make you familiar with indexing and slicing up within data.
extras = data_ipl[:,17]
extras_num = extras.astype(int)
tot_extras = sum(extras_num)
print('The no of extras in all matches:', tot_extras)

# Get the array of all delivery numbers when a given player got out. Also mention the wicket type.
player_filter = (data_ipl[:,-3] == 'S R Tendulkar')
filtered_ipl = data_ipl[player_filter]
delivery_num = filtered_ipl[:,-12]
wicket_type = filtered_ipl[:,-2]
print('The no of deliveries where Tendulkar got out', delivery_num)
print('The ways Tendulkar got out :', wicket_type)

# this exercise will help you get the statistics on one particular team
toss_winner_mask = (data_ipl[:,5] == 'Mumbai Indians')
toss_winner_data = data_ipl[toss_winner_mask]
unique_matches = set(toss_winner_data[:,0])
num_toss_winner_MI = len(unique_matches)
print('The no of matches MI won the toss:', num_toss_winner_MI)

# An exercise to know who is the most aggresive player or maybe the scoring player 
in_runs_six = (data_ipl[:,-7] == '6')
data_ipl_filtered = data_ipl[in_runs_six]
batsmans_sixes = data_ipl_filtered[:,-10]
batsman_count = Counter(batsmans_sixes)
print(batsman_count)
 





