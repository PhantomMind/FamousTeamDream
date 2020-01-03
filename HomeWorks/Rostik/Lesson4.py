
import random
s = "1234567890-=+_)(*&^%$#@!QWERTYUIOPASDFGHJKLZCVN,./qwertyuiopasdfghjklzxcvbnm[];'{}:"
psw = ""
for x in range(5):
    psw += random.choice(s)
print(psw)

try:
    f = open('passwords.txt', 'a')
except IOError as e:
    f = open('passwords.txt', 'w')
finally:
    f.writelines(psw)
    f.write('\t')
    f.writelines('Adsd')
    f.write('\n')
f.close()