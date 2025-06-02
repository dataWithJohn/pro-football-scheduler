#!/usr/bin/python3

import os
import random
import shutil

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def read_matchups_file(filename):
    matchups = []
    with open(filename, 'r') as file:
        for line in file:
            fields = line.strip().split(':')
            if len(fields) == 5:
                matchups.append({
                    'randNum': format(random.uniform(0, 1), '.12f'),
                    'unknown': fields[1],
                    'team1': fields[2],
                    'vs/at': fields[3],
                    'team2': fields[4]
                })
            else:
                print(f"Illegal format detected in line: {line}")
    return matchups

if os.path.exists('matchups2.fil'):
   os.remove('matchups2.fil')

if os.path.exists('matchups3.fil'):
   os.remove('matchups3.fil')

# Check if matchups-shuffled.fil exists, if not use matchups.fil
filename = 'matchups-shuffled.fil' if os.path.exists('matchups-shuffled.fil') else 'matchups.fil'
matchups = read_matchups_file(filename)

# Write new records to matchups2.fil
with open('matchups2.fil', 'w') as outfile:
    for matchup in matchups:
        outfile.write(f"{matchup['randNum']}:{matchup['unknown']}:{matchup['team1']}:{matchup['vs/at']}:{matchup['team2']}\n")

#clear_screen()
#print("New records written to matchups2.fil")

# Read matchups2.fil, sort its contents, and write to matchups3.fil
with open('matchups2.fil', 'r') as infile:
    lines = infile.readlines()

# Sort the lines based on the randNum field
sorted_lines = sorted(lines, key=lambda x: float(x.split(':')[0]))

# Write sorted lines to matchups3.fil
with open('matchups3.fil', 'w') as outfile:
    outfile.writelines(sorted_lines)

#print("Contents of matchups2.fil sorted and written to matchups3.fil")
# Remove matchups2.fil
os.remove('matchups2.fil')

# Rename matchups3.fil to matchups-shuffled.fil
shutil.move('matchups3.fil', 'matchups-shuffled.fil')

#print("matchups2.fil deleted and matchups3.fil renamed to matchups-shuffled.fil")
#print("matchups shuffled")
