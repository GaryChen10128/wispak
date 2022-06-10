from package.temp_package import *
from calibraxis import Calibraxis

pathway=Reader.get_UpperPath('.')+'/190709github_package_data/accCalibration.csv'
Reader.figure(path=pathway)
raw=Reader.export()
raw=raw[0:-10]
plt.title('old acc')
plt.plot(raw[:,1:4])
plt.show()
acc=np.zeros([len(raw),3], dtype=np.float64)
for i in range(len(raw)):
    acc[i]=np.array(raw[i][1:4], dtype=np.float64)
    #print(np.array(list[1:4], dtype=np.float64))

#acc=np.array(acc, dtype=np.float64)
c=Calibraxis()
c.add_points(acc)
#c.add_points(np.zeros([9,3]))

c.calibrate_accelerometer()
print('--------------------------------')
print(c.bias_vector)
print(c.scale_factor_matrix)

newAcc=c.batch_apply(acc)
plt.title('new acc')
plt.plot(newAcc)
plt.show()


finalacc=[]
for tturple in newAcc:
    finalacc.append([tturple[0],tturple[1],tturple[2]])
newAcc=np.array(finalacc)
plt.title('acc_x comparison')
plt.plot(acc[:,0])
plt.plot(newAcc[:,0])

plt.show()
