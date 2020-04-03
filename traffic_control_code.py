import cv2
import time
import numpy as np
font                   = cv2.FONT_HERSHEY_SIMPLEX    # ? 
bottomLeftCornerOfText = (20,220)   # ? 
fontScale              = 1
fontColor              = [(0,0,255),(0,255,0)]   # ? 
lineType               = 2

'''def signallogic(signal):
    if(signal.elapsedtime>2):
        signal.red=0
        signal.green=1
    elif(signal.evaluation>2):
        signal.red=0
        signal.green=1

        
    return signal     
   
'''
class Signallight:
    def __init__(self, name,red,green):
        self.name =name 
        self.green=green
        self.red=red
        self.orange=0
        self.evaluation=0
        self.fps=1;
        self.elapsedtime=0;
        self.releasetime=-1;
        self.maxreleasetime=20;
        self.vehiclescount=0;
        self.starttime=time.time()
    def setgreen(self,green):
        self.green=green
    def setgred(self,red):
        self.red=red
    def incfps(self):
        self.fps=self.fps+1 
    def incelapsed(self,delta):
        self.elapsedtime=self.elapsedtime+delta      
    def decrelease(self,delta):
        self.releasetime=self.releasetime-delta  
    def display(self):
      print(self.name,self.red,self.green,self.releasetime,self.vehiclescount,self.elapsedtime,self.maxreleasetime)
    def setreleasetime(self):
       self.releasetime=4+self.vehiclescount
       self.maxreleasetime=self.releasetime

starttime=time.time()
delta=0;
elapsed=starttime
mylist = []#array holding signal lights
car_cascade = cv2.CascadeClassifier('cars.xml') 
mylist.append(Signallight("path1",1,0))## adding four signal lights to array with default (red,green
mylist.append(Signallight("path2",1,0))## adding four signal lights to array
mylist.append(Signallight("path3",1,0))## adding four signal lights to array
mylist.append(Signallight("path4",0,1))## adding four signal lights to array

while (mylist[0].fps<500 and mylist[1].fps<500 and mylist[2].fps<500 and mylist[3].fps<500):
 delta=time.time()-elapsed
 elapsed=elapsed+delta
 image = cv2.imread(str(mylist[0].fps)+'.png')
 image1 = cv2.imread(str(mylist[1].fps)+'.png')
 image2 = cv2.imread(str(mylist[2].fps)+'.png')
 image3 = cv2.imread(str(mylist[3].fps)+'.png')

 gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
 gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
 gray3 = cv2.cvtColor(image3, cv2.COLOR_BGR2GRAY)
 
 cars = car_cascade.detectMultiScale(gray, 1.1, 1) 
 cars1 = car_cascade.detectMultiScale(gray1, 1.1, 1) 
 cars2 = car_cascade.detectMultiScale(gray2, 1.1, 1) 
 cars3 = car_cascade.detectMultiScale(gray3, 1.1, 1) 
 
 count=0;
 for (x,y,w,h) in cars: 
  cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
  count=count+1
 mylist[0].vehiclescount=count
 #mylist[0].setevaluation()
 count=0;
 for (x,y,w,h) in cars1: 
  cv2.rectangle(image1,(x,y),(x+w,y+h),(0,0,255),2)
  count=count+1
 mylist[1].vehiclescount=count
 #mylist[1].setevaluation()
 count=0;
 for (x,y,w,h) in cars2: 
  cv2.rectangle(image2,(x,y),(x+w,y+h),(0,0,255),2)
  count=count+1
 mylist[2].vehiclescount=count
# mylist[2].setevaluation()
 count=0;
 for (x,y,w,h) in cars3: 
  cv2.rectangle(image3,(x,y),(x+w,y+h),(0,0,255),2)
  count=count+1
 mylist[3].vehiclescount=count
 #mylist[3].setevaluation()
 for x in range(0, 4):
   
  if(mylist[x].red>0):
     mylist[x].incelapsed(delta)
     #print('red')
  else:
     mylist[x].incfps() 
     #signal.red
     if(mylist[x].releasetime>0):
       print(mylist[x].releasetime) 
       mylist[x].decrelease(delta)
       if(mylist[x].releasetime<2):
           #print('orange'+str(mylist[x].maxreleasetime-mylist[x].releasetime)+"relt"+str(mylist[x].maxreleasetime))
           mylist[x].orange=1
       else:
           mylist[x].orange=0
     else:
       mylist[x].red=1;
       mylist[x].green=0;
       if(x<3):
        mylist[x+1].red=0;
        mylist[x+1].green=1;
        mylist[x+1].setreleasetime()
        mylist[x+1].display()
       else:
        mylist[0].red=0;
        mylist[0].green=1;
        mylist[0].releasetime=2;
        mylist[0].setreleasetime()
        mylist[0].display()           

       
 if (type(image) == type(None)):
        break
 if (type(image1) == type(None)):
        break   

 
 cv2.circle(image,(10,10), 10, (0,mylist[0].green*255-mylist[0].orange*50,mylist[0].red*255+mylist[0].orange*255), -1)
 cv2.putText(image,str(int(1+mylist[0].releasetime)),(280,30), font, 1,(255,255,0),2,cv2.LINE_AA)
 
 cv2.circle(image1,(10,10), 10, (0,mylist[1].green*255-mylist[1].orange*50,mylist[1].red*255+mylist[1].orange*255), -1)
 cv2.putText(image1,str(int(1+mylist[1].releasetime)),(280,30), font, 1,(255,255,0),2,cv2.LINE_AA)
 
 cv2.circle(image2,(10,10), 10, (0,mylist[2].green*255-mylist[2].orange*50,mylist[2].red*255+mylist[2].orange*255), -1)
 cv2.putText(image2,str(int(1+mylist[2].releasetime)),(280,30), font, 1,(255,255,0),2,cv2.LINE_AA)
 
 cv2.circle(image3,(10,10), 10, (0,mylist[3].green*255-mylist[3].orange*50,mylist[3].red*255+mylist[3].orange*255), -1)
 cv2.putText(image3,str(int(1+mylist[3].releasetime)),(280,30), font, 1,(255,255,0),2,cv2.LINE_AA)
 
 numpy_horizontal1 = np.hstack((image1, image))
 numpy_horizontal2 = np.hstack((image2, image3))
 numpy_vertical = np.vstack((numpy_horizontal1, numpy_horizontal2))
 cv2.imshow('four',numpy_vertical)


 starttime=time.time()
 if cv2.waitKey(33) == 27:
        break
 

cv2.destroyAllWindows()

