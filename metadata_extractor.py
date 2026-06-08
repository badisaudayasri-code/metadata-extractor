import os

def extract_metadata(image_path):
    try:
        if not os.path.exists(image_path):
            print("❌ Error: Image file not found.")
            return

        with open(image_path, "rb") as f:
            data = f.read()

        print("\n--- Image Metadata ---\n")
        print("File Path :", image_path)
        print("File Size :", len(data), "bytes")

        if data[:2] == b'\xff\xd8':
            print("Image Type : JPEG")
        else:
            print("Image Type : Not JPEG")

        if b'Exif' in data:
            print("EXIF Data  : Found")
        else:
            print("EXIF Data  : Not Found")

    except Exception as e:
        print("❌ Error:", e)


# ---- Main Program ----
if __name__ == "__main__":
    print("Example path:")
    print("/storage/emulated/0/Download/test.jpg\n")

    image_path = input("Enter FULL image file path: ")
    extract_metadata(image_path)