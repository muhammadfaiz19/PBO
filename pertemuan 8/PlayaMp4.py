import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class VideoPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Video Player")
        self.root.geometry("1000x800")
        self.root.configure(bg="#333")

        # Create a VideoCapture object
        self.cap = cv2.VideoCapture()

        # Judul program
        self.title_label = tk.Label(root, text="Aplikasi Video Player", font=("Helvetica", 16, "bold"), bg="#333", fg="white")
        self.title_label.pack(padx=10, pady=10)

        # Nama, kelas, dan NIM
        self.name_label = tk.Label(root, text="Muhammad Faiz", font=("Helvetica", 12), bg="#333", fg="white")
        self.name_label.pack(pady=5)

        self.class_label = tk.Label(root, text="TI22D", font=("Helvetica", 12), bg="#333", fg="white")
        self.class_label.pack(pady=5)

        self.nim_label = tk.Label(root, text="220511139", font=("Helvetica", 12), bg="#333", fg="white")
        self.nim_label.pack(pady=5)

        # Create a label to display the video frames
        self.label = tk.Label(root, bg="#333")
        self.label.pack(padx=10, pady=10)

        # Create buttons
        self.btn_open = tk.Button(root, text="Open Video", command=self.open_video, font=("Helvetica", 12), bg="#4CAF50", fg="white")
        self.btn_open.pack(pady=5)

        self.btn_play = tk.Button(root, text="Play", command=self.play_video, font=("Helvetica", 12), bg="#4CAF50", fg="white")
        self.btn_play.pack(pady=5)

        self.btn_stop = tk.Button(root, text="Stop", command=self.stop_video, font=("Helvetica", 12), bg="#f44336", fg="white")
        self.btn_stop.pack(pady=5)

        self.btn_exit = tk.Button(root, text="Exit", command=root.destroy, font=("Helvetica", 12), bg="#333", fg="white")
        self.btn_exit.pack(pady=5)

    def open_video(self):
        file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi")])
        if file_path:
            self.cap.open(file_path)

            # Get the video's width and height
            width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

            # Resize the window to match the video resolution
            self.root.geometry(f"{width}x{height}")

    def play_video(self):
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                # Convert the frame to RGB format
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Convert the frame to ImageTk format
                img = Image.fromarray(rgb_frame)
                img_tk = ImageTk.PhotoImage(img)

                # Update the label with the new frame
                self.label.img_tk = img_tk
                self.label.config(image=img_tk)
                self.root.update()

                # Pause for a short time (approximately 33 milliseconds for 30 fps)
                self.root.after(33)

                # Press Q on the keyboard to exit
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
            else:
                break

    def stop_video(self):
        # Release the video capture object
        self.cap.release()
        # Close the OpenCV window
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoPlayerApp(root)
    root.mainloop()
