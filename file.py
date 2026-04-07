import os
print(os.getcwd())
fp=open('sample.txt','w+')
fp.write('We are learning python')
print(fp.read())
fp.close()
