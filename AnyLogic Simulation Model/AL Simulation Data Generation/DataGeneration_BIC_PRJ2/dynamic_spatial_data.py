import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation

spatial_data = pd.read_csv('tripFile.txt')
modified_spatial_data = spatial_data.copy()
modified_spatial_data['TIME']=modified_spatial_data.loc[:,['ST_AGV_START_TIME']]%1440

TIME_WINDOWS = np.arange(0,24*60,60)

fig, ax= plt.subplots()

def convert(minutes): 
    minutes = minutes % (24 * 60) 
    hour = minutes // 60
    minutes %= 60
      
    return "%d:%02d" % (hour, minutes) 

def get_data(start_time, end_time):
    filt = (modified_spatial_data['TIME']>=start_time) & (modified_spatial_data['TIME']<=end_time)
    data = modified_spatial_data.loc[filt, ['INFO_TASK_START_X','INFO_TASK_START_Y','TENANT_ID']]
    return data

def init():
    ax.set(xlim = (0,1000), ylim = (0,1000))

def animate(frame, *args):
    '''
    frame = iterable data, or interval
    *args = extra argument
    '''
    #print(f'frame:{frame}')
    #print(f'args:{args}')

    data= get_data(frame,frame+60)
    data_group = data.groupby(['TENANT_ID'])

    tenant_ids = list(data_group.groups.keys())
    
    ax.clear()
    ax.set(xlim = (0,1000), ylim = (0,1000), title=f'Requests in time interval {convert(frame)} to {convert(frame+60)}')
    for tenant in tenant_ids:
        try:
            x = data_group.get_group(tenant)['INFO_TASK_START_X']
            y = data_group.get_group(tenant)['INFO_TASK_START_Y']
            ax.plot(x,y, marker = 'o', linestyle='', label = f'Tenant {tenant}')
        except KeyError as exception:
            print(exception)
            pass
    ax.legend(bbox_to_anchor=(1,0.5))

    
    

ani = animation.FuncAnimation(fig, animate,frames = TIME_WINDOWS,fargs=[10,20,'hello'],init_func=init, interval = 500)
plt.show()
    


