import cv2 as cv

# Images, videos, live video
def rescale_frame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

# Only works for live video
def change_res(width, height):
    capture.set(3, width)
    capture.set(4, height)

# capture = cv.VideoCapture('Resources/Videos/dog.mp4')

# while True:
#     isTrue, frame = capture.read()
#     frame_resized = rescale_frame(frame)

#     cv.imshow('Video Resized', frame_resized)
#     if cv.waitKey(20) and 0xFF == ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()

# cv.waitKey(0)

img = cv.imread('Resources/Photos/cat.jpg')
cv.imshow('Cat', rescale_frame(img, 0.1))

cv.waitKey(0)