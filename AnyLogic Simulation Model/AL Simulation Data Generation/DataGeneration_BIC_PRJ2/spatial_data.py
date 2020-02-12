import matplotlib.pyplot as plt 
import pandas as pd
'''
spatial_data = open('tripFile.txt', 'r').readlines()

print(type(spatial_data))

spatial_data = [line.split(',') for line in spatial_data]
'''
spatial_data = pd.read_csv('tripFile.txt')
print(spatial_data.head())
print(f"Average Reward:{spatial_data['REWARD'].mean()}")


print(spatial_data[spatial_data['TENANT_ID']==0]['REWARD'])
'''
plt.plot(spatial_data['ST_AGV_START_X'],spatial_data['ST_AGV_START_Y'], label = spatial_data['TENANT_ID'])
plt.legend()
plt.show()
'''
plt.figure('Spatial Distribution of order arrivals')
for i in range(5):
    plt.plot(spatial_data[spatial_data['TENANT_ID']==i]['INFO_TASK_START_X'],spatial_data[spatial_data['TENANT_ID']==i]['INFO_TASK_START_Y'], label = f'Tenant {i}', marker = 'o', linestyle = '')
plt.legend(loc = 'best', bbox_to_anchor=(1, 0.5))
plt.title('Spatial Distribution of order arrivals')
plt.show()

