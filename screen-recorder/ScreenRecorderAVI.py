import numpy as np
import cv2
from PIL import ImageGrab
import time


fourcc = cv2.VideoWriter_fourcc(*'XVID')
#video name, format, frame, size
output = cv2.VideoWriter("recording.avi", fourcc, 14.0, (1366,768))

# it wait till 5 sec. video starts after 5 sec
time.sleep(5)

while True:
    #capturing image
    capturedImage = ImageGrab.grab();
    
    #converting image into numpy array
    imageArray = np.array(capturedImage);
    #creating frame
    frame = cv2.cvtColor(imageArray, cv2.COLOR_BGR2RGB)

   #writing frame to output
    output.write(frame)

    #pressing key 'q', program will quit
    if cv2.waitKey(1) == 27 & 0xFF == ord('q'):
        break

    #releasing output and destroying window
output.release()
cv2.destroyAllWindows()



