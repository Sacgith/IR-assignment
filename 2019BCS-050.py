import numpy as np

def RotationMatrix(axis, theta):
    theta = (theta / 180)
    theta*=np.pi
    if axis == 'x':
        return np.array(((1, 0, 0),(0, np.cos(theta), -np.sin(theta)), (0, np.sin(theta), np.cos(theta))))
    if axis == 'y':
        return np.array(((np.cos(theta), 0, np.sin(theta)), (0, 1, 0), (-np.sin(theta), 0, np.cos(theta))))
    if axis == 'z':
        return np.array(((np.cos(theta), -np.sin(theta), 0), (np.sin(theta), np.cos(theta), 0), (0, 0, 1)))
    raise Exception("invalid axis")

def Transform(axises, point, thetas, translation):
    rMatrix = np.array(((1, 0, 0), (0, 1, 0), (0, 0, 1)))
    for i in range(len(axises)):
        axis = axises[i].lower()
        if not (axis == 'x' or axis == 'y' or axis == 'z'):
            print("invalid axis")
            return
        temp_Rotaion_Matrix =RotationMatrix(axis, thetas[i])
        rMatrix = np.matmul(rMatrix, temp_Rotaion_Matrix)
    translate = np.concatenate((rMatrix, np.transpose(translation).reshape((3, 1))), axis=1)
    translate= np.concatenate((translate, [(0, 0, 0, 1)]), axis=0)
    point = np.concatenate((point, [1]), axis=0).reshape(4, 1)
    result = np.matmul(translate, point)
    return result
total = int(input(" no. of rotations: "))
axis = []
theta = []
for i in range(total):
    axis.append(input("frame about axis(x, y or z): "))
    theta.append(float(input("rotation degree in anticlockwise direction: ")))
translate = np.array(input("enter translation vector: ").strip().split(), float)
point = np.array(input("enter point in current frame: ").strip().split(), float)
res = Transform(axis, point, theta, translate)
print('co-ordinate of pinte in frame:', res[0][0], " ", res[1][0], " ", res[2][0])
