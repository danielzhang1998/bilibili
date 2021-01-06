import pickle, os
import easygui as g
import get_total_time as data

LOCATION = os.getcwd() + '/html_css_js_flask/learning_progress_count/'

url = input('enter\n')

# 18 is minutes and 00 is seconds
# add in more time list or edit if need
my_time = []
my_time = data.get_durations(url)

# make a new binary file to store the data in list my_time
def add_data_set(my_time):
    # auto create a new file if it not exists, or write into the file directly if the file exists
    pickle_file = open(LOCATION + 'html_learn_progress.testing','wb')   # wb is write binary, do not mind the file name, it can be anything
    pickle.dump(my_time,pickle_file)    # dump the list into the file
    pickle_file.close()

def data_set_read():
    if __name__ != '__main__':
        add_data_set(my_time)
    pickle_file = open(LOCATION + 'html_learn_progress.testing','rb')   # rb is read binary
    my_list2 = pickle.load(pickle_file) # load the binary data
    if __name__ == '__main__':
        print(my_list2) # show the data
    length_data_set = len(my_list2)
    g.msgbox(msg = 'data set insert successful :)' + '\n\n' + 'total insert: ' + str(length_data_set),title='System Warning',ok_button='Get it !')
    return my_list2

if __name__ == '__main__':
    add_data_set(my_time)
    data_set_read()