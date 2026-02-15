import matplotlib.pyplot as plt
import numpy as np
import csv


'''
run:
python3 Generator-Lorenz-attractor-20260205.py

then run  
python3 PeEn-run-20260131.py -i ./False-ECG-modul-sinus.csv -w 500 -d 5 -e 10

'''


def save_file_csv(xyz, time, output_file_name):
    print('BEGIN: save_file_csv')
    # self.output_file_name = \
    #     self.save_file_name(self.save_file_suffix_csv)
    print('xyz = ', xyz)
    print('time = ',time)
    print('len(time) = ', len(time),
          'len(xyz) = ', len(xyz)) #; exit(1)
    x = xyz[:,0]
    y = xyz[:,1]
    z = xyz[:,2]
    print('x = ',x)
    print('y = ',y)
    print('z = ',z)
    print('time = ',time)
    # #list_out = np.dstack((time, x, y, z))
    # #list_out = np.dstack((time, xyz))
    #list_out = np.concatenate((time, x,yz), axis=1)
    list_out = np.hstack((time, xyz))
    print('list_out',list_out)  #; exit(1)
    #output_file_name = 'False-Lorenz-attractor-new.csv'
    with open(output_file_name, mode='w') as ofile:
        #print('time = ', self.time)
        try:
            write_file = csv.writer(ofile, delimiter=',', \
                                    quotechar='"', quoting=csv.QUOTE_MINIMAL)
            array_size = len(time)
            for i in range(array_size):
                #print(str(time[i,0]), str(xyz[i,0]), str(xyz[i,1]), str(xyz[i,2])) 
                row = [str(time[i,0]), str(xyz[i,0]), str(xyz[i,1]), \
                       str(xyz[i,2])] # + '\n']
                write_file.writerow(row)
                #if i == 10:
                #    break
                #print(f'Output data saved to file: {output_file_name}') #;exit(1)
        except:
            print("Data were not saved")
    print('END:   save_file_csv')

    # array_size = len(time)
    # save_data = np.zeros((array_size,4))
    # for i in range(0,array_size):
    #     save_data[i,0] = time[i]
    #     save_data[i,1] = xyz[i,0]
    #     save_data[i,2] = xyz[i,1]
    #     save_data[i,3] = xyz[i,2]
    # try:
    #     output_file_name_new = output_file_name + '1'
    #     np.savetxt(output_file_name_new,save_data,delimiter=',') 
    #     print("Data saved")
    # except:
    #     print("Data were not saved")
    # print('END:   save_file_csv')
    

def lorenz_derivation(xyz, *, s=10, r=28, b=2.667):
    x, y, z = xyz
    #print('xyz = ', xyz)
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return np.array([x_dot, y_dot, z_dot])


def main():
    dt = 0.001            ## Step 0.01 or 0.001
    num_steps = 100_000   ## shorted data 10_000, longer data 100_000
    out_file_name = "False-Lorenz-attractor.csv"


    xyzs    = np.empty((num_steps + 1, 3))
    time    = np.empty((num_steps + 1, 1))
    xyzs[0] = (0, 1., 1.05)
    time[0] = (0.)

    #print('fill:time[0] = ',time[0], 'xyzs[0] = ', xyzs[0])
    for i in range(0,num_steps):
        xyzs[i + 1] = xyzs[i] + lorenz_derivation(xyzs[i]) * dt
        time[i + 1] = float(i + 1)
        #print('fill:time[i+1] = ',time[i+1], 'xyzs[i + 1] = ', xyzs[i + 1])

    save_file_csv(xyzs,time,out_file_name)

    ax = plt.figure().add_subplot(projection='3d')
    ax.plot(*xyzs.T, lw=0.5)
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    ax.set_title("Lorenz Attractor")
    plt.savefig("Lorenz-Attractor.png")

    plt.show()

if __name__=='__main__':
    main()
