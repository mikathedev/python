import mode
import medienfinder
import commean
import mean
import commode
import commed

l = input('enter with a comma and space between')
l2 = input('enter the second with a comma and space between')

print("1. mean: "+str(mean.mean(l))+" medien: "+str(medienfinder.medein(l))+" mode: "+str(mode.mode(l)))
print("2. mean: "+str(mean.mean(l2))+" medien: "+str(medienfinder.medein(l2))+" mode: "+str(mode.mode(l2)))
print(commean.compare(mean.mean(l), mean.mean(l2))+" ", commode.compare(medienfinder.medein(l), medienfinder.medein(l2))+" ", commed.compare(mode.mode(l), mode.mode(l2))+" ")


