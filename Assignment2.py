#%%
# question1

def computepay(h,r):
    if h <= 40: 
        Payment = h * r
    elif h > 40:
        Pay = 40 * r + (h-40) * r * 1.5
        return Payment

hrs = input('Enter Hours:')
h=float(hrs)
rate = input('Enter Rate:')
r=float(rate)

Payment=computepay(h,r)
print(Payment)
#%%

# question2
score = input("Enter Score: ")
s =  float(score)
x = 'Error'
if s >= 0.9 and s<1:
	x = 'A'
elif s >=0.8:
	x='B'
elif s >=0.7:
	x='C'
elif s >= 0.6:
	x='D'
elif s < .6:
	x ='F'
else:
	x ="Out of Range"
print (x)
#%%
