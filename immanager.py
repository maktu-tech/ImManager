from tkinter import *
from tkinter import filedialog
from PIL import Image as im
from PIL import ImageTk as it
from PIL import ImageFilter as iF
from PIL import ImageEnhance as ie

global img_ori ,img_alter_save ,imgpanel ,count
count=0
img_res=None
img_ori=None
name=None

#--standy functions-------
def donothing():
    #better to use pass instead of using return
    pass

def version_info():
    t1=Tk()
    t1.title("Version Info")
    label=Label(t1,text="This is the first release of ImManger.",width=50,height=7,font=("Times New Roman",14))
    label.pack()
def about():
    t1=Tk()
    t1.title("About Us")
    text="""Using ImManager you can:
view image files of supported formats(JPEG, GIF, PNG, BMP, Webp..),
resize them to your choice whether in terms of height or width or both,
enhance brightness or contrast or sharpness to your accordance,
perform rotating and other transposing action like fliping left- right,
changes modes provided by ImManager such W&B or RBG interchange,
And Ofcourse you can save them in any format of your choice.
"""
    label=Label(t1,text=text,width=60,height=10,font=("Times New Roman",14))
    label.pack()
def help1():
    t1=Tk()
    t1.title("Help Center")
    text="""Welcome to ImManager's Help Center:

Functions Performed:
Rotate: It will rotate the image with specified angle whereas image's dimension remains same.
Re-size: It will Resize the image according to the provided parameters (i.e width and height)
either or both can be provided.
Re-Size(ratio): It will Resize the image according to the provided ratio which means the altered
image's size will be original size X ratio.
Transpose: It can transpose the image, which means the image will rotate at right angle. Also
unlike rotate, here image's dimension can be altered.
Mode: For Images with RBG mode, it can interchange 'Red', 'Blue', 'Green'. For Single or Four mode images
it displays they aren't eligible.
Flip LR: It flip Left to Right & vice versa.
Flip TB: It flip Top to Bottom & vice versa.
B&W Mode: It changes 'RBG' image to Black & White
Contrast: It enhances Contrast of images according to provides number, which act for percentage change.
Brightness: It enhances Brightness of images according to provides number, which act for percentage change.
Sharpness: It enhances Sharpness of images according to provides number, which act for percentage change.
Back: Go to last saved image.
Save Alter: It saves the last altered image by user. If not pressed that editing after last save won't be saved.
Open: It opens image of extensions like JPEG, GIF, PNG, BMP, DIB, EPS, ICNS, ICO, IM, JPEG 2000,
MSP, PCX, PPM, SGI, SPIDER, TGA, TIFF, WebP, XBM, et cetera(many read only formats are included).
Save:  It can save image with extensions like JPEG, GIF, PNG, BMP, DIB, EPS, ICNS, ICO, IM, JPEG 2000,
MSP, PCX, PPM, SGI, SPIDER, TGA, TIFF, WebP, XBM.

Allowed Data Type:
Float and Integer is allowed in Re-Size(ratio), Contrast, Brightness and Sharpness
Integer is allowed in Rotate, Re-Size
Transpose allows 90, 180, 270
Lastly, Mode allows integer ranging from 1 to 6.

Information Bar:
Instruction Bar: Present at the bottomost of ImManager. It provide the information about the task last performed.
It generates the error and success message for user's guidance
Size Info: It provides the size of current 'saved' image.
"""
    label=Label(t1,text=text,width=100,height=40,font=("Times Roman",13),justify=LEFT)
    label.pack()
def check(string):
    try:
        float(string)
    except ValueError:
        info.configure(text="Enter suitable value, find correct data type at help")
        info.text="Enter suitable value, find correct data type at help"
        return True
def checkint(string):
    try:
        int(string)
    except ValueError:
        info.configure(text="Enter suitable value, find correct data type at help")
        info.text="Enter suitable value, find correct data type at help"
        return True
