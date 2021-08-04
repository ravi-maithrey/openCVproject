# trying out basic openCV
import cv2

# defining a video capture object
vid = cv2.VideoCapture(0)

while True:
    # capturing video per frame
    ret, frame = vid.read()
    # drawing a random bounding box
    start_point = (5, 5)
    end_point = (220, 220)

    # Blue color in BGR
    color = (255, 0, 0)

    # Line thickness of 2 px
    thickness = 2

    # Using cv2.rectangle() method
    # Draw a rectangle with blue line borders of thickness of 2 px
    frame = cv2.rectangle(frame, start_point, end_point, color, thickness)
    # displaying the image
    cv2.imshow('frame', frame)
    # setting stop button as 'q' for quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# releasing the vid capture obj
vid.release()
cv2.destroyAllWindows()
