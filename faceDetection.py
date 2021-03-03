import cv2
import binascii
import numpy
from PIL import Image
from io import BytesIO

def face_detection(img_uri):
    img_uri = img_uri.split(',')[1]
    img = binascii.a2b_base64(img_uri)
    img = Image.open(BytesIO(img))
    img = numpy.array(img)
    # img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # numpy.ndarray 타입 데이터 반환


    face_cascade = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')


    faces = face_cascade.detectMultiScale(img,1.1,1) # the input image, scaleFactor and minNeighbours.

    print(type(img))
    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

        def nparray_to_img(img):
            # Reshape the array into a
            # familiar resoluition
            array = numpy.reshape(img, (240, -1))

            # # show the shape of the array
            # print(array.shape)
            #
            # # show the array
            # print(array)

            # creating image object of
            # above array
            data = Image.fromarray(array)

            # saving the final output
            # as a PNG file
            # data.save('gfg_dummy_pic.png')
            fd = BytesIO()
            data.save(fd, "webp")
            return fd.getvalue()
        img = nparray_to_img(img)
        return img