def checkzero(tup):
    if (tup[0]<=0 or tup[1]<=0):
        info.configure(text="Enter suitable value, find correct data type at help")
        info.text="Enter suitable value, find correct data type at help"
        return True
def checkmode():
    try:
        r,g,b=img_ori.split()
    except ValueError:
        info.configure(text="Image doesn't have 3 color modes")
        info.text="Image doesn't have 3 color modes"
        return True
        
#-----edit functions-----
def rotate():
    global count
    global img_ori
    global img_alter_save
    if img_ori==None:
        info.configure(text="For editing you need to open an image.")
        info.text="For editing you need to open an image."
    elif(check(rot_entry.get())==True and rot_entry.get()!=''):
        return
    elif(checkint(rot_entry.get())==True and rot_entry.get()!=''):
        return
    elif(rot_entry.get() != ''):
        img_ori3 = img_ori.rotate(int(rot_entry.get()))
        show_panel(img_ori3)
        img_alter_save=img_ori3
        count+=1
        info.configure(text="Image is rotated")
        info.text="Image is rotated"
    else:
        info.configure(text="Enter value to rotate")
        info.text="Enter value to rotate"
def re_size():
    global count
    global img_alter_save
    global img_ori
    if img_ori==None:
        info.configure(text="For editing you need to open an image.")
        info.text="For editing you need to open an image."
    elif(check(resize_entryw.get())==True and resize_entryw.get() != ''):
        return
    elif(check(resize_entryh.get())==True and resize_entryh.get() != ''):
        return
    elif(checkint(resize_entryw.get())==True and resize_entryw.get() != ''):
        return
    elif(checkint(resize_entryh.get())==True and resize_entryh.get() != ''):
        return
    elif(resize_entryw.get() != '' and resize_entryh.get() != '' and int(resize_entryw.get())<10001 and int(resize_entryh.get())<10001):
        tup=(int(resize_entryw.get()),int(resize_entryh.get()))
        if(checkzero(tup)==True):
            return
        img_ori3=img_ori.resize(tup)
        show_panel(img_ori3)
        img_alter_save=img_ori3
        count+=1
        info.configure(text="Image is resized")
        info.text="Image is resized"
    elif(resize_entryw.get() != '' and resize_entryh.get() == ''  and int(resize_entryw.get())<10001):
        w=int(resize_entryw.get())
        img_ori2=it.PhotoImage(img_ori)
        tup=(w,(int(w*img_ori2.height()/img_ori2.width())))
        if(checkzero(tup)==True):
            return
        img_ori3=img_ori.resize(tup)
        show_panel(img_ori3)
        img_alter_save=img_ori3
        count+=1
        info.configure(text="Image is resized")
        info.text="Image is resized"
    elif(resize_entryw.get() == '' and resize_entryh.get() != '' and int(resize_entryh.get())<10001 ):
        img_ori2=it.PhotoImage(img_ori)
        h=int(resize_entryh.get())
        tup=(int(h*img_ori2.width()/img_ori2.height()),h)
        if(checkzero(tup)==True):
            return
        img_ori3=img_ori.resize(tup)
        show_panel(img_ori3)
        img_alter_save=img_ori3
        count+=1
        info.configure(text="Image is resized")
        info.text="Image is resized"
    else:
        info.configure(text="Enter value to resize with max upto 10000")
        info.text="Enter value to resize with max upto 10000"
def re_size_rationally():
    global count
    global img_ori
    global img_alter_save
    if img_ori==None:
        info.configure(text="For editing you need to open an image.")
        info.text="For editing you need to open an image."
    elif(check(resize_rat_entry.get())==True and resize_rat_entry.get()!=''):
        return
    
    elif(resize_rat_entry.get() != '' ):
        width,height=img_ori.size
        ratio=float(resize_rat_entry.get())
        if(ratio>3):
            info.configure(text="Enter ratio smaller than 3")
            info.text="Enter ratio smaller than 3"
            return
        width,height=width*ratio,height*ratio
        box=(int(width),int(height))
        if(checkzero(box)==True):
            return
        img_ori3=img_ori.resize(box)
        show_panel(img_ori3)
        img_alter_save=img_ori3
        count+=1
        info.configure(text="Image is resized rationally")
        info.text="Image is resized rationally"
    else:
        info.configure(text="Enter value to resize(rationally)")
        info.text="Enter value to resize(rationally)"
        


