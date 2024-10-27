import numpy as np
import pandas as pd

matches = pd.read_csv(r"/home/soham-saxena/Downloads/matches.csv")
print(f"Number of matches conducted on 2008: {len(matches[matches['season'] == 2008])}")
print(f"City with maximum count: {matches['city'].value_counts().idxmax()}\nCity with minimum count: {matches['city'].value_counts().idxmin()}")
print("Total count of matches city wise:\n")
print(matches['city'].value_counts())
print(f"Team with maximum toss wins: {matches['toss_winner'].value_counts().idxmax()}\nTeam with minimum toss wins: {matches['toss_winner'].value_counts().idxmin()}")
print("Toss decisions taken by teams:")
print(matches[['toss_winner', 'toss_decision']])
print(matches['result'].value_counts())
print(matches.loc[matches['result'] == 'tie'][['team1', 'team2', 'result']])
print(f"Team who won match by highest runs: {matches.iloc[matches['win_by_runs'].idxmax()]['winner']}\nTeam who won by least runs: {matches.iloc[matches['win_by_runs'].idxmin()]['winner']}")
player_of_match = matches['player_of_match'].value_counts()
print(f"Players who were awarded player of the match more than 3 times:\n{player_of_match.loc[player_of_match[:] > 3]}")
print(f"Player who was awared highest: {player_of_match.idxmax()}")
print(f"Venue where highest runs was made: {matches.iloc[matches['win_by_runs'].idxmax()]['venue']}")
print(f"Venue where minimum runs was made: {matches.iloc[matches['win_by_runs'].idxmin()]['venue']}")
print(f"Umpires who did umpiring the maximum times: {(matches['umpire1'].value_counts() + matches['umpire2'].value_counts() + matches['umpire3'].value_counts()).idxmax()}")
print(f"Total matches played in each season:\n{matches['season'].value_counts()}")
# print(f"Total number of runs in each season:\n{matches[['season', 'win_by_runs']]}")
print(f"Number of tosses won by each team:\n{matches['toss_winner'].value_counts()}")
print(f"Total number of matches for each time:\n{matches['team1'].value_counts() + matches['team2'].value_counts()}")
total = matches['team1'].value_counts() + matches['team2'].value_counts();
winners = matches['winner'].value_counts()
win_rate = winners*100/total
print(f"Winrate of the teams:\n{win_rate}")