from package.temp_package import *



a=np.array([[1,2,3],[4,5,6],[7,8,9]])
pathway=Reader.get_UpperPath('.')+'/190709github_package_data/220310iphoneDATA/accIphone5.csv'
Reader.figure(path=pathway)
raw=Reader.export()

#plt.plot(raw[:,1:4])
adp=Adp_iphone('220310',0,0,3,False)
beta=0.05
dev01=IMU(adp,mag_on=False,beta=beta,mag_cali_on=False,acc_cali_on=False)
#dev01.show_raw()
dev01.acc.values*=9.81
dev01.position=Signal(np.zeros(dev01.acc.values.shape))

dev01.velocity=Signal.copy(dev01.position)
#plt.plot(dev01.position.values)
dev01.sampleperiod=1/25

plt.title('acc_mag')
plt.plot(dev01.accMag.values)
plt.show()

b, a = sp.signal.butter(4, 0.001/(30), btype = 'highpass')
dev01.accMag.values = sp.signal.filtfilt(b, a, dev01.accMag.values,axis=0)

plt.title('acc_mag (after highpass)')
plt.plot(dev01.accMag.values)
plt.show()
dev01.accMag.values=abs(dev01.accMag.values)
#
b, a = sp.signal.butter(4, 5/(30), btype = 'lowpass')
dev01.accMag.values = sp.signal.filtfilt(b, a, dev01.accMag.values,axis=0)
plt.title('acc_mag (after lowpass)')
plt.plot(dev01.accMag.values)

plt.show()

for i in range(dev01.acc.length):
    if i==0:
        dev01.velocity.values[i]=dev01.acc.values[i]*dev01.sampleperiod
    elif abs(dev01.accMag.values[i])<0.05:#0.004-0.006
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
plt.title('iphone position')
plt.scatter(dev01.position.values[:,0],dev01.position.values[:,1], label='path') 
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()


t=20
freq=60
x=np.linspace(0,t,t*freq)
y=np.sin(ts)*2*np.pi*freq
plt.scatter(x,y, label='artificail signal') 
plt.grid()
plt.xlabel('x')
plt.ylabel('t')
plt.legend()
plt.show()


x=dev01.position.values[:,0]
y=dev01.position.values[:,1]
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
from matplotlib.animation import FuncAnimation
ani=FuncAnimation(fig ,animate, init_func=init, frames=x.shape[0],interval=10,blit=True)
ani.save('anim.mp4',writer='ffmpeg',fps=30)