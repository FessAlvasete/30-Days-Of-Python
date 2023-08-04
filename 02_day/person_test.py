a=0
b=0
for i in range(0,101,1):
    if i % 2 == 0:
        a+=i
    else:
        b+=i

print("Evenes sum: ", a)
print('Odds sum: ', b)