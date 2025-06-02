#!/usr/bin/python3

import os

def write_to_temp_file(record):
    with open('temp1.fil', 'a') as f:
        second_field = str(record[1]).zfill(3)
        if second_field != "00?":
           f.write(f"{second_field}:{record[2]}:{record[3]}:{record[4]}\n")
    
def read_temp_file(filename):
    records = []
    with open(filename, 'r') as f:
        for line in f:
            fields = line.strip().split(':')
            records.append(fields)
    return records

def write_to_temp_file2(records, filename):
    with open(filename, 'w') as f:
        for record in records:
            f.write(':'.join(record) + '\n')

def read_schedule(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return [line.strip().split(':') for line in lines]

def write_schedule(schedule, output_filename):
    # Compute number of weeks to print
    lastWeekToPrint = 1
    while True:
        count = 0
        with open('matchups-shuffled.fil', 'r') as matchups_file:
            matchups = matchups_file.readlines()

            # Loop through each record in matchups
            for matchup in matchups:
                fields = matchup.split(':')
                fields[1] = fields[1].strip()

                if (fields[1] != "?"):
                    if (int(fields[1]) == int(lastWeekToPrint)):
                        count = count + 1

        if (count == 0):
            break
        else:
            lastWeekToPrint = lastWeekToPrint + 1
     
    lastWeekToPrint = lastWeekToPrint - 1



    with open(output_filename, 'w') as file:
        current_week = None
        for item in schedule:
            week, team1, _, team2 = item
            week = int(week)  # Convert week number to integer to remove leading zeros
            if ((week != current_week) and (week <= lastWeekToPrint)):
                current_week = week
                if week == 1:
                   file.write(f"Week {week}\n======\n")
                elif week < 10:
                   file.write(f"\n\n\nWeek {week}\n======\n")
                elif week < 100:
                   file.write(f"\n\n\nWeek {week}\n=======\n")
                else:
                   file.write(f"\n\n\nWeek {week}\n========\n")
            if (int(week) <= int(lastWeekToPrint)):
               file.write(f"{team1} at {team2}\n")

def main():

    # Make sure these files are gone before beginning
    if os.path.exists('temp1.fil'):
       os.remove('temp1.fil')
    if os.path.exists('temp2.fil'):
       os.remove('temp2.fil')
    if os.path.exists('msPrint1.fil'):
       os.remove('msPrint1.fil')
    if os.path.exists('msPrint2.fil'):
       os.remove('msPrint2.fil')

    # Make another copy of the byes file for the printout
    with open('byes.fil', 'r') as byes_file:
         byes = byes_file.readlines()

         for bye in byes:
             fields = bye.split(':')

             fields[0] = fields[0].strip()
             fields[1] = fields[1].strip()

             recordLine = ".999:" + fields[0] + ":zzzbye:trash:" + fields[1]

             # Open priorOpponent.fil in append mode
             msPrint2_file = open('msPrint2.fil', 'a')
             # Append a record to msPrint2.fil
             msPrint2_file.write(f"{recordLine}\n")
             # Close msPrint2.fil file
             msPrint2_file.close()
 
    ### LEFT OFF HERE
    os.system("sort msPrint2.fil > msPrint2-sorted.fil")
    os.system("mv msPrint2-sorted.fil msPrint2.fil")
    ### /\
    os.system("cp matchups-shuffled.fil msPrint1.fil")
    os.system("cat msPrint2.fil >> msPrint1.fil")

    #with open('matchups-shuffled.fil', 'r') as f:
    with open('msPrint1.fil', 'r') as f:
        for line in f:
            fields = line.strip().split(':')
            write_to_temp_file(fields)

            # Read from temp1.fil
            records = read_temp_file('temp1.fil')

            # Sort records based on the second field
            sorted_records = sorted(records, key=lambda x: (x[0], x[1]))
            #sorted_records = sorted(records, key=lambda x: int(x[1]))

            # Write sorted records to temp2.fil
            write_to_temp_file2(sorted_records, 'temp2.fil')

    input_filename = 'temp2.fil'
    output_filename = 'final-schedule.fil'

    schedule = read_schedule(input_filename)
    write_schedule(schedule, output_filename)

    os.system("sed 's/zzzbye at/bye:/g' final-schedule.fil > tempSched.fil") 
    os.system("mv tempSched.fil final-schedule.fil")
    print("Schedule generated successfully!")

    ### LEFT OFF HERE
    exit()

    # Make sure these files are gone -- cleanup
    if os.path.exists('temp1.fil'):
       os.remove('temp1.fil')
    if os.path.exists('temp2.fil'):
       os.remove('temp2.fil')
    if os.path.exists('msPrint1.fil'):
       os.remove('msPrint1.fil')
    if os.path.exists('msPrint2.fil'):
       os.remove('msPrint2.fil')

if __name__ == "__main__":
    main()
