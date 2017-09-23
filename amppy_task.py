from time import time
def time_random():
    return time() - float(str(time()).split('.')[0])
def gen_random_range(min,max,frequency):
    mod=1
    lst=[]
    count=0
    while True:
        mod = min%max
        if count == frequency:
            break
        if ((int(str(time_random()).split('.')[1]) % max + mod) % max) !=0:
            print (int(str(time_random()).split('.')[1]) % max + mod) % max
        else:
            count -=1
        count += 1
        min += 1
    return lst
if __name__=="__main__":
    print "Plz enter the range"
    min=int(raw_input())
    max=int(raw_input())
    print "Plz enter the frequency"
    frequency=int(raw_input())
    print "Random Numbers"
    gen_random_range(min,max,frequency)
