import os
from PIL import Image

# Capturing frame in cap varibale
cap = cv2.VideoCapture(0)
# Creating detection function for QR Code
detection = cv2.QRCodeDetector()

while True:

    # Reading frame cap
    ret,frame = cap.read()

    # Decoding the frame for QR Code data
    data,box,point = detection.detectAndDecode(frame)

    # Printing frame
    cv2.imshow("QR Code Scanner",frame)

    if cv2.waitKey(1) & len(data)>1:
        break

# Printing the QR Code data
print(data)
cap.release()
cv2.destroyAllWindows()
