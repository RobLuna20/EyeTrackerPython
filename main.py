import cv2
import mediapipe as mp

cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True) #478 landmarks

while True:
    _, frame = cam.read() #read what is coming from camera
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape
    if landmark_points:
        landmarks = landmark_points[0].landmark
        for landmark in landmarks:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x,y), 3, (0,255,0)) #draw circle on frame, center xy, how big radius, color rgb
            print(x, y)
    cv2.imshow('Face Tracker', frame)
    cv2.waitKey(1)


