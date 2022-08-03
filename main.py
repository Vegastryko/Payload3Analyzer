import csv


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    tags_list=[]
    weight_frame_list = []

    valid_tags_occurence = 0
    left_arm_tag_occurence=0
    right_arm_tag_occurence = 0

    zero_weights_left = 0
    zero_weights_right = 0
    zero_weights_occurence = 0
    weights_occurence = 0
    weights_frame_duplicity = 0;

    with open('payload3_example.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        reading_line = 0

        for row in csv_reader:
            if reading_line == 0:
                reading_line += 1
            else:
                if row['Ant'] == '3' or row['Ant'] == '4':               #event z anten 3 4

                    if row['TagID'] == '300003000016000000000000':    #left arm tag
                        left_arm_tag_occurence += 1
                    elif row['TagID'] == '300003000015000000000000':    #right arm tag
                        right_arm_tag_occurence += 1
                    elif '00000000000020000' in str(row['TagID']):               #valid RFID
                        if row['TagID'] not in tags_list:          #deduplikacia existujucich tagov
                            tags_list.append(row['TagID'])
                            valid_tags_occurence += 1
                    else:
                        print("Podozrivy Tag " + str(row['TagID']))


                if row['Ant']=='11' or row['Ant']=='12':                  #event z digisense 11-lavo 12 vpravo
                    weight = int("0x"+str(row['TagID'])[0:2], 16)
                    frame_number = int("0x" + str(row['TagID'])[11:], 16)

                    if (frame_number not in weight_frame_list):
                        weight_frame_list.append(frame_number)
                        if weight <= 0:
                            if row['Ant']=='11':
                                zero_weights_left += 1
                            else:
                                zero_weights_right += 1
                            zero_weights_occurence +=1
                        else:
                            weights_occurence += 1
                    else:
                        weights_frame_duplicity += 1
                        print(row)


                reading_line += 1

        print("Valid BIN tags         " + str(valid_tags_occurence))
        print("Valid Non-zero weights " + str(weights_occurence))

        print("Left arm Tag  " + str(left_arm_tag_occurence))
        print("Right arm Tag " + str(right_arm_tag_occurence))

        print("Zero weights  " + str(zero_weights_occurence))
        print("Zero weightsL " + str(zero_weights_left))
        print("Zero weightsR " + str(zero_weights_right))

        print("Weight frame duplicity  " + str(weights_frame_duplicity))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

