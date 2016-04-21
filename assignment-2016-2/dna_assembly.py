import random
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('filename', help='name file',default='fragments_file.txt')

args = parser.parse_args()


f=open(args.filename)
f=open(args.filename)
#ftiaxnw lista me ta gonidiwmata
edge=[]
for line in f:
    parts=line.split()
    edge.append(parts)

k=len(edge[0][0])
#apaleifw tis diplotimes ap th lista kai metraw grammes
gram=0
newedge=[]
for i in edge:
    if i not in newedge:
        gram=gram+1
        newedge.append(i)

#ftiaxnw leksiko me thn akolouthia
neighbours=dict()
for i in newedge:
    parts1=i[0][:(k-1)]
    parts2=i[0][1:k]
    neighbours.setdefault(parts1,[])
    neighbours[parts1].append(parts2)

#ftiaxnw thn allhlouxia tou dna
star = random.choice(newedge)
gal = star[0][1:k]
start= star[0][:]
dna=[]
doubles=[]
flag=True
x=0
metr=0
startfound=False
dnastr='-'
first=0
while flag==True:
    for keys in neighbours:
        if x==(gram):
            flag=False
        if flag==True:
            if keys==gal:

                l=0
                for values in neighbours[keys]:
                    if ((keys[0]+values) not in dna) and ((keys[0]+values) not in doubles) and l>0:
                        doubles.append(keys[0]+values)
                    if ((keys[0]+values) not in dna) and l==0:
                        dna.append(keys[0]+values)
                        x=x+1
                        dnastr=dnastr+values+'-'
                        l=l+1
                        gal=values
                        starstar=1
                        if ((keys[0]+values) in doubles):
                            doubles.remove(keys[0]+values)


                if start in dna:
                    startfound=True
        if startfound==True:
            starstar=0
            startfound=False
            if first==0:
                dnastring=dnastr
                dnastr=''

            else:
                dnastr=start[1:k]+'-'+dnastr[0:-(k)]
                index = start[0:(k-1)]+'-'
                hrs, mins = dnastring.split(index)
                dnastring=hrs+index+dnastr+mins
                dnastr=''
            if len(doubles)>0:
                star=doubles[-1]
                start=str (star)
                gal=start[1:k]

            first=1
print (dnastring[(k-1)::k])
