#Import modules
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
​
​
#Initialize camera
camera = PiCamera()
camera.resolution = (320, 240)
camera.color_effects = (128, 128)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(320, 240))
​
#Let camera warm up
time.sleep(0.2)
​
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	img = frame.array
	cv2.imshow("Preview", img)
	
	rawCapture.truncate(0)
	
	key = cv2.waitKey(1)
	if key == ord("q"):
		print("Quitting")
		break
	
	
cv2.destroyAllWindows()
camera.close()

    e2=[0]*len(a)
    e3=[0]*len(a)
    e4=[0]*len(a)
    for i in range(0,len(a),2):
        #cc[a[i]][a[i+1]]=g
        #pp[-a[i+1]+b-1][a[i]]=g
        #kk[-a[i]+b-1][-a[i+1]+b-1]=g
        #mm[a[i+1]][-a[i]+b-1]=g
        
        e1[i]=a[i]
        e1[i+1]=a[i+1]
        e2[i]=-a[i+1]+b-1
        e2[i+1]=a[i]
        e3[i]=-a[i]+b-1
        e3[i+1]=-a[i+1]+b-1
        e4[i]=a[i+1]
        e4[i+1]=-a[i]+b-1
    return [pos(e1),pos(e2),pos(e3),pos(e4)]

def minn(a,b):
    c=0
    d=[]
    for i in range(b,len(a),2):
        d.append(a[i])
    return min(d)

def test(a):
    b=max(a[0])+1
    cc=[]
    pp=[]
    kk=[]
    mm=[]
    for i in range(b):
        cc.append([0]*b)
        pp.append([0]*b)
        kk.append([0]*b)
        mm.append([0]*b)
    for i in range(0,len(a[0]),2):
        cc[a[0][i]][a[0][i+1]]=4
        pp[a[1][i]][a[1][i+1]]=4
        kk[a[2][i]][a[2][i+1]]=4
        mm[a[3][i]][a[3][i+1]]=4
    for i in range(len(cc)):
        print(cc[i],"  ",pp[i],"  ",kk[i],"  ",mm[i])

def perm(a):
    return (itertools.product("0123", repeat=a))

def brute(grid,obj):
    gen=perm(len(obj))
    
def can(grid,obj,x,y,c):
    g=copy.deepcopy(grid)
    for i in range(0,len(obj),2):
        if((x+obj[i]>=len(grid)) or y+obj[i+1]>=len(grid[x])):
            return False
        elif(grid[x+obj[i]][y+obj[i+1]]!=0):
            return False
        g[x+obj[i]][y+obj[i+1]]=c 
    return g
#############################################################################
def f(grid,obj,gen):
    

    for i in gen:
        per=[]
        comb=itertools.permutations("0123")
        g=copy.deepcopy(grid)
        for u in range(len(obj)):
            per.append(obj[u][int(i[u])])
        for k in comb:
            for p in k:
                p=int(p)
                a=topleft(g,0)
                b=topleft(per[p],1)
                g=can(g,per[p],a[0]-b[0],a[1]-b[1],p+1)
                """
                if(k==('3', '2', '1', '0') and i==('3', '1', '2', '2')):
                    print(per)
                    print(a,b)
                    for h in g:
                        print(h)
                    print(g!=False)
                    print(p,k[len(k)-1])
                    print()
                """
                if(g!=False and int(p)==int(k[len(k)-1])):
                    return g
                elif(g==False):
                    g=copy.deepcopy(grid)
                    break

#############################################################################

abc=[]
k=[]
p=[]
abc2=[]
x,i=0,0
filename = sys.argv[1]
#filename = "ubongo.txt"
e = (open(filename, "r" ))
cc=e.readline()
p=cc.split()
while (i<int(p[0])):
    k=list(map(int, e.readline().split()))
    abc.append(k)
    i+=1
    #print(k)
    k=[]
i=0
while (1<2):
    i+=1
    cc=e.readline()
    k=cc.split()
    if(k=="" or cc==" " or cc==""):
        break;
    p=[0]*len(k)
    x=int(minn(k,0))
    for u in range(0,len(k),2):
        p[u]=int(k[u])-x
    x=int(minn(k,1))
    for u in range(1,len(k),2):
        p[u]=int(k[u])-x
    abc2.append(turn(p,i))
    k=[]
'''
for i in abc2:
    print(i)
    print()
print()
print()

for i in range(len(abc2)):
    test(abc2[i])
    print()
print("-------------------------------------------------------")
'''

#a=f(abc,abc2,perm(len(abc2)))
'''
if (a==None):
    print(-1,-1,-1,4,5,6)
    print(-1,-1,3,4,5,6)
    print(1,2,3,4,5,6)
    print(1,2,3,4,5,6)
    print(1,2,3,4,5,-1)
    print(-1,-1,3,4,5,-1)
    '''
p=1
for i in abc:
    for k in range(len(i)):
        if i[k]==0:
            i[k]=p
        p+=1
    p=1
for i in abc:
    for k in i:
        print(k," ",end="")
    print()



#test(abc2[3])


