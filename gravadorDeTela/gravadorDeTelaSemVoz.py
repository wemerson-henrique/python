try:
    import pyautogui
except:
    print("Erro: import pyautogui")
try:
    import cv2 #as cv
except:
    print("Erro: import cv2 as cv")
try:
    import numpy as np
except:
    print("Erro: import numpy as np")
try:
    from datetime import datetime
except:
    print("Erro: from datetime import datetime")


# display screen resolution, get it using pyautogui itself
SCREEN_SIZE = tuple(pyautogui.size())
# define the codec
fourcc = cv2.VideoWriter_fourcc(*"XVID")
# frames per second
fps = 12.0
# create the video write object
nomeDoVideo = "video.avi"
out = cv2.VideoWriter(nomeDoVideo, fourcc, fps, (SCREEN_SIZE))
# the time you want to record in seconds
record_seconds = 10

cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live",480,270)

for i in range(int(record_seconds * fps)):
    # make a screenshot
    img = pyautogui.screenshot()
    # convert these pixels to a proper numpy array to work with OpenCV
    frame = np.array(img)
    # convert colors from BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # write the frame
    out.write(frame)
    # show the frame
    cv2.imshow("Live", frame)
    # if the user clicks q, it exits
    if cv2.waitKey(1) == ord("q"):
        break

# make sure everything is closed when exited
cv2.destroyAllWindows()
out.release()