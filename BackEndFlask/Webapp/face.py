import cv2
import face_recognition
import os
import glob

#create a class for face recogniation
class FaceRecognition:
    vc = cv2.VideoCapture(0)
    known_faces = []
    known_names = []
    known_faces_paths = []

    registered_faces_path = 'registered/'
    def checkFace(self):
        for name in os.listdir(self.registered_faces_path):
            images_mask = '%s%s/*.jpg' % (self.registered_faces_path, name)
            images_paths = glob.glob(images_mask)
            self.known_faces_paths += images_paths
            self.known_names += [name for x in images_paths]
    
faceObject = FaceRecognition()
def get_encodings(img_path):
    image = face_recognition.load_image_file(img_path)
    encoding = face_recognition.face_encodings(image)
    return encoding[0]

known_faces = [get_encodings(img_path) for img_path in faceObject.known_faces_paths]

