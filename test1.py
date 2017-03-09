import cv2
from matplotlib import pyplot as plt
import numpy as np
from Tkinter import Tk, Label, Button

img = cv2.imread('E:/My Photoes/RMORA@TRICO/2015-12-19-12-26-26-528.jpg',cv2.IMREAD_UNCHANGED)
cv2.namedWindow("image",cv2.WINDOW_NORMAL)  
cv2.imshow('image',img)  
def nothing():
    pass

def ColorTemp(*void):
    valueG = cv2.getTrackbarPos('Green','image') 
    valueR = cv2.getTrackbarPos('Red','image') 
    valueB = cv2.getTrackbarPos('Blue','image') 
    
    B,G,R = cv2.split(img)
    
    if(valueG>255):
        valueG=valueG-255
        valueG2= (255- valueG)/255.0
        X = np.multiply(G,valueG2)
        G = np.add(valueG,X)
        G=np.uint8(G)
    else:
        value2= (valueG)/255.0
        G = np.multiply(value2,G)
        G=np.uint8(G)
        
    if(valueB>255):
        valueB=valueB-255
        valueB2= (255- valueB)/255.0
        X = np.multiply(B,valueB2)
        B = np.add(valueB,X)
        B=np.uint8(B)
    else:
        valueB2= (valueB)/255.0
        B = np.multiply(valueB2,B)
        B=np.uint8(B)
        
    if(valueR>255):
        valueR=valueR-255
        valueR2= (255- valueR)/255.0
        X = np.multiply(R,valueR2)
        R = np.add(valueR,X)
        R=np.uint8(R)
    else:
        valueR2= (valueR)/255.0
        R = np.multiply(valueR2,R)
        R=np.uint8(R)
        
    img2 = cv2.merge([B,G,R])
    cv2.imshow('image',img2) 

    
    pass


def Sharpen(*void):
    value = cv2.getTrackbarPos('Sharpeing','image')
    kernel = value
    if(kernel%2==1):
        kernel = kernel
    else:
        kernel = kernel + 1
    blur = cv2.GaussianBlur(img,(kernel,kernel),sigmaX=value,sigmaY=value)
    unsharp_image = cv2.addWeighted(img, 1.5, blur, -0.5, 0)
    cv2.imshow('image',unsharp_image) 

def Noise(*void):  
    r = cv2.getTrackbarPos('Noise','image')
    k=3*r
    if(k%2==1):
        k=k
    else:
        k=k+1
    blur = cv2.GaussianBlur(img,(k,k),sigmaX=r,sigmaY=r)
    cv2.imshow('image',blur) 
    
    
def colorHist():
    color = ('b','g','r')
    for i,col in enumerate(color):
        histr = cv2.calcHist([img],[i],None,[256],[0,256])
        plt.plot(histr,color = col)
        plt.xlim([0,256])
    plt.show()
    
class MyFirstGUI:
    def __init__(self,master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()
        
        self.greet_button = Button(master, text="ColorTemp", command=self.ColorT)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()
        
    def greet(self):
        colorHist()
        
    def ColorT(self):
        ColorTemp()
        
        

cv2.createTrackbar("Noise","image",0,100,Noise)
cv2.createTrackbar("Sharpeing","image",0,100,Sharpen) 
cv2.createTrackbar("Green","image",255,511,ColorTemp) 
cv2.createTrackbar("Red","image",255,511,ColorTemp) 
cv2.createTrackbar("Blue","image",255,511,ColorTemp) 

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()

#equ = cv2.(img)
#res = np.hstack((img,equ))
#cv2.imshow("image",res) 


cv2.waitKey(0)
cv2.destroyAllWindows()



 