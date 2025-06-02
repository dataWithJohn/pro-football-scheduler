#!/usr/bin/python3
import os
#import shuffle
#import makeAWeek



if os.path.exists('stop.fil'):
    os.remove('stop.fil')



os.system('cls' if os.name == 'nt' else 'clear')

attempt = 1
while True:
    if os.path.exists('matchups-shuffled.fil'):
        os.remove('matchups-shuffled.fil')

    verbage = "Attempt #" + str(attempt)
    print(verbage)

    # Define the range for x from 1 to 400
    for x in range(1, 401):
        # Execute shuffle.py
        os.system("./shuffle.py")
        #shuffle.main()
        
        # Execute makeAWeek.py
        os.system("./makeAWeek.py")
        #result = makeAWeek.returnStatus() 
       
        #print(result)
        #if (result == "success"):
        #    exit()
        #elif (result == "fail"):
        #    if os.path.exists('matchups-shuffled.fil'):
        #        os.remove('matchups-shuffled.fil')
        if os.path.exists('stop.fil'):
            exit()
        ### LEFT OFF HERE
        ###exit()

    attempt = attempt + 1
