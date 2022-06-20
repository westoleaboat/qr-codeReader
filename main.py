from tkinter import *
#import pynput
#from pynput.mouse import Button, Controller, Listener
#import mouse
import PIL
from PIL import ImageGrab
import cv2
#import qrtools
#from qrtools import *
#from qrtools.qrtools import *


click_number = 0
click1=False
class Content:
    def __init__(self, root):

        # def mouse_position():

        #     global get_position

        #     # label will display the mouse position 
        #     def get_position():
        #         global display
        #         string = mouse.get_position()
        #         display = string

        #         lbl1['text']=display

        #         root.after(10, mouse_position)
        #     get_position()

        def clicked(event):
            #root1=Tk()
            #root1.lift()
            global click_number
            global click1
            global x1,x2,y1,y2
            global root1
            if click_number == 0:
                if click1==False:
                    x1=event.x
                    y1=event.y
                    print(x1,y1)
                    click1=True
                else:
                    x2=event.x
                    y2=event.y
                    print(x2,y2)

                    snapshot = PIL.ImageGrab.grab(bbox=(x1,y1,x2,y2))
                    snapshot.save('qr-image.png')
                    print('image created')
                    click_number=1
                    root.destroy()
                    root1=Tk()
                    root1.geometry('600x500+500+300')
                    root1.resizable(0,0)

                    img = cv2.imread("qr-image.png", 0)
                  #  #initialize detector
                    detector=cv2.QRCodeDetector()
                    data, bbox, straight_qrcode = detector.detectAndDecode(img)

                    lbl5=Label(text='', font='Verdana 20')
                    #if there is a qr code
                    if bbox is not None:
                        print(f"QRcode data:\n{data}")
                        lbl5['text']=data

                    else:
                        print("QR code not detected")
                        lbl5['text']='QR code not detected, please try again!'

                    lbl3=Label(text='Selected image', font='Verdana 20')
                    lbl3.pack()

                    qr_generated=PhotoImage(file='qr-image.png')
                    img_label=Label(image=qr_generated)
                    img_label.pack()

                    lbl4=Label(text='QR code data:', font='Verdana 20')
                    lbl4.pack()

                    lbl5.pack()
                    #lbl5=Label(text='', font='Verdana 20')
                    #lbl5.pack()
                    
                  #  my_QR = qrtools.QR(filename='qr-image.png')
                  #  my_QR.decode()
                  #  print(my_QR.data)


        def closeMe(event):
            root.destroy()
            print('screenshot stop')
        root.bind('<Key>', closeMe)

        #root.bind('<Button-1>', clicked)
        root.bind('<Button-1>', clicked)

        lbl_click = Label(text='<click the top-left and bottom-right corners of the code image>\nPress any key to exit', font='Verdana 25')
        lbl_click.pack()

        lbl1 = Label(text='text')
        #lbl1.pack()

        #mouse_position()

def main():
    #root1=Tk()
    root=Tk()
    cnt=Content(root)
    #root.geometry('600x500+500+300')
    root.resizable(0,0)
    root.attributes('-fullscreen', 1)
    #transparent background
    root.config(bg='')
    #root.title('qr code')
    root.mainloop()

if __name__ == '__main__':
    main()

