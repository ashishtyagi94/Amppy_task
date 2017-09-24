# Amppy_task
    mod=1 # for modular division
    count=0 # used to terminate the loop
    higher_frequency=0 # For biased higher number than mid(Explained below)
    lower_frequency=0  # For lesser number than mid
    high_counter=0
    low_counter=0
    mid = max/2 # Midiator of range given  
    higher_frequency = int((frequency * 73)/100) # Calculated 73 % biased for higher number
    lower_frequency = frequency - higher_frequency # Calculated 27 % biased for lesser number
    rnd =(int(str(time_random()).split('.')[1]) % max + mod) % max # Calculated random number b/w a given range
    if rnd == 0:# Skipped Zero if exist during calculating modular division 
    if count == frequency: # Terminated condition
    if rnd > mid and higher_frequency > high_counter:# biased condition for higher number than mid
    elif rnd < mid and lower_frequency > low_counter:# biased condition for lesser number than mid
    return time() - float(str(time()).split('.')[0])# Calculating time quanta
