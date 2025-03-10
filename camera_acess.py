import cv2

# Open the default camera (usually the built-in webcam)
cap = cv2.VideoCapture(0)

# Check if the camera was opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Loop to continuously capture frames from the webcam
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If frame is read correctly, ret is True
    if not ret:
        print("Error: Failed to capture frame.")
        break

    #Flip the frame in horizontaly to mirror effect
    flipped_frame =cv2.flip(frame, 1) #1 for horizontal fli, 0 for vertical flip, -1 both horizontal and vertical flip

    # Display the frame in a window
    cv2.imshow('Webcam Feed', flipped_frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()