'''def roll_lr(image, delta):
    "Roll an image sideways"
    xsize, ysize = image.size
    delta = delta % xsize
    if delta == 0: return image
    part1 = image.crop((0, 0, delta, ysize))
    part2 = image.crop((delta, 0, xsize, ysize))
    image.paste(part2, (0, 0, xsize-delta, ysize))
    image.paste(part1, (xsize-delta, 0, xsize, ysize))
    return image
def roll_tb(image, delta):
    "Roll an image sideways"
    xsize, ysize = image.size
    delta = delta % ysize
    if delta == 0: return image
    part1 = image.crop((0, 0,xsize,delta))
    part2 = image.crop((0,delta, xsize, ysize))
    image.paste(part2, (0, 0, xsize, ysize-delta))
    image.paste(part1, (0,ysize-delta, xsize, ysize))
    return image'''
def transpose():
    global count
    global img_ori
    global img_alter_save
    if img_ori==None:
        info.configure(text="For editing you need to open an image.")
        info.text="For editing you need to open an image."
    elif(check(trans_entry.get())==True and trans_entry.get()!=''):
        return
    elif(trans_entry.get() != ''):
        if(int(trans_entry.get()) ==90):
            img_ori3 = img_ori.transpose(im.ROTATE_90)
        elif(int(trans_entry.get()) ==180):
            img_ori3 = img_ori.transpose(im.ROTATE_180)
        elif(int(trans_entry.get())==270):
            img_ori3 = img_ori.transpose(im.ROTATE_270)
        else:
            info.configure(text="Transposition can be done at right angle (i.e 90, 180, 270)")
            info.text="Transposition can be done at right angle (i.e 90, 180, 270)"
            return
        show_panel(img_ori3)
        img_alter_save=img_ori3
        count+=1
        info.configure(text="Image is Transposed")
        info.text="Image is Transposed"
    else:
        info.configure(text="Enter value to Transposed")
        info.text="Enter value to Transposed"
def split_merge():
    global count
    global img_ori
    global img_alter_save
    if img_ori==None:
        info.configure(text="For editing you need to open an image.")
        info.text="For editing you need to open an image."
    elif(check(split_entry.get())==True and split_entry.get() != ''):
        return
    elif(checkint(split_entry.get())==True and split_entry.get() != ''):
        return
    elif (checkmode()==True):
        return
    elif(split_entry.get() != ''):
        img_ori3=img_ori
        r, g, b  = img_ori.split()
        if int(split_entry.get())==1:
            img_ori3 = im.merge("RGB", (r,g,b ))
        elif int(split_entry.get())==2:
            img_ori3 = im.merge("RGB", (r,b,g ))
        elif int(split_entry.get())==3:
            img_ori3 = im.merge("RGB", (g,r,b ))
        elif int(split_entry.get())==4:
            img_ori3 = im.merge("RGB", (g,b,r ))
        elif int(split_entry.get())==5:
            img_ori3 = im.merge("RGB", (b,g,r ))
        elif int(split_entry.get())==6:
            img_ori3 = im.merge("RGB", (b,r,g))
        else:
            info.configure(text="Enter valid option")
            info.text="Enter valid option"
            return
        show_panel(img_ori3)
        img_alter_save=img_ori3
        count+=1
        info.configure(text="Image is altered")
        info.text="Image is altered"
    else:
        info.configure(text="Enter value to Change Mode")
        info.text="Enter value to Change Mode"
