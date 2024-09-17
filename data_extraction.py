import os

def data_extraction():
    
    path = os.path.join(os.getcwd(), "Medical-imaging-dataset")
    
    for file in os.listdir(path):
        img_dir = os.path.join(path, file)
        for f in os.listdir(img_dir):        
            print(f)
        
    return file, f
    
data_extraction()