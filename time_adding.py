import pickle
import easygui as g
import get_data_set as data_set

sum_second = 0  # time already used, initial be zero



# calculate the progress
def calculate(my_list2):
    global sum_second
    total_time = 0
    for each in range(len(my_list2)):
        total_time += 60 * int(my_list2[each][0]) + int(my_list2[each][1])
        if each < already_take:
            sum_second += 60 * int(my_list2[each][0]) + int(my_list2[each][1])
    string1 = "hours already take: " + str(sum_second/(60*60)) +' / ' + str(total_time/(60*60))
    string2 = "current percentage: " + str((sum_second/total_time) * 100) + ' %'
    #g.msgbox(msg = string1 + '\n\n' + string2,title='System Warning',ok_button='Get it !')
    g.msgbox(msg = string1 + '\n\n' + string2,title='System Warning',ok_button='Get it !')


if __name__ == "__main__":
    already_take = input('how many unit you already take up to now?\n')
    try:
        already_take = int(already_take)
    except ValueError:
        g.msgbox(msg = 'seems enter is wrong, please check it and enter again!', title='System Warning',ok_button='Get it !')
        exit()
    my_list2 = data_set.data_set_read()
    calculate(my_list2)