

from pyzbar import pyzbar
import cv2

def show(output,overlay,barcodeType, barcodeData,entries):
    if(len(entries)==1):
         cv2.putText(overlay, entries[0], (20, 50 ), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 255, 0), 2)
    else:
        for i in entries:
            print((entries.index(i)+1)*150)
            cv2.putText(overlay, i, (20, (entries.index(i)+1)*50 ), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 255, 0), 2)
       

entries=[]
cap=cv2.VideoCapture(0)
found=False
while(True):
    ret,frame=cap.read()
    barcodes = pyzbar.decode(frame)
    overlay = frame.copy()
    output = frame.copy()	
    cv2.rectangle(overlay, (0, 0), (200, 480),(0, 0, 100), -1)
	
    if(len(barcodes)>0):
        found=True
        for barcode in barcodes:
            (x, y, w, h) = barcode.rect
            cv2.rectangle(output, (x, y), (x + w, y + h), (0, 0, 255), 2)
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
    
        if(barcodeData not in entries):
            entries.append(barcodeData)
        text = "{} ({})".format(barcodeData, barcodeType)
      #  cv2.putText(output, text, (x, y+10 ), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 0, 255), 2)

  #      print("Found {} barcode: {}".format(barcodeType, barcodeData))
    if(found==True):
        show(output,overlay,barcodeType, barcodeData,entries)
    cv2.addWeighted(overlay, 0.9, output, 1 - 0.7,
		0, output)
    cv2.imshow("Image", output)
    k=cv2.waitKey(1)
    if(k==ord('q')):
        break


