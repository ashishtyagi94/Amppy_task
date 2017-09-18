def power(base,exp):
	if(exp==1):
		return(base)
	if(exp!=1):
		return(base*power(base,exp-1))
def factor(fact):
	if fact == 1:
		return 1
        elif fact ==0:
                return 1
        else:
                return fact * factor(fact-1)	
if __name__=="__main__":
	base=int(input("Enter base: "))
	exp=int(input("Enter exponential value: "))
	print("Result:",power(base,exp))
        print(factor(5))

