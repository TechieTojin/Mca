import cv2
from deepface import DeepFace

# Initialize the camera
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Load the reference image
reference_img_path = r"C:\Users\digi_\OneDrive\Desktop\DP.jpg"
reference_img = cv2.imread(reference_img_path)

if reference_img is None:
    print(f"Error: Could not load reference image from {reference_img_path}.")
    exit()

def check_face(frame):
    try:
        result = DeepFace.verify(frame, reference_img.copy())
        return result['verified']
    except Exception as e:
        print(f"Verification error: {str(e)}")
        return False

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break
    
    face_match = check_face(frame)

    if face_match:
        cv2.putText(frame, "MATCH", (20, 450),
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 3)
    else:
        cv2.putText(frame, "NOT A MATCH", (20, 450),
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 3)

    cv2.imshow("video", frame)
    
    key = cv2.waitKey(1)
    if key == ord("j"):  # Press "j" to exit
        break

# Release the camera and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
