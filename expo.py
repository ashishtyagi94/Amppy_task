from time import time
def power(base,exp):
	if(exp==1):
		return(base)
	if(exp!=1):
		return(base*power(base,exp-1))
def time():
	return time()	
if __name__=="__main__":
	print(time())
	#for i in range(1,11):
	#	for j in range(1,11):print("Result:",power(i,j))

