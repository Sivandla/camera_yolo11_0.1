import cv2
from ultralytics import YOLO

model = YOLO("yolo11n.pt")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
	print("Error: không mở được camera")
	exit()

while True:
	# đọc từng khung hình
	ret, frame = cap.read()

	# khi không đọc được
	if not ret:
		print("Error: không đọc được khung")
		break

	# phát hiện đối tượng trong khung
	results = model(frame)

	# gắn nhãn các đối tượng trong khung
	annotated_frame = results[0].plot() 

	# đưa ra các giá trị của các đối tượng được xác định trong khung
	cv2.imshow('YOLO camera', annotated_frame)

	# thoát khỏi nhấn "q"
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
