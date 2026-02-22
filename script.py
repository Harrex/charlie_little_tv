import cv2
import sys
import time

static = cv2.VideoCapture("static.mp4")
Audrey = cv2.VideoCapture("Audrey.mp4")
Harinee = cv2.VideoCapture("Harinee.mp4")
Heidi = cv2.VideoCapture("Heidi.mp4")
cv2.namedWindow("Video", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Video", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)


def static_loop(cap):
    while True:
        ret, frame = cap.read()

        if not ret:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

        cv2.imshow("Video", frame)

        # Press Q to quit
        if ord("a") <= cv2.waitKey(25) & 0xFF <= ord("z"):
            return


def video_play(cap):
    while True:
        ret, frame = cap.read()

        if not ret:
            time.sleep(1)
            break  # No more frames → end of video

        cv2.imshow("Video", frame)

        # Press Q to quit
        if ord("a") <= cv2.waitKey(25) & 0xFF <= ord("z"):
            return
    static_loop(static)


if sys.argv[1] == "Audrey":
    a = Audrey
else:
    a = Harinee


try:
    static_loop(static)
    while True:
        video_play(a)
        video_play(Heidi)
except KeyboardInterrupt:
    print("Stopping...")
    Audrey.release()
    Harinee.release()
    Heidi.release()
    cv2.destroyAllWindows()
