import cv2

for i in range(168):
  filename = "fileme/{}.png"
  filename = filename.format(i)
  image = cv2.imread(filename)
  detector = cv2.QRCodeDetector()
  data, vertices_array, binary_qrcode = detector.detectAndDecode(image)
  print(data,end="")