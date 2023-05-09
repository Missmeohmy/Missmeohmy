#This program will prompt the user for hours and rate per hour using input to compute gross pay#
def computepay(h, r):
    return (h*r)+((h-40)*(r*0.5))

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
realhours = float(hrs)
realrate = float(rate)
if realhours <=40:
    x = realhours * realrate
    print("Pay", x)
else:
    p = computepay(realhours, realrate)    
    print("Pay", p)