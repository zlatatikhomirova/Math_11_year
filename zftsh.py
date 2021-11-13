def sign(n):
    if n > 0:
        return '+'
    elif n < 0:
        return '-'
    else:
        return '0'

def get_roots():
	breaker = 1
	roots = []
	while breaker:
	    a = int(input('a    '))
	    b = int(input('b    '))
	    c = int(input('c    '))
	    d = b*b - 4*a*c
	    if d>=0:
	        if not d**0.5%1:
	            print(f'x1 = {(-b-d**0.5)/(2*a)}')
	            print(f'x2 = {(-b+d**0.5)/(2*a)}')
	            roots.append((-b-d**0.5)/(2*a))
	            roots.append((-b+d**0.5)/(2*a))
	        else:
	            print(f'x1 = ({-b}-sqrt({d}))/{2*a}')
	            print(f'x2 = ({-b}+sqrt({d}))/{2*a}')
	    else:
	        print('no roots')
	    breaker = input("Continue doing it?  (0/1)")
	return sorted(roots)
	    

"""# Boundaries"""
def get_boundaries():
	breaker = 1
	while breaker>0:
	    x = float(input('the boundary  '))
	    upp = (2*x-1)*((2*x - 3)**2)
	    down = (x-2)*(2*x+1)
	    print(sign(upp/down))
	    breaker = input("Continue doing it?  (0/1)")
def calculations():
	breaker = 1
	while breaker:
		exec(input())
		breaker = input("Continue doing it?  (0/1)")
		
		
		
get_roots()
		