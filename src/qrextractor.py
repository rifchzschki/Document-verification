import numpy as np
import os
import pyboof as pb
import cv2

pb.__init_memmap() #Optional

class QR_Extractor:
    # Src: github.com/lessthanoptimal/PyBoof/blob/master/examples/qrcode_detect.py
    def __init__(self):
        self.detector = pb.FactoryFiducial(np.uint8).qrcode()
    
    def extract(self, img_path):
        if not os.path.isfile(img_path):
            print('File not found:', img_path)
            return None
        image = pb.load_single_band(img_path, np.uint8)
        self.detector.detect(image)
        qr_codes = []
        for qr in self.detector.detections:
            qr_codes.append({
                'text': qr.message,
                'points': qr.bounds.convert_tuple()
            })
        return qr_codes
    
def extract_text_from_image(image_path):
    qr_extractor = QR_Extractor()
    qr_codes = qr_extractor.extract(image_path)
    if qr_codes is None:
        return []
    return qr_codes[0]['text'], qr_codes[0]['points']

def resize_image(img, ratio, points):
    resized = cv2.resize(img, (int(img.shape[1]*ratio),int(img.shape[0]*ratio)), interpolation=cv2.INTER_AREA)
    # for i in range(len(points)):
    #     points[i][0]*=ratio
    #     points[i][1]*=ratio
    return resized

def show_result(image_path, ratio):
    image = cv2.imread(image_path)  
    text, points = extract_text_from_image(image_path=image_path)

    pts = np.array(points, np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv2.polylines(image, [pts], isClosed=True, color=(0, 255, 0), thickness=2)
    image = resize_image(image, ratio, points)
    cv2.putText(image, text, (int(points[3][0]*ratio), int(points[3][1]*ratio )+ 20),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
    # cv2.imshow('Image with Box and Text', image)
    cv2.imwrite('../assets/qr-extractor.jpg', image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

show_result("../data/tmp/1.jpg", 0.4)