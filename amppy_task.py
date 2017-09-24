from time import time # We have to take system time for calculation 
def time_random():
    return time() - float(str(time()).split('.')[0]) # Calculating time quantum
def gen_random_range(min,max,frequency):
    mod=1
    count=0 # used to terminate the loop
    higher_frequency=0 # For biased higher number than mid(Explained below)
    lower_frequency=0  # For lesser number than mid
    high_counter=0
    low_counter=0
    while True:
        mod = min%max
        mid = max/2 # Midiator of range given  
        higher_frequency = int((frequency * 73)/100) # Calculated 73 % biased for higher number
        lower_frequency = frequency - higher_frequency # Calculated 27 % biased for lesser number
        rnd =(int(str(time_random()).split('.')[1]) % max + mod) % max # Calculated random number b/w a given range
        if rnd == 0:# Skipped Zero if exist during calculating modular division 
            continue
        if count == frequency: # Terminated condition
            break
        if rnd > mid and higher_frequency > high_counter:# biased condition for higher number than mid
            print rnd
            high_counter +=1
            count += 1 
        elif rnd < mid and lower_frequency > low_counter:# biased condition for lesser number than mid
            print rnd
            low_counter +=1
            count += 1     
        min += 1
    print "Here the frequency of numbers Greater than" ,mid,"is = ",higher_frequency
    print "Here the frequency of numbers Less than " ,mid,"is = ",lower_frequency
if __name__=="__main__":
    print "Plz enter the range"
    min=int(raw_input())
    max=int(raw_input())
    print "Plz enter the frequency"
    frequency=int(raw_input())
    print "Random Numbers"
    gen_random_range(min,max,frequency)

