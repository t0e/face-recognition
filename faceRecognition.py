from PIL import Image
import face_recognition
import cv2

img = cv2.imread('humhealthbnr.jpg')
image = face_recognition.load_image_file("humhealthbnr.jpg")
face_locations = face_recognition.face_locations(image)

print("I found {} face(s) in this photograph.".format(len(face_locations)))

for face_location in face_locations:
    top, right, bottom, left = face_location
    cv2.rectangle(img, (left,top), (right,bottom), (255,0,0), 2)
    # print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
    # You can access the actual face itself like this:
    
cv2.imshow('image', img)
cv2.waitKey(0)