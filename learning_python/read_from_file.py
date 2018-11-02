file='index.html'
myfile=open(file, 'r')
for f in myfile:
    print(f.strip())