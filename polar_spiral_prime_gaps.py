"""This is a basic sacks spiral using polar coordinates, investigating prime gaps
Youll need the python pyx package installed."""


from pyx import *
from math import cos, sin, log, sqrt, pi

#inspired by work from http://www.dcs.gla.ac.uk/~jhw/spirals/

n = 100000 #all primes less than this number
ca = canvas.canvas()

# This prime function is taken from William Stein's ent package. 
def primes(n):
    if n <= 1: return []
    X = [i for i in range(3,n+1) if i%2 != 0]     # (1)
    P = [2]                                       # (2)
    sqrt_n = sqrt(n)                              # (3)
    while len(X) > 0 and X[0] <= sqrt_n:          # (4)
        p = X[0]                                  # (5)
        P.append(p)                               # (6)
        X = [a for a in X if a%p != 0]            # (7)
    return P + X                                  # (8)

all_primes = primes(n)

for j in range(len(all_primes)):
	first = all_primes[j]
	if j+2 <= len(all_primes):
		second = all_primes[j+1]
	else:
		break
	d = second - first
	r = sqrt(j)
	theta = r * 2 * pi
	x = cos(theta)*r
	y = -sin(theta)*r
	# -- here are some radius functions, you can play with them, or add more.
	radius = 0.1 * sqrt(d)
	#radius = 0.1 * log(d)
	ca.fill(path.circle(x,y,radius))

d = document.document(pages = [document.page(ca, paperformat=document.paperformat.A4, fittosize=1)])
d.writePSfile("prime_gaps_spiral.ps")