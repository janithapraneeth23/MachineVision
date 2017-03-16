import cv2
import copy
from matplotlib import pyplot as plt
import numpy as np
from Tkinter import *
import tkFileDialog

global GUIGreenVal
GUIGreenVal = 255 
global GUIRedVal
GUIRedVal = 255
global GUIBlueVal
GUIBlueVal = 255
global img
global imgReset

global mouseDrag
mouseDrag = 0
global startPixX
startPixX = 0
global startPixY
startPixY = 0
global stopPixX
stopPixX = 0
global stopPixY
stopPixY = 0

img = cv2.imread('E:/My Photoes/RMORA@TRICO/2015-12-19-08-17-53-743.jpg',cv2.IMREAD_UNCHANGED)
global img2
img2 = img
global imgReset
imgReset = copy.copy(img)
cv2.namedWindow("image",cv2.WINDOW_AUTOSIZE)  
cv2.imshow('image',img)  

def nothing():
    pass

def CallBackFunc(event, x, y, flags,*userdata):
    global mouseDrag
    global startPixX
    global startPixY
    global stopPixX
    global stopPixY
    global img2
    if  ( event == cv2.EVENT_LBUTTONDOWN ):
        img2 = copy.copy(img)
        cv2.imshow('image',img2)
        print("Left Button Click")
        startPixX = x
        startPixY = y
        print(x)
        print(y)
        mouseDrag = 1
    elif(event == cv2.EVENT_MOUSEMOVE and mouseDrag):
        img2 = copy.copy(img)
        cv2.rectangle(img2,(startPixX,startPixY),(x,y),(0,0,255),2)
        cv2.imshow('image',img2)
        print("Mouse Move")
        print(x - startPixX)
        print(y - startPixY)  
    elif(event == cv2.EVENT_LBUTTONUP):
        print("Left Button UP")
        cv2.rectangle(img2,(startPixX,startPixY),(x,y),(0,0,255),2)
        cv2.imshow('image',img2)
        print(x)
        print(y)
        stopPixX = x
        stopPixY = y
        mouseDrag = 0
        
def imageSelect():
    cv2.setMouseCallback("image",CallBackFunc,None)
    
def imageCrop():
    global img
    crop_img = img[startPixY:stopPixY,startPixX:stopPixX]
    cv2.imshow("image",crop_img)
    img = copy.copy(crop_img)

def imageReset():
    global img
    img = copy.copy(imgReset)
    cv2.imshow("image",img)
    
    
def imageTemp(value):
    print(value)
    B,G,R = cv2.split(img)
    if(value>0):
        valueR=value
        valueR2= (255- valueR)/255.0
        X = np.multiply(R,valueR2)
        R = np.add(valueR,X)
        R=np.uint8(R)
        valueB2= (255 - value)/255.0
        B = np.multiply(valueB2,B)
        B=np.uint8(B)
    elif(value<0):
        value = -value
        valueB=value
        valueB2= (255- valueB)/255.0
        X = np.multiply(B,valueB2)
        B = np.add(valueB,X)
        B=np.uint8(B)
        valueR2= (255 - value)/255.0
        R = np.multiply(valueR2,R)
        R=np.uint8(R)
    img2 = cv2.merge([B,G,R])
    cv2.imshow('image',img2) 
    

def ColorChange():
    #valueG = cv2.getTrackbarPos('Green','image') 
    #valueR = cv2.getTrackbarPos('Red','image') 
    #valueB = cv2.getTrackbarPos('Blue','image') 
    global GUIGreenVal 
    global GUIRedVal
    global GUIBlueVal
    valueG = GUIGreenVal 
    valueR = GUIRedVal
    valueB = GUIBlueVal
    print(valueG)
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


def Sharpen(value):
    #value = cv2.getTrackbarPos('Sharpeing','image')
    kernel = value
    if(kernel%2==1):
        kernel = kernel
    else:
        kernel = kernel + 1
    blur = cv2.GaussianBlur(img,(kernel,kernel),sigmaX=value,sigmaY=value)
    unsharp_image = cv2.addWeighted(img, 1.5, blur, -0.5, 0)
    cv2.imshow('image',unsharp_image) 
    
