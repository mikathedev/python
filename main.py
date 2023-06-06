import mode
import medienfinder
import range
import mean
i = input("1 mode, 2 medin, 3 range")
l= input('enter with a comma and space between')

if i == '1':
    print(mode.mode(l))
elif i=='3':
    print(range.a(l))

elif i == '4':
    print(mean.mean(l))
else :
    print(medienfinder.medein(l))