def fliplr():
    global count
    global img_ori
    global img_alter_save
    if img_ori==None:
        info.configure(text="For editing you need to open an image.")
        info.text="For editing you need to open an image."
    else:
        img_ori3=img_ori.transpose(im.FLIP_LEFT_RIGHT)
        show_panel(img_ori3)
        img_alter_save=img_ori3
        count+=1
        info.configure(text="Image is fliped Left - Right")
        info.text="Image is fliped Left - Right"
def fliptb():
    global count
    global img_ori
    global img_alter_save
    if img_ori==None:
        info.configure(text="For editing you need to open an image.")
        info.text="For editing you need to open an image."
    else:
        img_ori3=img_ori.transpose(im.FLIP_TOP_BOTTOM)
        show_panel(img_ori3)
        img_alter_save=img_ori3
        count+=1
        info.configure(text="Image is fliped Left - Right")
        info.text="Image is fliped Left - Right"
def convert_bw():
    global count
    global img_ori
    global img_alter_save
    if img_ori==None:
        info.configure(text="For editing you need to open an image.")
        info.text="For editing you need to open an image."
    else:
        img_ori3=img_ori.convert("L")
        show_panel(img_ori3)
        img_alter_save=img_ori3
        count+=1
        info.configure(text="Image is converted to Black And White")
        info.text="Image is converted to Black And White"
def contrast():
    global count
    global img_ori
    global img_alter_save
    if img_ori==None:
        info.configure(text="For editing you need to open an image.")
        info.text="For editing you need to open an image."
    elif(check(contrast_entry.get())==True and contrast_entry.get()!=''):
        return
    elif(contrast_entry.get() != ''):
        img_ori3 = ie.Contrast(img_ori)
        img_ori3=img_ori3.enhance(float(contrast_entry.get()))
        show_panel(img_ori3)
        img_alter_save=img_ori3
        count+=1
        info.configure(text="Contrast is change")
        info.text="Contrast is change"
    else:
        info.configure(text="Enter value to change contrast")
        info.text="Enter value to change contrast"
def brightness():
    global count
    global img_ori
    global img_alter_save
    if img_ori==None:
        info.configure(text="For editing you need to open an image.")
        info.text="For editing you need to open an image."
    elif(check(brightness_entry.get())==True and brightness_entry.get()!=''):
        return
    elif(brightness_entry.get() != ''):
        img_ori3 = ie.Brightness(img_ori)
        img_ori3=img_ori3.enhance(float(brightness_entry.get()))
        show_panel(img_ori3)
        img_alter_save=img_ori3
        count+=1
        info.configure(text="Brightness is change")
        info.text="Brightness is change"
    else:
        info.configure(text="Enter value to change brightness")
        info.text="Enter value to change brightness"
def sharpness():
    global count
    global img_ori
    global img_alter_save
    if img_ori==None:
        info.configure(text="For editing you need to open an image.")
        info.text="For editing you need to open an image."
    elif(check(sharpness_entry.get())==True and sharpness_entry.get()!=''):
        return
    elif(sharpness_entry.get() != ''):
        img_ori3 = ie.Sharpness(img_ori)
        img_ori3=img_ori3.enhance(float(sharpness_entry.get()))
        show_panel(img_ori3)
        img_alter_save=img_ori3
        count+=1
        info.configure(text="Sharpness is change")
        info.text="Sharpness is change"
    else:
        info.configure(text="Enter value to change sharpness")
        info.text="Enter value to change sharpness"


#---basic functions ------
def OpenFile():
    global img_ori
    name = filedialog.askopenfile()
    if (name!=None):
        img_ori=im.open(name.name)
        info.configure(text="Image is opened")
        info.text="Image is opened"
        show_panel(img_ori)
    else:
        info.configure(text="Image isn't selected")
        info.text="Image isn't selected"
