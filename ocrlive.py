import numpy as np
import cv2
import time 
import datetime # date time setting ]
import os 
from ocrtextout import ocr_msg
WorkDay = [] 
today = datetime.date.today() 
WorkDay.append(today) 

cap = cv2.VideoCapture(0)

def capture_picture(): 
      cv2.imshow('img1',frame) # Frame reade and show the picture that saved 
      cv2 .imwrite('img1'+ str(WorkDay[0]) + '.jpg',frame )
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if not ret: 
        break 
    k = cv2.waitKey(1) 

    if k%256 == 27: 
       print("Escape hit , closing ...")
       break
    elif k%256 == 32:
         capture_picture()
         time.sleep(0.4)
         os.system("python ocrtextout.py")  
         Text  = ocr_msg
         print(Text)
         file = open("Tableposition.txt","w")
         file.write("," + Text)
         file.writelines("," + Text)
         time.sleep(0.8)
         file.close() 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
