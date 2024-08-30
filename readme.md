# Document Verification

<div align="center">
  <img src="assets/uhuuy.png" alt="uhuy">
</div>
Document Verification is the implementation of the program described in the paper "One-shot Verification of Paper Certificates with Robust Preprocessing." This program consists of several processing stages: preprocessing, text extraction, QR extraction, and verification. Due to certain limitations, our implementation does not include storage on the blockchain. Therefore, during verification, the program is assumed to have already received the original value (pattern). The output of the program is the validity status of the certificate.

# Dependencies

1. This program runs on Python 3.9.10.
2. For the OCR engine, we use Paddle OCR (PPOCR V4).
3. The segmentation process uses YOLOv8.
4. The QR extraction process uses PyBoof (Python library).

# How to Run the Program

1. Clone this repository:

   ```bash
   git clone https://github.com/rifchzschki/Document-verification
   ```

2. Install all dependencies:

   ```bash
   cd Document-verification
   pip install -r requirements.txt
   ```

3. Create an `input` folder in `data` to store your captured images:

   ```bash
   mkdir data/input
   ```

4. Create `output` and `output_segmentation` folders in `data` to view the segmentation results:

   ```bash
   cd data
   mkdir output
   mkdir output_segmentation
   ```

5. Create a `txtTruth` folder to store the ground truth values for each field in the certificate:

   ```bash
   mkdir txtTruth
   ```

6. Create a `tmp` folder to store your temporary files; all processing will be stored there:

   ```bash
   mkdir tmp
   ```

7. Store input images in the `input` folder and ground truth values in `txtTruth`.
8. Run this command in your CLI:

   ```bash
   cd src
   python main.py --image_name {your-image} --invers {y/n} --output {temp txt for OCR result} --target {ground-truth-txt} --prep {y/n} --ocr {y/n} --verif {y/n}
   ```

9. See the results in `tmp/hasil.txt`.
10. All processes will be stored in the `tmp` folder; you can change the scheme if you want.

# Example

### Captured Image

> First, place your captured image into the `input` folder.
> ![input](assets/input.jpg)

### Segmented Image

> The program will segment your certificate.
> ![input](assets/segmented.jpg)

### Cropped Image

> After segmentation, the segmented area will be cropped, and this process will correct the perspective of the certificate.
> ![input](assets/cropped.jpg)

### Preprocessed Image

> The cropped image will undergo image enhancement and auto-rotation to correct the text direction in the certificate.
> ![input](assets/final.jpg)

### OCR Result

> The text extraction process will extract each text element in the certificate.
> ![input](assets/ocr-result.png)

### QR Result

> Unfortunately, our program is still not robust in this process. For QR detection, we must ensure that the image provided is very clear, especially the QR code section. In this case, we used another image that was clearer but from the same certificate.
> ![input](assets/qr-extractor.jpg)

### Ground Truth Text

> This value would be stored in the database or blockchain. For experimental purposes, we assumed the text is stored as a `.txt` file.
> ![input](assets/groundTruth.png)

### Result

> The verification process will display the result as the validity status of the image.
> ![input](assets/result.png)

# Important Considerations

1. The selection of field values in the ground truth is crucial. You must carefully choose only the important values, and each should have more than 5 characters. When determining field values, ensure that the order and line format match those on the original certificate. This means that each line in the ground truth should correspond to a single line on the original certificate. It is recommended to avoid including sentences that lack significant meaning.

2. For the QR Extractor, we use the PyBoof library. Occasionally, you may encounter errors with this library. There are two possible causes: the QR code was not found, or there is an issue with the library itself. For the second issue, you may need to modify line 160 in the `Lib/site-packages/pyboof/__init__.py` file to:

   ```python
   pbg.mmap_file = mmap.mmap(pbg.mmap_fid.fileno(), length=0)
   ```

3. In the QR Extractor process, we still face challenges when the QR code is not detected properly. We recommend creating the QR code in a sufficiently large size to ensure it can be read clearly from a distance.

# Authors

1. Muhamad Rifki Virziadeili Harisman
2. Maulvi Ziadinda Maulana
3. Raditya Aditama
