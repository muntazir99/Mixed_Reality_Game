import cv2
import numpy as np

def detect_board(img):
    img = cropping(img, 0)
    #  img = processing(img)
    imgContours, bboxs, centers, radius = Contours(img)  # Call the Contours function and get contours and bounding boxes
    return imgContours, bboxs

def cropping(img, cropVal):
    h, w, c = img.shape
    img = img[int(cropVal * h):h, 0:w]
    return img

def processing(img):
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(gray, (3, 3), 1)

    # Perform Canny edge detection
    edges = cv2.Canny(blurred, 50, 120)

    # Apply morphological operations (dilation and erosion) to close gaps
    kernel = np.ones((5, 5), np.uint8)
    edges = cv2.dilate(edges, kernel, iterations=1)
    edges = cv2.erode(edges, kernel, iterations=1)

    return edges

def rescaling(img, scale=0.75):
    height = int(img.shape[0] * scale)
    width = int(img.shape[1] * scale)
    dimensions = (width, height)
    return cv2.resize(img, dimensions, interpolation=cv2.INTER_AREA)

def Contours(img):
    # imgContours = img.copy()  #  Create a copy of the image to draw contours on
    img = processing(img)
    h, w = img.shape  # Get the height and width of the image
    imgContours = img.copy()
    contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    bboxs = []  # List to store bounding box coordinates
    centers = []
    radius = []

    for idx, cnt in enumerate(contours):  # Iterate through each contour
        area = cv2.contourArea(cnt)
        if 500 < area < 250000: 

            (x2,y2),radii = cv2.minEnclosingCircle(cnt)
            center = (int(x2), int(y2))
            radii = int(radii)
            centers.append(center)
            radius.append(radii)
            print("center : ", center)
            cv2.circle(imgContours, center, radii, (0,255,0), 2)
            cv2.circle(imgContours, center, 2, (0,0,255), 3)

            # Draw the contour
            cv2.drawContours(imgContours, contours, idx, (255, 0, 255), 2)  # Draw the contour
            x, y, width, height = cv2.boundingRect(cnt)
            cv2.rectangle(imgContours, (x, y), (x + width, y + height), (255, 0, 0), 3)
            bboxs.append((x, y, width, height))  # Store the bounding box coordinates

    return imgContours, bboxs, centers, radius

img = cv2.imread(r"C:\Users\Sahil Sahu\Desktop\Mixed_reality_game\resource\testing3.jpg")

# Detect objects, plot contours, and draw bounding boxes
imgContours, bboxs = detect_board(img)

# Display the image with contours and bounding boxes
cv2.imshow("Board Detection", rescaling(imgContours, 0.5))
cv2.waitKey(0)
cv2.destroyAllWindows()

# Print the detected bounding box coordinates
for bbox in bboxs:
    print("Bounding Box:", bbox)
