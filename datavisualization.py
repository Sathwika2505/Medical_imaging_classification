import os, random
import pandas as pd
from PIL import Image

def datavisualization():
    path = os.path.join(os.getcwd(), "Medical-imaging-dataset")
    op =  os.getcwd()
    for file in os.listdir(path):
        print(file)
        
        img_dir = os.path.join(path, file)
        if os.path.isdir(img_dir):
            jpg_files = [f for f in os.listdir(img_dir) if f.endswith(".jpg")]
            random_files = random.sample(jpg_files, min(1, len(jpg_files)))
            print("============",random_files)
            for file_name in random_files:
                img_path = os.path.join(img_dir, file_name)
                img = Image.open(img_path)
                output_image_path = os.path.join(op, f"{file}.jpg")
                img.save(output_image_path)
            
    return file, img
    
datavisualization() 