# trying out basic openCV
import cv2

# defining a video capture object
vid = cv2.VideoCapture(0)

while True:
    # capturing video per frame
    ret, frame = vid.read()
    # displaying the image
    cv2.imshow('frame', frame)
    # setting stop button as 'q' for quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# releasing the vid capture obj
vid.release()
cv2.destroyAllWindows()
