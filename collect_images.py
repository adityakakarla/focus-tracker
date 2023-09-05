import cv2
import os
import time
import uuid

IMAGES_PATH = 'data/phone_images/'

labels = ['phone', 'no_phone']
number_imgs = 100

for label in labels:
    os.system('mkdir "data/phone_images/{}"'.format(label))
    cap = cv2.VideoCapture(1)
    print('Collecting images for {}'.format(label))
    time.sleep(10)
    for imgnum in range(number_imgs):
        ret, frame = cap.read()
        imagename = os.path.join(IMAGES_PATH, label , label + '{}.jpg'.format(str(uuid.uuid1())))
        print("Image Name:", imagename)
        try:
            if ret:
                with open(imagename, 'wb') as file:
                    file.write(cv2.imencode('.jpg', frame)[1].tobytes())
                cv2.imshow('frame', frame)
                time.sleep(0.5)

                if cv2.waitKey(1) and 0xFF == ord('q'):
                    break
            else:
                print("Error reading frame")
        except Exception as e:
            print(e)
    cap.release()
