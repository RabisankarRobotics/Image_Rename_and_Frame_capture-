import cv2
import os

# Create a directory to save the captured frames
output_directory = 'Arpan'
os.makedirs(output_directory, exist_ok=True)

# Initialize the camera
cap = cv2.VideoCapture(0)  # 0 is usually the default camera

frame_count = 0
max_frames = 200

while frame_count < max_frames:
    ret, frame = cap.read()
    
    if not ret:
        print("Failed to capture frame.")
        continue

    frame_count += 1

    resized_frame = cv2.resize(frame, (416, 416))

    frame_filename = os.path.join(output_directory, f"{frame_count}.jpg")
    
    # Save the frame as an image
    cv2.imwrite(frame_filename, resized_frame)
    
    # Display the frame (optional)
    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

print(f"Captured {frame_count} frames. Stopping the program.")
