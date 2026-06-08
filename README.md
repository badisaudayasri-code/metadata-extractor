# EXIF Metadata Extractor

## 📌 Project Description
The **EXIF Metadata Extractor** is a lightweight Python-based tool developed under the **Cyber Security & Ethical Hacking** domain.  
It is designed to analyze image files and identify the presence of hidden metadata (EXIF data), which can reveal sensitive information such as file size, image type, and embedded metadata markers.

This project is especially useful in **digital forensics, ethical hacking, and privacy analysis**, where understanding hidden information inside media files is crucial.

---

## 🎯 Objectives
- To extract basic metadata information from image files  
- To detect the presence of EXIF data without using external libraries  
- To ensure compatibility with mobile and low-resource Python environments  
- To understand the role of metadata in cyber security and forensics  

---

## 🧠 How It Works
- Reads the image file in binary mode  
- Calculates file size  
- Identifies image type (JPEG or non-JPEG)  
- Checks whether EXIF metadata exists inside the file  

This approach avoids third-party dependencies, making the tool portable and secure.

---

## 🛠️ Technologies Used
- Python 3  
- OS module  
- Binary file analysis  

