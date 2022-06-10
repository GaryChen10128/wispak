from package.temp_package import *



pathway=Reader.get_UpperPath('.')+'/190709github_package_data/220328data/220328data/circle/KaptureC707D_SixAxis_220328.csv'
Reader.figure(path=pathway)
raw=Reader.export()



#plt.plot(raw[:,1:4])

#plt.plot(raw[:,8:12])

#
adp=Adp_wistron('220328',0,0,0,False)
beta=0.05
dev01=IMU(adp,mag_on=False,beta=beta,mag_cali_on=False,acc_cali_on=False)
plt.title('acc_magnitude')
plt.plot(dev01.accMag)
plt.plot(np.ones(len(dev01.accMag)))
dev01.show_raw()

dev01.acc_new =np.copy(dev01.acc.values)
dev01.acc_mag_new=np.copy(dev01.accMag)
for i in range(len(dev01.acc.values)):
    q=Quaternion(adp.quaternion.values[i,0],adp.quaternion.values[i,1],adp.quaternion.values[i,2],adp.quaternion.values[i,3])
    vec=Quaternion(0,adp.acc.values[i,0],adp.acc.values[i,1],adp.acc.values[i,2])
    out=q*vec*(q.conj())
    dev01.acc_new[i,:]=np.array([out[1],out[2],out[3]])
    dev01.acc_mag_new[i]=(dev01.acc_new[i,0]**2+dev01.acc_new[i,1]**2+dev01.acc_new[i,2]**2)**0.5
#    print(i)

dev01.acc_new=Signal(dev01.acc_new)

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
dev01.accMag=Signal(dev01.accMag)
dev01.acc.values*=9.81
dev01.acc.values[:,2]-=9.81
dev01.position=Signal(np.zeros(dev01.acc.values.shape))

dev01.velocity=Signal.copy(dev01.position)
#plt.plot(dev01.position.values)
dev01.sampleperiod=1/45
#
plt.title('acc_mag')
plt.plot(dev01.accMag.values)
plt.show()
#
#dev01.accMag=Signal(dev01.accMag)
#b, a = sp.signal.butter(4, 0.001/(30), btype = 'highpass')
#dev01.accMag.values = sp.signal.filtfilt(b, a, dev01.accMag.values,axis=0)
#
#plt.title('acc_mag (after highpass)')
#plt.plot(dev01.accMag.values)
#plt.show()
#dev01.accMag.values=abs(dev01.accMag.values)
##
#b, a = sp.signal.butter(4, 5/(30), btype = 'lowpass')
#dev01.accMag.values = sp.signal.filtfilt(b, a, dev01.accMag.values,axis=0)
#plt.title('acc_mag (after lowpass)')
#plt.plot(dev01.accMag.values)
#
#plt.show()

for i in range(dev01.acc.length):
    if i==0:
        dev01.velocity.values[i]=dev01.acc.values[i]*dev01.sampleperiod
    elif abs(dev01.accMag.values[i])<0.078*9.8:#0.004-0.006
        dev01.velocity.values[i]=0
    else:
        dev01.velocity.values[i]=dev01.acc.values[i]*dev01.sampleperiod+dev01.velocity.values[i-1]
        
for i in range(dev01.acc.length):
    if i==0:
        dev01.position.values[i]=dev01.velocity.values[i]*dev01.sampleperiod
        
    else:
        if abs(dev01.accMag.values[i])<0.078*9.8:#0.004-0.006
            dev01.position.values[i]=dev01.velocity.values[i]*dev01.sampleperiod+dev01.position.values[i-1]
#            dev01.position.values[i,2]=0
            pass
        else:
            dev01.position.values[i]=dev01.velocity.values[i]*dev01.sampleperiod+dev01.position.values[i-1]
#plt.plot(dev01.accMag.values)
plt.title('c707d velocity')
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
plt.title('c707d position')
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
#ani=Animation(x,y)
#ani.animateGenerate()
##
fig=plt.figure()
axis=plt.axes(xlim=(np.min(x),np.max(x)),ylim=(np.min(y),np.max(y)))
line, =axis.plot([],[],lw=2)
def init():
    line.set_data([],[])
    return line,
xdata, ydata=[],[]
def animate(i):
    xdata.append(x[i])
    ydata.append(y[i])
    line.set_data(xdata,ydata)
    return line, 
#from matplotlib.animation import FuncAnimation
#ani=FuncAnimation(fig ,animate, init_func=init, frames=x.shape[0],interval=10,blit=True)
#ani.save('anim.mp4',writer='ffmpeg',fps=30)
plt.show()


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x, y, z, c = 'b', marker='o')

plt.show()