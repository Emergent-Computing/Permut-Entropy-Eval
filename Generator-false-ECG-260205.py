import numpy as np
import matplotlib.pyplot as plt


'''
run:
python3 Generator-false-ECG-260205.py

then run  
python3 PeEn-run-20260206.py -i ./False-ECG-sinus.csv -w 500 -d 3 -e 1

'''


array_size    = 100000
time          = np.zeros((array_size))
data_ECG      = np.zeros((array_size))
file_name_out = 'False-ECG-sinus.csv'


def generate_ECG_sinus():
    global time, data_ECG
    for i in range(0,array_size):
        time[i] = i
        data_ECG[i] = np.sin(i/57.2958) - 0.33

    
def save_data():
    save_data = np.zeros((array_size,2))
    for i in range(0,array_size):
        save_data[i,0] = time[i]
        save_data[i,1] = data_ECG[i]
        
    try:
        np.savetxt(file_name_out,save_data,delimiter=',') 
        print(f'Output saved into the file: >>> {file_name_out} <<<')
    except:
        print("Data were not saved")

        
def plot_curve():
    plt.plot(time[:],data_ECG[:])
    plt.pause(2)
    plt.cla()
    plt.plot(time[:1000],data_ECG[:1000])
    plt.pause(2)
    plt.show()

    
def main():
    print("Program 'Generator-false-ECG' initiated.")
    generate_ECG_sinus()
    plot_curve()
    save_data()
    print("Program 'Generator-false-ECG' finalized.")

    
if __name__=='__main__':
    main()
