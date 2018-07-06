
#baekjoon problem 2333

def ins_sort(inp_arr, i, j):
    for k in range(j): 
        curr_val = inp_arr[k]
        pos = k

        while pos > 0 and inp_arr[pos - 1][0] > curr_val[0]:
            inp_arr[pos] = inp_arr[pos - 1]
            pos = pos-1

        inp_arr[pos] = curr_val

    return inp_arr 


if __name__ == '__main__':

    health = 10
    box_h = 0
    survived_t = 0
    box_height_sum = 0
    box_food_sum = 0
    kswitch = 0
    
    temp = input()
    trap_h, box_n = temp.split()
    trap_h, box_n = int(trap_h), int(box_n)

    box_attr = [[0 for x in range(3)] for y in range(box_n)]
    
    for k in range(box_n):
        temp = input()
        box_attr[k][0], box_attr[k][1], box_attr[k][2] = temp.split()
        box_attr[k][0], box_attr[k][1], box_attr[k][2] = int(box_attr[k][0]), int(box_attr[k][1]), int(box_attr[k][2])  
       
        box_height_sum += box_attr[k][2]
        box_food_sum += box_attr[k][1]

    box_attr = ins_sort(box_attr, 3, box_n)

    # when first box comes after 10 t
    if box_attr[0][0] > health:
        survived_t = health
        print(survived_t)
    # if the sum of all boxes are < trap_h
    elif box_height_sum < trap_h:
        survived_t = box_food_sum + health
        print(survive)
    else:
        health -= box_attr[0][0]
        survive = box_attr[0][0]

        for iterator in range(box_n-1):
            if health >= 0:
                #diff between 2 timesteps
                time_diff = box_attr[iterator+1][0] - box_attr[iterator][0]

                # if we cannot survive without eating
                if time_diff > health: 
                    health += box_attr[iterator][1]
                    survived_t += box_attr[iterator][1]
                # stack box
                else:
                    box_h += box_attr[iterator][2]

                survived_t += time_diff
                health -= time_diff

            if box_h >= trap_h:
                print(box_attr[iterator][0])
                kswitch = 1

        if kswitch == 0:
            time_diff = box_attr[box_n-1][0] - box_attr[box_n-2][0]
            if time_diff - health < 0:
                survived_t += box_attr[box_n-1][1]
                print(survived_t)
            else:
                box_h += box_attr[box_n-1][2]
                if box_h >= trap_h:
                    print(box_attr[box_n-1][0])







    





