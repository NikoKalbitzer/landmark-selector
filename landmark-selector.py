# importing the module
import re

import cv2

PATH_OUTPUT = "out/"
PATH_PICTURE = "renderPicMean.png"

landmarks = [["SN", 0, 0], ["N-L", 0, 0], ["N-R", 0, 0]]
counter = 0


def get_name_without_ending(filename):
    return re.split("\\.", filename)[0]


def click_event(event, x, y, flags, params):
    global landmarks
    global counter
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
        font = cv2.FONT_HERSHEY_SIMPLEX
        # 70x30 schwarze box zeichnen
        cv2.rectangle(img, (0, 0), (70, 30), (0, 0, 0), -1)
        cv2.circle(img, (x, y), radius=4, color=(0, 0, 255), thickness=-1)
        if counter < len(landmarks):
            landmarks[counter][1] = x
            landmarks[counter][2] = y
            counter += 1
        if counter < len(landmarks):
            cv2.putText(img, landmarks[counter][0], (5, 25), font,
                        1, (255, 0, 0), 2)
        cv2.imshow('image', img)
        print(landmarks)

    # checking for right mouse clicks
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.imshow('image', img)


def write_to_file(lm_List):
    with open(PATH_OUTPUT + get_name_without_ending(PATH_PICTURE) + ".tlms", "w") as f:
        for line in lm_List:
            f.write(f"{line[0]} 1 {line[1]} {line[2]}\n")  # so far always visible


# driver function
if __name__ == "__main__":

    img = cv2.imread(PATH_PICTURE, 1)
    cv2.imshow('image', img)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, landmarks[0][0], (5, 25), font,
                1, (255, 0, 0), 2)
    cv2.imshow('image', img)
    cv2.setMouseCallback('image', click_event)
    cv2.waitKey(0)  # press 0 to exit
    write_to_file(landmarks)
    cv2.destroyAllWindows()
