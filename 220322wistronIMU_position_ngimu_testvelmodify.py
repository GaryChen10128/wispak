from package.temp_package import *



#pathway=Reader.get_UpperPath('.')+'/190709github_package_data/220329ngimudata/220329ngimudata/walkaround4/NGIMU - 0029C6FC/quaternion.csv'
#Reader.figure(path=pathway,header=0)
#raw=Reader.export()
##plt.plot(raw[:,1:4])
#plt.plot(raw[:,1:5])
#plt.show()
#pathway=Reader.get_UpperPath('.')+'/190709github_package_data/220329ngimudata/220329ngimudata/walkaround4/NGIMU - 0029C6FC/sensors.csv'
#Reader.figure(path=pathway,header=0)
#raw=Reader.export()
##plt.plot(raw[:,1:4])
#
#plt.plot(raw[:,1:4])
#plt.show()
#plt.plot(raw[:,4:7])
#plt.show()



adp=Adp_ngimu('220329',0,0,3,False,cali_path='')
adp_cali=Adp_ngimu('220329',0,0,4,False,cali_path='')

cali_mag(adp_cali.mag.values,adp.mag.values)
plt.show()
#ellipse_fitting2(adp_cali.mag.values,adp.mag.values)
beta=0.05
dev01=IMU(adp,mag_on=True,beta=beta,mag_cali_on=False,acc_cali_on=False)


#plot acc_magnitude
plt.plot(adp.quaternion.values)
plt.title('acc_magnitude')
plt.plot(dev01.accMag.values)
plt.plot(np.ones(dev01.accMag.length))
#plot acc_magnitude
dev01.show_raw()
dev01.show_qq()
dev01.acc_new =np.copy(dev01.acc.values)
dev01.acc_mag_new=np.copy(dev01.accMag.values)
for i in range(len(dev01.acc.values)):
    q=Quaternion(adp.quaternion.values[i,0],adp.quaternion.values[i,1],adp.quaternion.values[i,2],adp.quaternion.values[i,3])
    vec=Quaternion(0,adp.acc.values[i,0],adp.acc.values[i,1],adp.acc.values[i,2])
    out=q*vec*(q.conj())
    dev01.acc_new[i,:]=np.array([out[1],out[2],out[3]])
    dev01.acc_mag_new[i]=(dev01.acc_new[i,0]**2+dev01.acc_new[i,1]**2+dev01.acc_new[i,2]**2)**0.5

dev01.calc_angle(True)

dev01.acc_new=Signal(dev01.acc_new)
#plt.plot(adp.quaternion.values)

#plt.plot(adp.quaternion.values[:,0],label='x')    
#plt.plot(adp.quaternion.values[:,1],label='y')    
#plt.plot(adp.quaternion.values[:,2],label='z')   
#plt.plot(adp.quaternion.values[:,3],label='w')   
#plt.legend()
#plt.show()

plt.plot(dev01.acc_new.values)
#q1=Quaternion(0.707,0,0,0.707)
#q2=Quaternion(0.707,0.707,0,0)
##q3=q1*q2
#vec=Quaternion(0,1,0,0)
##print(q3._q)
##
#out=q1*vec*(q1.conj())
#print(out._q)
dev01.acc=dev01.acc_new
#dev01.accMag=Signal(dev01.accMag)
dev01.acc.values*=9.81
#dev01.acc.values[:,2]-=9.81
dev01.acc_new.values[:,2]-=9.81
dev01.position=Signal(np.zeros(dev01.acc.values.shape))

dev01.velocity=Signal.copy(dev01.position)
#plt.plot(dev01.position.values)
samplerate=50
dev01.sampleperiod=1/samplerate
#
plt.show()
plt.title('acc_mag')
plt.plot(dev01.accMag.values)
plt.show()
#
#dev01.accMag=Signal(dev01.accMag)
b, a = sp.signal.butter(4, 2*0.001/(samplerate), btype = 'highpass')
dev01.accMag.values = sp.signal.filtfilt(b, a, dev01.accMag.values,axis=0)

plt.title('acc_mag (after highpass)')
plt.plot(dev01.accMag.values)
plt.show()
dev01.accMag.values=abs(dev01.accMag.values)
#
b, a = sp.signal.butter(4, 2*5/(samplerate), btype = 'lowpass')
dev01.accMag.values = sp.signal.filtfilt(b, a, dev01.accMag.values,axis=0)

plt.title('acc_mag (after lowpass)')
plt.plot(dev01.accMag.values)
plt.plot(np.ones(dev01.accMag.length)*0.8)
#
plt.show()
stationary=dev01.accMag.values<0.3 #越大peak越多 ## best 0.1
for i in range(dev01.acc.length):
    if i==0:
        dev01.velocity.values[i]=dev01.acc_new.values[i]*dev01.sampleperiod
    elif stationary[i]:#0.18, 0.3
        dev01.velocity.values[i]=0
    else:
        dev01.velocity.values[i]=dev01.acc_new.values[i]*dev01.sampleperiod+dev01.velocity.values[i-1]
        
velDrift=np.zeros(dev01.velocity.length)

for i in range(dev01.acc.length):
    if i==0:
        dev01.position.values[i]=dev01.velocity.values[i]*dev01.sampleperiod
    else:
        if stationary[i]:
            dev01.position.values[i]=dev01.velocity.values[i]*dev01.sampleperiod+dev01.position.values[i-1]
#            dev01.position.values[i,2]=0
            pass
        else:
            dev01.position.values[i]=dev01.velocity.values[i]*dev01.sampleperiod+dev01.position.values[i-1]
#plt.plot(dev01.accMag.values)
plt.title('ngimu velocity')
plt.plot(dev01.velocity.values[:,0],label='x')    
plt.plot(dev01.velocity.values[:,1],label='y')    
plt.plot(dev01.velocity.values[:,2],label='z')    
plt.plot(dev01.accMag.values,label='acc_mag')  
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
plt.title('ngimu position')
plt.scatter(dev01.position.values[:,0],dev01.position.values[:,1], label='path') 

plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()



## dont do below
#t=20
#freq=50
#x=np.linspace(0,t,t*freq)
#y=np.sin(ts)*2*np.pi*freq
#plt.scatter(x,y, label='artificail signal') 
#plt.grid()
#plt.xlabel('x')
#plt.ylabel('t')
#plt.legend()
#plt.show()
#
#
x=dev01.position.values[:,0]
y=dev01.position.values[:,1]
z=dev01.position.values[:,2]
#fig=plt.figure()
#plt.grid()
#plt.xlabel('x')
#plt.ylabel('y')
#plt.legend()
#axis=plt.axes(xlim=(np.min(x),np.max(x)),ylim=(np.min(y),np.max(y)))
#line, =axis.plot([],[],lw=2)
#def init():
#    line.set_data([],[])
#    return line,
#xdata, ydata=[],[]
#def animate(i):
#    xdata.append(x[i])
#    ydata.append(y[i])
#    line.set_data(xdata,ydata)
#    return line, 
#from matplotlib.animation import FuncAnimation
#ani=FuncAnimation(fig ,animate, init_func=init, frames=x.shape[0],interval=10,blit=True)
#ani.save('anim.mp4',writer='ffmpeg',fps=30)


#not complete yet
#ani=Animation(x,y)
#ani.animateGenerate()
##
plt.show()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x, y, z, c = 'b', marker='o')

plt.show()
