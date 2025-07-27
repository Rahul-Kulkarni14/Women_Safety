import main  # Import your main.py functionalities
import cv2
from PIL import Image, ImageTk
import tkinter as tk


# Function to detect threat
def detect_threat(frame_results):
    fear_detected = False
    female_fear = False
    male_count = 0

    for face in frame_results:
        gender = face['gender']
        emotions = face['emotion']

        # Detect fear in a female
        if gender.get('Woman', 0) > 50 and emotions.get('fear', 0) > 50:
            female_fear = True

        # Count males
        if gender.get('Man', 0) > 50:
            male_count += 1

    # Check threat condition
    if female_fear and male_count >= 2:
        print("⚠️ Threat Alert: Fearful woman detected with multiple men nearby!")
        return True  # Return True to indicate threat
    return False


# Main function to run the threat detection with GUI
def run_threat_detection():
    global running  # Control program state
    running = True

    # Create the main window
    root = tk.Tk()
    root.title("Threat Detection")
    root.geometry("1200x600")

    video_label = tk.Label(root)
    video_label.pack(expand=True, fill=tk.BOTH)

    cap = cv2.VideoCapture(0)

    # Function to update the frame
    def update_frame():
        global running
        ret, frame = cap.read()
        if not ret:
            return

        # Analyze the frame
        frame_results = main.analyze_frame(frame)
        if frame_results:
            threat = detect_threat(frame_results)
            if threat:
                print("Threat detected. Closing application.")
                running = False
                close_app()  # Close application when threat is detected

            # Draw the detection results on the frame
            for result in frame_results:
                x, y, w, h = result['region']
                emotions = result['emotion']
                gender = result['gender']

                # Draw rectangle around the face
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                # Display emotions and gender
                y_offset = y  # Start position for text
                for emotion, prob in emotions.items():
                    cv2.putText(frame, f"{emotion}: {prob:.2f}", (x + w + 10, y_offset), cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                                (0, 255, 0), 2)
                    y_offset += 20  # Move down for next line of text

                # Show gender probabilities
                male_prob = gender.get("Man", 0)
                female_prob = gender.get("Woman", 0)
                cv2.putText(frame, f"Male: {male_prob:.2f}", (x, y + h + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                            (0, 255, 0), 2)
                cv2.putText(frame, f"Female: {female_prob:.2f}", (x, y + h + 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                            (0, 255, 0), 2)

        # Convert the frame from BGR to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame_rgb)
        imgtk = ImageTk.PhotoImage(image=img)
        video_label.imgtk = imgtk
        video_label.configure(image=imgtk)

        if running:
            video_label.after(10, update_frame)  # Repeat after 10 ms

    # Stop the camera and close the window
    def close_app():
        global running
        running = False
        cap.release()
        cv2.destroyAllWindows()
        root.quit()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", close_app)  # Handle window close
    update_frame()
    root.mainloop()


# Run the program
if __name__ == "__main__":
    run_threat_detection()
