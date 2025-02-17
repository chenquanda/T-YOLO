import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('ultralytics/cfg/models/v8/t-yolo.yaml')
    model.train(data=r'',
                cache=False,
                imgsz=640,
                epochs=250,
                batch=8,
                close_mosaic=0,
                workers=8,
                device='0',
                optimizer='SGD',
                resume=False,
                )