#def Constrat(value):
#    x = np.uint8([90])
#    
#    #Cons = 0.009 * value + 1
#    B,G,R = cv2.split(img)
#    B = np.uint8(B)
#    bigmaskB = cv2.compare(img,np.uint8([127]),cv2.CMP_GE)
#    smallmaskB = cv2.bitwise_not(bigmaskB)
#    smallB = cv2.subtract(B,value,mask = smallmaskB)
#    bigB = cv2.add(B,value,mask = bigmaskB)
#    
#    bigmaskR = cv2.compare(R,np.uint8([127]),cv2.CMP_GE)
#    smallmaskR = cv2.bitwise_not(bigmaskR)
#    smallR = cv2.subtract(R,value,mask = smallmaskR)
#    bigR = cv2.add(R,value,mask = bigmaskR)
#    
#    bigmaskG = cv2.compare(G,np.uint8([127]),cv2.CMP_GE)
#    smallmaskG = cv2.bitwise_not(bigmaskG)
#    smallG = cv2.subtract(G,value,mask = smallmaskG)
#    bigG = cv2.add(G,value,mask = bigmaskG)
#    
#    B = cv2.add(bigB,smallB)
#    R = cv2.add(bigR,smallR)
#    G = cv2.add(bigG,smallG)
#    
#    img2 = cv2.merge([B,G,R])
#    cv2.imshow('image',img2) 

def Noise(r):  
    #= cv2.getTrackbarPos('Noise','image')
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
        master.title("PhotoEditter")
        
        menubar = Menu(master)
        master.config(menu=menubar)
        
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Open", command=self.FileOpen)
        menubar.add_cascade(label="File", menu=fileMenu)
        
        NoiseSlider = Scale(master, from_=0, to=100, orient=HORIZONTAL,command=self.GUINoise,label="Noise",length=250)
        NoiseSlider.pack(fill=X)
        
        SharpenSlider = Scale(master, from_=0, to=100, orient=HORIZONTAL,command=self.GUISharpen,label="Sharpen",length=250)
        SharpenSlider.pack(fill=X)
        
        ConstratSlider = Scale(master, from_=-100, to=100, orient=HORIZONTAL,command=self.GUIConstrat,label="Constrat",length=250)
        ConstratSlider.pack(fill=X)
        ConstratSlider.set(0)
        
        ConstratSlider = Scale(master, from_=-100, to=100, orient=HORIZONTAL,command=self.GUISaturation,label="Saturation",length=250)
        ConstratSlider.pack(fill=X)
        ConstratSlider.set(0)
        
        ColorGroup = LabelFrame(master, text="Color Adjestment", padx=5, pady=5)
        ColorGroup.pack()
        
        SliderGreen = Scale(ColorGroup, from_=0, to=511, orient=HORIZONTAL,command=self.GUIGreen,label="Green",length=250)
        SliderGreen.pack(fill=X)
        SliderGreen.set(255)
        
        SliderRed = Scale(ColorGroup, from_=0, to=511, orient=HORIZONTAL,command=self.GUIRed,label="Red",length=250)
        SliderRed.pack(fill=X)
        SliderRed.set(255)
        
        SliderBlue = Scale(ColorGroup, from_=0, to=511, orient=HORIZONTAL,command=self.GUIBlue,label="Blue",length=250)
        SliderBlue.pack(fill=X)
        SliderBlue.set(255)
        
        SliderBlue = Scale(master, from_=-20, to=20, orient=HORIZONTAL,command=self.GUITemp,label="Temparature",length=250)
        SliderBlue.pack(fill=X)
        SliderBlue.set(0)
        
        self.greet_button = Button(master, text="Color Histogram", command=self.greet)
        self.greet_button.pack()

        CropGroup = LabelFrame(master, text="Image Crop", padx=5, pady=5)
        CropGroup.pack()
        
        self.close_button = Button(CropGroup, text="Select", command=self.select)
        self.close_button.pack()
        
        self.close_button = Button(CropGroup, text="Crop", command=self.crop)
        self.close_button.pack()
        
        self.close_button = Button(CropGroup, text="Reset", command=self.reset)
        self.close_button.pack()
        
    def greet(self):
        colorHist()
        
    def select(self):
        imageSelect()
        
    def crop(self):
        imageCrop()
    
    def reset(self):
        imageReset()
    
    def GUINoise(self,val):
        Noise(int(val))
        
    def GUISharpen(self,val):
        Sharpen(int(val))
        
    def GUIGreen(self,val):
        global GUIGreenVal 
        GUIGreenVal = int(val)
        ColorChange()
        
    def GUIRed(self,val):
        global GUIRedVal
        GUIRedVal = int(val)
        ColorChange()
        
    def GUIBlue(self,val):
        global GUIBlueVal
        GUIBlueVal = int(val)
        ColorChange()
    
    def FileOpen(self):
        FILEOPENOPTIONS = dict(defaultextension='.jpg',filetypes=[('jpg','*.jpg')])
        file_path = tkFileDialog.askopenfilename(**FILEOPENOPTIONS)
        print(file_path)
        global img
        img = cv2.imread(file_path,cv2.IMREAD_UNCHANGED)
        cv2.imshow('image',img)  
        print(file_path)
        
    def GUITemp(self,val):
        imageTemp(int(val))
        
    def GUIConstrat(self,val):
        pass
    
    def GUISaturation(self,val):
        pass
    
root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()

cv2.waitKey(0)
cv2.destroyAllWindows()



 