def show_panel(img_ori):
    img_ori2=it.PhotoImage(img_ori)
    if (img_ori2.height()>700 and img_ori2.height()>img_ori2.width()):
        img_res=img_ori.resize((int(700*img_ori2.width()/img_ori2.height()),700),im.ANTIALIAS)
        img_res=it.PhotoImage(img_res)
    elif (img_ori2.width()>700 and img_ori2.width()>img_ori2.height()):
        img_res=img_ori.resize((700,int(700*img_ori2.height()/img_ori2.width())),im.ANTIALIAS)
        img_res=it.PhotoImage(img_res)
    elif(img_ori2.width()>700 and img_ori2.width()==img_ori2.height()):
        img_res=img_ori.resize((700,700),im.ANTIALIAS)
        img_res=it.PhotoImage(img_res)
    else:
        img_res=img_ori2
    imgpanel.configure(image=img_res)
    imgpanel.image=img_res
    info_size(img_ori)
def SaveFile():
    if img_ori==None:
        info.configure(text="For saving you need to open an image.")
        info.text="For saving you need to open an image."
    else:
        name=None
        name =filedialog.asksaveasfile()
        if (name!=None):
            img_ori.save(name.name,format='JPEG')
            info.configure(text="Image is saved")
            info.text="Image is saved"
def alter_save():
    global img_ori
    global img_alter_save
    global count
    if img_ori==None:
        info.configure(text="For saving you need to open an image.")
        info.text="For saving you need to open an image."
    elif (count>0):
        img_ori=img_alter_save
        info.configure(text="Altered Image is saved")
        info.text="Altered Image is saved"
    else:
        info.configure(text="Image isn't altered")
        info.text="Image isn't altered"
def info_size(image):
    if image==None:
        return("")
    else:
        width,height=image.size
        i=(str(width)+' x '+str(height))
        i="Size: "+i
        label_info.configure(text=i)
        label_info.text=i
def back():
    global img_ori
    if img_ori==None:
        info.configure(text="Back option is blocked.")
        info.text="Back option is blocked."
    else:
        show_panel(img_ori)
        info.configure(text="This is the last saved image.")
        info.text="This is the last saved image."
        
#--screens and frames--------
root=Tk()
root.geometry('1200x700')
root.title("ImManager")
frame3=Frame(root)
frame3.pack(side=BOTTOM, fill=X)
frame4=Frame(root)
frame4.pack(side=BOTTOM, fill=X)
frame2=Frame(root)
frame2.pack(side=LEFT, fill=X)
frame1=Frame(root)
frame1.pack(side=LEFT,fill=X)




#--menus----------------
m=Menu(frame1)
root.config(menu=m)

mainmenu=Menu(m,tearoff=0)
m.add_cascade(label='File',menu=mainmenu)
mainmenu.add_command(label='Open', command=OpenFile)
mainmenu.add_command(label='Save', command=SaveFile)
mainmenu.add_separator()
mainmenu.add_command(label='Exit', command=root.destroy)

helpmenu=Menu(m,tearoff=0)
m.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='Help Center',command=help1)
helpmenu.add_command(label='About',command=about)
helpmenu.add_separator()
helpmenu.add_command(label='Version: 1.0',command=version_info)

