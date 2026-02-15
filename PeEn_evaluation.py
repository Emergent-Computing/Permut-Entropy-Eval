import numpy as np
import matplotlib.pyplot as plt
import math
import sys, csv, os
import itertools
import argparse
import time


class PeEn:

    def __init__(self, points_per_sec=1000, segment_size=100, embed_delay=1,
                 embed_dimension=3):
        print('init input: ',points_per_sec, segment_size, embed_delay,
                 embed_dimension); 
        # Class Variables:
        self.input_file_name = ''
        #self.input_file      = ''
        self.data_file       = []
        self.output_file_name  = 'Something-went-wrong.csv'
        self.figure_displ_time = 0.5 # [s]  # Display  time of figures
        self.array_size      = 0
        self.segment_size    = segment_size
        self.embed_dimension = embed_dimension
        self.embed_delay     = 1
        self.points_per_sec  = points_per_sec
        self.ECG_data        = np.empty(shape=[0,2])
        self.perm_entr_array = np.empty(shape=[0])
        self.time            = np.empty(shape=[0])
        self.embed_delay     = embed_delay
        self.start_time      = -1
        self.end_time        = -1
        self.save_file_preffix    = 'PeEn-'
        self.save_file_suffix_csv = '-output.csv'
        self.save_file_suffix_png = '-output.png'
        self.save_PNG        = 0
        self.display_graphs  = 0
        self.restrict_data   = 1000

        
    def hello(self):
        print('Hello from class PeEn')

        
    def time_start(self):
        self.start_time = time.time()
        return self.start_time

    
    def time_end(self):
        self.end_time = time.time()
        return self.end_time
        
        
    def time_total(self):
        return (self.end_time - self.start_time)


    def set_point_per_sec(self, input_value):
        self.points_per_sec = input_value

        
    def gen_time_segment_center(self,len_pe_arr):    
        list_time_temp = []
        for i in range(1,len_pe_arr):
            value = ((i * self.segment_size - self.segment_size/2)\
                     /self.points_per_sec)
            list_time_temp.append(float(value))
            self.time = np.array(list_time_temp)

    
    def read_input_file_name(self):
        print('BEGIN: read_input_file_name',
              self.input_file_name,self.segment_size,self.embed_dimension)
        parser = argparse.ArgumentParser("Evaluation of Permutation Entropy")
        parser.add_argument("-i",help="The input file containing the \
        ECG recording.", \
                             type=str)
        parser.add_argument("-w",help="Size of the window used to \
        evaluate PeEn.", \
                             type=int)
        parser.add_argument("-d",help="Embedded dimension (nb. of used \
        values to perform ordering).", \
                             type=int)
        parser.add_argument("-e",help="Embedded separation (distance \
        between embeded points).", \
                             type=int)
        try:
            args = parser.parse_args(args=None if sys.argv[7:8] else ['--help'])
            print('input_file_name = ', args.i)
            self.input_file_name = args.i
            # print('output_file_name = ', args.o)
            # self.output_file_name = args.o
            print('segment_size = ', args.w)
            self.segment_size    = args.w
            print('embed_dimension = ', args.d)
            self.embed_dimension = args.d
            print('embed_delay = ', args.e)
            self.embed_delay = args.e
        except:
            print('Error in loading file. Run the command: \'python3 PeEn-run-XXXXXX.py -h\' for help.')
            exit(1)
        print('END: read_input_file_name') 



    def save_file_csv(self, time_array, entropy_array):
        print('BEGIN: save_file_csv')
        self.output_file_name = \
            self.save_file_name(self.save_file_suffix_csv)
        with open(self.output_file_name, mode='w') as ofile:
            print('here 1')
            try:
                print('here 2')
                write_file = csv.writer(ofile, delimiter=',', \
                                        quotechar='"', quoting=csv.QUOTE_MINIMAL )
                array_size = len(time_array)
                print('here 3: array_size = ',array_size)
                for i in range(array_size):
                    print('i = ',i)
                    print(str(time_array[i]), str(entropy_array[i])) 
                    row = [str(time_array[i]), str(entropy_array[i])]
                    write_file.writerow(row)
                print(f'Output data saved to file >> {output_file_name}') 
                print('here 4')
            except:
                print("Data were not saved.")
                print(f'Saving >> {self.output_file_name} << failed.') 
        print('END:   save_file_csv')
            

    def open_file_fill_ECG_data_arr(self):
        print('BEGIN: open_file_fill_ECG_data_arr')
        try:
            file_stats = os.stat(self.input_file_name).st_size
        except:
            print('PROGRAM TERMINATED!\n',
                  'The name of the input file <',
                  self.input_file_name,'> is incorrect.\n',
                  'Insert the valid input file.')
            exit(1)
        self.array_size = file_stats #.st_size 
        print('Number of Lines = ', self.array_size)

        with open(self.input_file_name,'r') as csvfile:
            try:
                data_file = csv.reader(csvfile, delimiter=',')
                print('data_file = ',data_file)
            except:
                print("Cannot open file '%s'." % csvfile)
                exit(1)

            list_time_temp = []
            list_ECG_temp = []
            i = 0
            for row in data_file:
                if row == []:
                    continue
                list_time_temp.append(float(row[0]))
                list_ECG_temp.append(float(row[1]))
                i += 1
            ECG_data_dim  = len(list_ECG_temp)  
            self.ECG_data      = np.empty(shape=[ECG_data_dim,2])
            self.ECG_data[:,0] = np.array(list_time_temp)
            self.ECG_data[:,1] = np.array(list_ECG_temp)
            print('*ECG_data = ',self.ECG_data[:,1]) #, 'array_size = ', self.array_size)
        print('END:   open_file_fill_ECG_data_arr')


    def scale_x(self):
        print('BEGIN:   scale_x')
        len_ECG = len(self.ECG_data[:,0])
        ECG_time_scaled = np.empty(shape=[len_ECG])
        for i in range(len_ECG):
            ECG_time_scaled[i] = \
                float(self.ECG_data[i,0]/self.points_per_sec)
        print('ECG_time_scaled = ',ECG_time_scaled) 
        print('END:     scale_x')
        return len_ECG, ECG_time_scaled


    def display_ECG_data(self):
        print('BEGIN:  display_ECG_data')
        print('data displayed here')
        len_ECG, ECG_time_scaled = self.scale_x()
        if self.display_graphs:
            plt.ion()
        else:
            plt.ioff()
        fig, ax = plt.subplots()
        ax.plot(ECG_time_scaled[:],self.ECG_data[:,1])
        ax.set_title("Full data.\nPress 'Q' or close the window to continue.")
        plt.cla()
        ax.plot(ECG_time_scaled[:self.restrict_data],
                self.ECG_data[:self.restrict_data,1])
        ax.set_title("Restricted data to %s points.\nPress 'Q' or close the window to continue." % \
                     self.restrict_data)
        if self.display_graphs:
            plt.show(block=True)
        print('END:    display_ECG_data')

        
    def slicing_arrays(self, time, data_to_display):
        
        data_size = len(time)
        print('BEGIN -> slicing_arrays')
        print('data_to_display = ', data_to_display[:])
        print('time = ', time[:])
        print('len(data_to_display) = ', len(data_to_display[:]))
        print('len(time) = ', len(time[:])) 
        print('shape time = ',(time).shape,\
              'shape data_to_display = ', (data_to_display).shape)
        set_min_y =  10e100
        set_max_y = -10e100
        set_min_x =  10e100
        set_max_x = -10e100
        for i in range(len(data_to_display)):
            if data_to_display[i] > 0:
                if set_min_y > data_to_display[i]:
                    set_min_y = data_to_display[i]
                if set_max_y < data_to_display[i]:
                    set_max_y = data_to_display[i]
                if set_min_x > time[i]:                    
                    set_min_x = time[i]
                if set_max_x < time[i]:                    
                    set_max_x = time[i]
        print('len(time) =',len(time)) 
        data_size = len(time)
        data_to_display = data_to_display[0:data_size]
        print('len(data_to_display) = ', len(data_to_display)) 
        print('len(time) =',len(time)) 
        print('END -> slicing_arrays')

        return time, data_to_display, set_min_y, set_max_y, set_min_x, set_max_x
        
    def save_file_name(self, suffix):
        file_name_sliced = \
        os.path.splitext(os.path.basename(self.input_file_name))[0]
        output_file_name = self.save_file_preffix + \
            file_name_sliced + \
            '-w' + str(self.segment_size) + '-del' + \
            str(self.embed_delay) + \
            '-dim' + str(self.embed_dimension) + \
            suffix
        return output_file_name

    
    def display_perm_entropy(self, time, data_to_display):
        print('BEGIN:  display_perm_entropy')
        time, data_to_display, set_min_y, set_max_y, set_min_x, set_max_x = \
            self.slicing_arrays(time, data_to_display)
        print('time = ',time, \
              'len(time) = ',len(time), \
              ',\n data_to_display = ', data_to_display,
              ',\n len(data_to_display) = ',
              len(data_to_display))
        print('self.display_graphs = ', self.display_graphs) 
        if self.display_graphs or self.save_PNG:
            if self.display_graphs:
                plt.ion()
            else:
                plt.ioff()
            print('in:save_PNG = ',self.save_PNG)
            self.output_file_name = \
                self.save_file_name(self.save_file_suffix_png)
            print('out:save_PNG = ',self.save_PNG)
            fig, ax = plt.subplots()
            ax.set_xlim((set_min_x * 0.99, set_max_x * 1.01))
            ax.set_ylim((set_min_y * 0.99, set_max_y * 1.01))
            ax.set_xlabel("time [sec]")
            ax.set_ylabel("potential [mV]")
            plt.title(self.output_file_name+"\nPress 'Q' or close the window to continue.")
            ax.plot(time[:],data_to_display[:])
            if self.save_PNG:
                plt.savefig(self.output_file_name)
            print('save_PNG = ',self.save_PNG) 
            if self.display_graphs:
                plt.show(block=True)
            print('END:    display_perm_entropy')


    def shannon_En(self, frequency):
        frequency = np.asarray(frequency)
        frequency = frequency[frequency > 0]
        return -np.sum(frequency * np.log2(frequency))
    

    def freq_ordinal_patterns(self, time_series, embed_dim, embed_delay):
        print('BEGIN:  freq_ordinal_patterns')
        time_series = np.asarray(time_series)
        len_time_series = len(time_series)
        number_patterns = math.factorial(embed_dim)

        all_patterns     = list(itertools.permutations(range(embed_dim)))
        print('all_patterns = ',all_patterns)
        pattern_idx = {patern: i for i, patern in enumerate(all_patterns)}
        frequency = np.zeros(number_patterns)

        print('embed_dim = ', embed_dim, 'embed_delay = ', embed_delay)
        print('len_time_series = ',len_time_series)
        print('len_time_series - (embed_dim - 1) * embed_delay = ', \
            len_time_series - (embed_dim - 1) * embed_delay)
        for i in range(len_time_series - (embed_dim - 1) * embed_delay):
            window = time_series[i:i + embed_delay * embed_dim:embed_delay]
            order = tuple(np.argsort(window))
            if i < 20:
                print(f'{embed_dim}-tuple (window) = {window}', \
                      'order = ',order)
            frequency[pattern_idx[order]] += 1
            print('frequency = ', frequency)
        sum_all = np.sum(frequency)
        print('frequency = ', frequency)
        print('END:    freq_ordinal_patterns')
        return frequency / sum_all if sum_all > 0 else frequency

    
    def perm_entropy(self, time_series, embed_dim, embed_delay):
        """
        Returns normalized permutation entropy
        """
        print('BEGIN:  perm_entropy')
        patterns = self.freq_ordinal_patterns(time_series, \
                                              embed_dim, embed_delay)
        print('perm_entropy: len(patterns) = ',len(patterns))
        max_En = np.log2(len(patterns)) if len(patterns) > 0 else 0
        print('shannon_En(patterns) = ', self.shannon_En(patterns))
        print('permutation_En = ', \
              self.shannon_En(patterns) / max_En if max_En > 0 else 0.0)
        print('END:    perm_entropy')
        return self.shannon_En(patterns) / max_En if max_En > 0 else 0.0


    def segmented_perm_entropy(self, time_series):
        print('BEGIN:  segmented_perm_entropy')
        print('len(time_series) = ',len(time_series))
        print(len(time_series),float(self.segment_size)) 
        for i in range(1,int(len(time_series)/self.segment_size)):
            print('segmented_perm_entropy :: i = ',i)
            if ((self.segment_size * i) < len(time_series)):
                time_series_segment = \
                    time_series[(self.segment_size * (i - 1)) : \
                                (self.segment_size * i)] # - 1)]
                print('self.segment_size = ',self.segment_size)
                print('self.segment_size * (i - 1)= ', \
                      self.segment_size * (i - 1), \
                      ', (self.segment_size * i) - 1  = ', \
                      (self.segment_size * i) - 1)
                print('time_series_segment = ',time_series_segment)
                pe_en = self.perm_entropy(time_series_segment,\
                                          self.embed_dimension, \
                                          self.embed_delay)
                self.time = np.append(self.time, \
                                      float(self.segment_size * i - 1)) 
                self.perm_entr_array = np.append(self.perm_entr_array, \
                                                 float(pe_en))
                print('self.time = ',self.time, \
                      'len(self.time) = ',len(self.time), \
                      ',\n self.perm_entr_array = ',self.perm_entr_array,
                      ',\n len(self.perm_entr_array) = ',
                      len(self.perm_entr_array))
                print('segmented:perm_entropy = ', (pe_en))
        print('self.perm_entr_array =  ',self.perm_entr_array, \
              'len(self.perm_entr_array =  ',len(self.perm_entr_array)) 
        print('i = ',i)
        print('END:    segmented_perm_entropy')
