import cv2
from deepface import DeepFace
from PIL import Image, ImageTk
import tkinter as tk

# Variable to control the program state
running = True

# Function to analyze the frame and obtain emotions and gender
def analyze_frame(frame):
    try:
        # Analyze the frame to detect faces and obtain emotions and gender
        analysis_results = DeepFace.analyze(frame, actions=['emotion', 'gender'], enforce_detection=False, detector_backend='retinaface')

        processed_faces = []

        for face in analysis_results:
            x, y, w, h = face["region"]['x'], face["region"]['y'], face["region"]['w'], face["region"]['h']
            processed_faces.append({
                "emotion": face["emotion"],
                "gender": face["gender"],
                "region": (x, y, w, h)
            })

        return processed_faces
    except Exception as e:
        print(f"Error in detection: {str(e)}")
        return None

# Function to update the webcam frame and show emotions and gender
def update_frame(video_label, cap):
    global running

    # Read the frame from the webcam
    ret, frame = cap.read()

    if not ret:
        print("Error capturing video.")
        return

    # Flip the frame horizontally (like a mirror)
    frame = cv2.flip(frame, 1)

    # Analyze the frame for emotions and gender
    analysis_results = analyze_frame(frame)

    if analysis_results:
        # If faces are detected, draw the rectangle and show the information
        for result in analysis_results:
            x, y, w, h = result['region']
            emotion_probabilities = result['emotion']
            gender = result['gender']

            # Draw a rectangle around the face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            y_offset = y  # Vertical position for emotions
            for emotion, prob in emotion_probabilities.items():
                cv2.putText(frame, f"{emotion}: {prob:.2f}", (x + w + 10, y_offset), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                y_offset += 20  # Add offset for the next emotion

            # Show gender probabilities
            male_probability = gender.get("Man", 0)
            female_probability = gender.get("Woman", 0)
            cv2.putText(frame, f"Male: {male_probability:.2f}", (x, y + h + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            cv2.putText(frame, f"Female: {female_probability:.2f}", (x, y + h + 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # Convert the frame from BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(rgb_frame)
    imgtk = ImageTk.PhotoImage(image=img)

    # Update the video label with the new frame
    video_label.imgtk = imgtk
    video_label.configure(image=imgtk)

    # If the program is still running, update the frame after 10 ms
    if running:
        video_label.after(10, update_frame, video_label, cap)

# Main function that manages the Tkinter window and video
def main():
    global running, cap

    # Create the main window
    root = tk.Tk()
    root.title("Emotion and Gender Detection")
    root.geometry("1200x600")  # Resizable window
    root.resizable(True, True)  # Allow window resizing

    # Create a label to show the video
    video_label = tk.Label(root)
    video_label.pack(expand=True, fill=tk.BOTH)

    # Start capturing video from the webcam
    cap = cv2.VideoCapture(0)

    # Add handler for closing the window
    root.protocol("WM_DELETE_WINDOW", lambda: close_app(root))

    # Continuously update the frame
    update_frame(video_label, cap)

    # Start the Tkinter interface
    root.mainloop()

# Function to close the application
def close_app(root):
    global running
    running = False
    cap.release()  # Release the webcam
    cv2.destroyAllWindows()  # Close all OpenCV windows
    root.quit()  # Exit the Tkinter mainloop
    root.destroy()  # Destroy the window

# Run the application
if __name__ == "__main__":
    main()
