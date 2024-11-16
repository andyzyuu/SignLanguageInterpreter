# from angles import calcAngles
import cv2 
import mediapipe as mp


cap = cv2.VideoCapture(0)

mp_drawing = mp.solutions.drawing_utils #interconnecting nodes
mp_drawing_styles = mp.solutions.drawing_styles # styling 
mp_hands = mp.solutions.hands # track hands in real time, hand is a class

hands = mp_hands.Hands()

while cap.isOpened():
    ret, frame = cap.read()
    #Flip the frame
    image = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
    
    
    #Storing the results 
    result = hands.process(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS) #draw lines from node to node
    
    cv2.imshow('Live Video', image)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    

    
cap.release()
cv2.destroyAllWindows()
cv2.waitKey(1)