import gdown
import time

def download_image_repository_from_drive():
    url = "https://drive.google.com/drive/folders/1Ct5QfEFchW4f0ejEFRlJ4ahySA_rOqvj?usp=sharing"
    gdown.download_folder(url, quiet=True, use_cookies=False)

def main():
    download_image_repository_from_drive
    time.slee(600)

if __name__ == "__main__":
    main