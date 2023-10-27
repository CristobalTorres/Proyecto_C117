import os
import cv2

path="/Users/migue/Desktop/Python/PROYECTO 117 cristobal/images"
images=[]

for file in os.listdir(path):
    name,ext= os.path.splitext(file)

    if ext in [".gif",".jpg",".png","jpeg"]:
        file_name=path+"/"+file
        images.append(file_name)
    
    count=len(images)

    frame=cv2.imread(images[0])
    h,w,c = frame.shape
    size=(w,h)
    out = cv2.VideoWriter('Nevados.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 5, size)

    for i in range(count -1,0,-1):
        frame=cv2.imread(images[1])
        out.write(frame)


print("fin")

print(file_name)
out.release()