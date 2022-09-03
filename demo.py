import wget
import os

#get the relevant email set from the file 'emailset.txt'
emailset=[]
fileobj=open("emailset.txt")
emailset=fileobj.read().split(',')
#print(lines)
for i in range(0,len(emailset)):
    emailset[i]=(emailset[i].replace("'","")).strip()

x = 38816


while(x<40000):
    if ("{0}.eml".format(x)) in emailset:
        url = f'https://file.wikileaks.org/file/podesta-emails/Maildir/cur/{x}.eml'
        filename = wget.download(url)
    x+=1

