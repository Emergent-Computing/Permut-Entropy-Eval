import numpy as np
from PeEn_evaluation import PeEn



# run examples: 
# python3 PeEn-run-20260131.py -i ./False-ECG-sinus.csv -w 500 -d 3 -e 1
# python3 PeEn-run-20260131.py -i ./False-ECG-modul-sinus.csv -w 500 -d 3 -e 1
# python3 PeEn-run-20260131.py -i ./False-ECG-jumps.csv -w 500 -d 3 -e 1
# python3 PeEn-run-20260131.py -i ./False-Lorenz-attractor.csv -w 500 -d 3 -e 1

# ********************************************************************** #
# ********************************************************************** #
#                                                                        #
save_PNG = 1          ## 1 = YES & 0 = NO
#                                                                        #
display_graphs = 1    ## 1 = YES & 0 = NO
#                                                                        #
#                                                                        #
# ********************************************************************** #
# ********************************************************************** #



def main():
    print("PeEn program initiated.")
    #time_start()
    #global perm_entr_array, time
    #pe = PeEn
    ##
    ## pe = PeEn(points_per_sec, segment_size, embed_delay,
    ##          embed_dimension)
    pe = PeEn()
    pe.save_PNG       = save_PNG
    pe.display_graphs = display_graphs
    pe.hello()
    # pe.set_point_per_sec(2000)
    pe.time_start()
    pe.read_input_file_name()
    pe.open_file_fill_ECG_data_arr()
    if display_graphs: 
        pe.display_ECG_data()
    print('ECG_data[:,1] = ',pe.ECG_data[:,1])
    pe.segmented_perm_entropy(pe.ECG_data[:,1])
    len_pe_arr = int(len(pe.ECG_data[:,1])/pe.segment_size)
    pe.time =np.empty(shape=[0]) #len_pe_arr])
    print('len(pe.perm_entr_array) = ',len_pe_arr)
    pe.gen_time_segment_center(len_pe_arr)
    print('main: time = ', pe.time, 'type(pe.time) = ', type(pe.time)) #; exit(1)
    print('main:perm_entr_array = ',pe.perm_entr_array) #; exit(1)
    pe.display_perm_entropy(pe.time, \
                            pe.perm_entr_array) #; exit(1)
    # Evaluate PeEn
    perm_entr = pe.perm_entropy(pe.ECG_data[:,1], embed_dim=pe.embed_dimension, embed_delay=pe.embed_delay)
    pe.save_file_csv(pe.time,pe.perm_entr_array)
    print('perm_entr_array = ',pe.perm_entr_array)
    print('perm_entr = ',perm_entr)
    print("PeEn program finalized with: ")
    print(f'input_file_name = {pe.input_file_name}\nsegment_size = {pe.segment_size}\nembed_dimension = {pe.embed_dimension}')
    print(f'output_file_name = {pe.output_file_name}')
    pe.time_end()
    time_total = pe.time_total()
    print(f'time_total = {time_total} [s]')
    #print(f'>>> pe.start_time = {pe.start_time}')
    #print(f'pe.end_time = {pe.end_time}')
  
if __name__=='__main__':
    main()
