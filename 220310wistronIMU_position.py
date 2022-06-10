from package.temp_package import *

#pathway=Reader.get_UpperPath('.')+'/190709github_package_data/220308positionTrack/Kapture42A7F_SixAxis_220308.csv'
#Reader.figure(path=pathway)
#raw=Reader.export()
#adp=Adp_wistron('220308',0,0,0,False)
#beta=0.05
#dev01=IMU(adp,mag_on=False,beta=beta,mag_cali_on=False,acc_cali_on=False)
#dev01.gyr.values=dev01.gyr.values-np.average(dev01.gyr.values,axis=0)
#dev01.show_raw()
#dev01.calc_angle(fake_t_on=False)
#dev01.show_eu()
#plt.title('acc_mag')
#plt.plot(dev01.accMag)



a=np.array([[1,2,3],[4,5,6],[7,8,9]])
pathway=Reader.get_UpperPath('.')+'/190709github_package_data/220310iphoneDATA/accIphone5.csv'
Reader.figure(path=pathway)
raw=Reader.export()

#plt.plot(raw[:,1:4])
adp=Adp_iphone('220310',0,0,0,False)
beta=0.05
dev01=IMU(adp,mag_on=False,beta=beta,mag_cali_on=False,acc_cali_on=False)
dev01.show_raw()
dev01.acc.values*=9.81
dev01.position=Signal(np.zeros(dev01.acc.values.shape))
dev01.velocity=Signal.copy(dev01.position)
#plt.plot(dev01.position.values)
dev01.sampleperiod=1/30
for i in range(dev01.acc.length):
    if i==0:
        dev01.velocity.values[i]=dev01.acc.values[i]*dev01.sampleperiod
    elif dev01.accMag.values[i]<0.048:#0.004-0.006
        dev01.velocity.values[i]=0
    else:
        dev01.velocity.values[i]=dev01.acc.values[i]*dev01.sampleperiod+dev01.velocity.values[i-1]
        
for i in range(dev01.acc.length):
    if i==0:
        dev01.position.values[i]=dev01.velocity.values[i]*dev01.sampleperiod
    else:
        dev01.position.values[i]=dev01.velocity.values[i]*dev01.sampleperiod+dev01.position.values[i-1]
#plt.plot(dev01.accMag.values)
plt.title('iphone velocity')
plt.plot(dev01.velocity.values[:,0],label='x')    
plt.plot(dev01.velocity.values[:,1],label='y')    
plt.plot(dev01.velocity.values[:,2],label='z')    
plt.legend()
plt.grid()
plt.show()



#plt.scatter(dev01.position.values[:100,0],dev01.position.values[:100,1], label='path') 
#plt.grid()
#plt.legend()
#plt.show()
#
#
#plt.scatter(dev01.position.values[100:,0],dev01.position.values[100:,1], label='path') 
#plt.grid()
#plt.legend()
#plt.show()
plt.scatter(dev01.position.values[:,0],dev01.position.values[:,1], label='path') 
plt.grid()
plt.legend()
plt.show()



#plt.title('iphone position')
#plt.plot(dev01.position.values[:,0],label='x')    
#plt.plot(dev01.position.values[:,1],label='y')    
#plt.plot(dev01.position.values[:,2],label='z')    
#plt.legend()
#plt.grid()
#plt.show()
#Ani
#for i in range(dev01.acc.length):
#    print(i)



# plt.plot(dev01.ts.values)
# dev01.show_raw()

# pathway=Reader.get_UpperPath('.')+'/190709github_package_data/210910wistron1min/KaptureE0798_SixAxis_210910.csv'
# Reader.figure(path=pathway)
# raw=Reader.export()


# adp=Adp_wiPstron('210910',0,0,1,False)
# beta=0.05
# dev01=IMU(adp,mag_on=False,beta=beta,mag_cali_on=False,acc_cali_on=False)

# dev01.gyr.values=dev01.gyr.values-np.average(dev01.gyr.values,axis=0)
# dev01.show_raw()
# dev01.calc_angle(fake_t_on=True)
# dev01.show_eu()



# pathway=Reader.get_UpperPath('.')+'/190709github_package_data/210913devices1minStatic/Kapture3B1FA_SixAxis_210913.csv'
# pathway=Reader.get_UpperPath('.')+'/190709github_package_data/210913devices1minStatic/Kapture3CDD4_SixAxis_210913.csv'
# pathway=Reader.get_UpperPath('.')+'/190709github_package_data/210913devices1minStatic/Kapture735EC_SixAxis_210913.csv'
# pathway=Reader.get_UpperPath('.')+'/190709github_package_data/210913devices1minStatic/Kapture97681_SixAxis_210913.csv'
# pathway=Reader.get_UpperPath('.')+'/190709github_package_data/210913devices1minStatic/KaptureE0798_SixAxis_210913.csv'
# Reader.figure(path=pathway)
# raw=Reader.export()
#adp=Adp_wistron('210913',0,0,1,False)
#beta=0.05
#dev01=IMU(adp,mag_on=False,beta=beta,mag_cali_on=False,acc_cali_on=False)
# dev01.gyr.values=dev01.gyr.values-np.average(dev01.gyr.values,axis=0)
# dev01.show_raw()
# dev01.calc_angle(fake_t_on=True)
# dev01.show_eu()



# from Kalman import KalmanFilter
# from conversion import accelerometer_to_attitude, euler_to_quaternion, quoternion_to_euler_angles, gyro_transition_matrix, normalize_quaternion
# Q = np.array([[10 ** -4, 0, 0, 0],
#             [0, 10 ** -4, 0, 0], 
#             [0, 0, 10 ** -4, 0], 
#             [0, 0, 0, 10 ** -4]])

# R = np.array([[10, 0, 0, 0],
#             [0, 10, 0, 0],
#             [0, 0, 10, 0],
#             [0, 0, 0, 10]])
# delta_t=1/31


# x0 = np.array(euler_to_quaternion(0,0,0))
# F = np.identity(4)
# H = np.identity(4)
# P = np.eye(4)

# kalman = KalmanFilter(x0, F, H, P, Q, R)

# Collect Data
# df = pd.read_excel("data/simulated_data.xlsx", engine="openpyxl")
# accelerometer_data = np.array([df["Accel X"], df["Accel Y"], df["Accel Z"]], ndmin=2).transpose()
# gyro_data = np.array([(df["Gyro Phi"]), (df["Gyro Theta"]), (df["Gyro Omega"])], ndmin=2).transpose()

# time = np.linspace(0, 200.1, num=20001)
# kalman_corrected_phi = []
# kalman_corrected_theta = []
# kalman_corrected_omega = []
# i = 0

# buffers_accel = np.zeros((3,6))
# buffers_gyros = np.zeros((3,6))
# buffers = np.zeros((6,6))

# for i in range(len(dev01.gyr.values)):
    
#     accelerometer_measurement = dev01.gyr.values[i] 
#     gyro_measurement = dev01.acc.values
    
#     F = gyro_transition_matrix(gyro_measurement[0], gyro_measurement[1], gyro_measurement[2], delta_t)
#     kalman.update_state_transition(F)

#     kalman.predict()

#     z = euler_to_quaternion(*accelerometer_to_attitude(accelerometer_measurement[0], accelerometer_measurement[1], accelerometer_measurement[2]))
#     print('z',z)
#     z=list()
#     x = kalman.correct(z)
    
    # x = normalize_quaternion(*x)
    # kalman.normalize_x(x)

    # phi, theta, omega = quoternion_to_euler_angles(*x)
