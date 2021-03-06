import binascii
import time
import cv2
import numpy
from flask import stream_with_context, Response
from base64 import b64decode, b64encode
from PIL import Image
from base64 import decodestring
from io import BytesIO
from flask_socketio import SocketIO



# 이미지 흑백 처리
# testImg = cv2.imread("Resources/react-logo.png", 0)
#
# resizedImg = cv2.resize(testImg, (800,600))
#
#
# cv2.imshow("testImg", resizedImg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 동영상 흑백 처리


def giveGrayEffect(img_uri):
    if img_uri:
        img_uri = img_uri.split(',')[1]
        img = binascii.a2b_base64(img_uri)
        img = Image.open(BytesIO(img))
        img = numpy.array(img)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # numpy.ndarray 타입 데이터 반환

        def nparray_to_img():
            # Reshape the array into a
            # familiar resoluition
            array = numpy.reshape(img_gray, (240, 240))

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

        return nparray_to_img()
        # imgGray, buffer = cv2.imencode('.jpg', imgGray)
        # # jpg_as_text = base64.b64encode(buffer)
        # cv2.imshow("gray",imgGray)