#---frames------
#--frame3------
info=Label(frame3,text="Developed by. mayank",relief=SUNKEN,font=("Times Roman",15),anchor=W)
info.pack(expand="yes",fill="both")
#----frame2-------
rot_button=Button(frame2,text="Rotate",height=2,width=10,command=rotate)
rot_button.grid(row=1,column=1,padx=25,ipadx=10,pady=5)
rot_entry = Entry(frame2,justify=RIGHT,width=5,font=("",14))
rot_entry.grid(row=1,column=2)
resize_button=Button(frame2,text="Re-Size",height=2,width=10,command=re_size)
resize_button.grid(row=2,column=1,padx=25,ipadx=10,pady=5)
resize_entryw = Entry(frame2,justify=RIGHT,width=5,font=("",14))
resize_entryw.grid(row=2,column=2)
resize_entryh = Entry(frame2,justify=RIGHT,width=5,font=("",14))
resize_entryh.grid(row=2,column=3)
resize_rat_button=Button(frame2,text="Re-Size(ratio)",height=2,width=10,command=re_size_rationally)
resize_rat_button.grid(row=3,column=1,padx=25,ipadx=10,pady=5)
resize_rat_entry = Entry(frame2,justify=RIGHT,width=5,font=("",14))
resize_rat_entry.grid(row=3,column=2)
trans_button=Button(frame2,text="Transpose",height=2,width=10,command=transpose)
trans_button.grid(row=4,column=1,padx=25,ipadx=10,pady=5)
trans_entry = Entry(frame2,justify=RIGHT,width=5,font=("",14))
trans_entry.grid(row=4,column=2)
split_button=Button(frame2,text="Mode",height=2,width=10,command=split_merge)
split_button.grid(row=5,column=1,padx=25,ipadx=10,pady=5)
split_entry = Entry(frame2,justify=RIGHT,width=5,font=("",14))
split_entry.grid(row=5,column=2)
fliplr_button=Button(frame2,text="Flip LR",height=2,width=10,command=fliplr)
fliplr_button.grid(row=6,column=1,padx=25,ipadx=10,pady=5)
fliptb_button=Button(frame2,text="Flip TB",height=2,width=10,command=fliptb)
fliptb_button.grid(row=6,column=2,padx=10,ipadx=10,pady=5)
bw_button=Button(frame2,text="B&W Mode",height=2,width=10,command=convert_bw)
bw_button.grid(row=7,column=1,padx=25,ipadx=10,pady=5)
#crop_button=Button(frame2,text="Crop",height=2,width=10,command=crop)
#crop_button.grid(row=7,column=2,padx=25,ipadx=10,pady=5)
contrast_button=Button(frame2,text="Contrast",height=2,width=10,command=contrast)
contrast_button.grid(row=8,column=1,padx=25,ipadx=10,pady=5)
contrast_entry = Entry(frame2,justify=RIGHT,width=5,font=("",14))
contrast_entry.grid(row=8,column=2)
brightness_button=Button(frame2,text="Brightness",height=2,width=10,command=brightness)
brightness_button.grid(row=9,column=1,padx=25,ipadx=10,pady=5)
brightness_entry = Entry(frame2,justify=RIGHT,width=5,font=("",14))
brightness_entry.grid(row=9,column=2)
sharpness_button=Button(frame2,text="Sharpness",height=2,width=10,command=sharpness)
sharpness_button.grid(row=10,column=1,padx=25,ipadx=10,pady=5)
sharpness_entry = Entry(frame2,justify=RIGHT,width=5,font=("",14))
sharpness_entry.grid(row=10,column=2)
#---frame1-------
label_info=Label(frame4,text="Size: ",height=2,width=15,font=("",16))
label_info.grid(row=1,column=5,padx=20,ipadx=50,pady=10)
open_button=Button(frame4,text="Open",height=2,width=10,command=OpenFile,font=("",12))
open_button.grid(row=1,column=3,padx=50,ipadx=10,pady=10)
save_button=Button(frame4,text="Save",height=2,width=10,command=SaveFile,font=("",12))
save_button.grid(row=1,column=4,padx=50,ipadx=10,pady=10)
alter_save_button=Button(frame4,text="Save Alter",height=2,width=10,command=alter_save,font=("",12))
alter_save_button.grid(row=1,column=2,padx=50,ipadx=10,pady=10)
back_button=Button(frame4,text="Back",height=2,width=10,command=back,font=("",12))
back_button.grid(row=1,column=1,padx=50,ipadx=10,pady=10)
imgpanel=Label(frame1,height=700,width=800)
imgpanel.pack(expand="yes",fill="none")


root.mainloop()
