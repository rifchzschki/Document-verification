# Document Verification
Document verification is the implementation of the program described in the paper "One-shot Verification of Paper Certificates with Robust Preprocessing." This program consists of several processing stages: preprocessing, text extraction, QR extraction, and verification. Due to certain limitations, our implementation does not include storage on the blockchain. Therefore, during verification, the program is assumed to have already received the original value (pattern). The output of the program is the validity status of the certificate.

# Dependency
1. This program is running on python 3.9.10. 
2. For the OCR engine we use Paddle OCR (PPOCR V4)
3. Segmentation process using YOLOv8
4. QR Extraction process using pyboof (python library)


# How to run program
1. Clone this repository
```bash
git clone https://github.com/rifchzschki/Document-verification
```
2. Install all dependency
```bash
cd Document-verification
pip install -r requirements.txt
```
3. Make folder input in data for store your capture images
```bash
mkdir data/input
```

4. Make folder output in data for see segmentation result
```bash
cd data
mkdir data/output
```
5. Make folder txtTruth for store your ground truth value of each field in certificate
```bash
mkdir data/txtTruth
```
6. You can store input images in input and ground truth value in txtTruth
7. Run this command in your CLI
```bash
cd src
python main.py --image_name {your-image} --invers {y/n} --output {temp txt for OCR result} --target {ground-truth-txt} --prep {y/n} --ocr {y/n} --verif {y/n}
```
8. See the result in tmp/hasil.txt!
9. All the process will be store in tmp folder, you can changes the scheme if you want


# Authors
1. Muhamad Rifki Virziadeili Harisman
2. Maulvi Ziadinda Maulana
3. Raditya Aditama
