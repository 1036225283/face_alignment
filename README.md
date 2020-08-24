# face_align
this is a project for: Full convolution face alignment
show:
![pic1](https://github.com/sunnythree/face_alignment/blob/master/data/t1.png)
![pic2](https://github.com/sunnythree/face_alignment/blob/master/data/t2.png)
![pic3](https://github.com/sunnythree/face_alignment/blob/master/data/t3.png)

description:
CnnAlignHard is a better model for face alignment,so use XXXHard.py 

train:   
```
python3.6 TrainHard.py -b 100 -l 0.001 -e 2000 -s 500  
```
if you want train from last time, just add -p True
```
python3.6 TrainHard.py -b 100 -l 0.001 -e 2000 -s 500  -P true
```
test on  eval dataset:
```
python3.6 TestHard.py
```
test with camera
```
python3.6 CameraShowHard.py
```