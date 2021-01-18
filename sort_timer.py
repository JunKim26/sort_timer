# Author: Jun Kim
# Date:05/20/2020
# Description: A program that compares the times it takes to run two decorated sort functions


from time import perf_counter
import random
from matplotlib import pyplot
import functools


def sort_timer(func):
    """Decorator function to use in bubble and insertion sort"""


    @functools.wraps(func)
    def wrapper(*args):


        start = perf_counter()
        result = func(*args)
        end = perf_counter()

        if func.__name__ == "bubble_sort":                                      # adds wrap to bubbles or insertion depending on function name
            bubble.append((end - start))                                        # Subtracting the begin time from the end time will give you the elapsed time in seconds.
        else:
            if func.__name__ == "insertion_sort":
                insertion.append((end - start))                                 # Subtracting the begin time from the end time will give you the elapsed time in seconds.

    return wrapper




                                                                                # define function for insertion sort and decorate with sort timer
@sort_timer
def insertion_sort(a_list):
    """sorts a list using insertion sort from greatest to least"""


    for index in range (1, len(a_list)):                                        # cycles through every index in the list
        value = a_list[index]
        pos = index - 1

        while pos>= 0 and a_list[pos] < value:
            #if the value of an index is less than the value on the one to the right,
            #keep moving it's position to the right"

            a_list[pos + 1] = a_list[pos]
            pos -= 1
        a_list[pos + 1] = value


                                                                                #define function for bubble sort and decorate with sort timer
@sort_timer
def bubble_sort(a_list):
    """sorts a list using bubble sort from greatest to least"""

    comparisons = 0
    exchanges = 0

    #loop through each index of list, for each index
    for pass_num in range(len(a_list)-1):
        for index in range(len(a_list)-1-pass_num):


            if a_list[index] > a_list[index+1]:

                temp = a_list[index]
                a_list[index] = a_list[index+1]
                a_list[index+1] = temp


def  compare_sorts(bubble,insert):
    """compares how long it takes to use bubble sort and insertion sort"""

    test_list = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]


    for thousand in test_list:

        list_1 = []

        for number in range(1,thousand+1):
            list_1.append(random.randint(1, 10000))                             #generates a random number of integers matching value on test list

        list_2 = list(list_1) #makes copy of list


        bubble(list_1)
        insert(list_2)


#list to store time it took to run bubble and insertion sort
bubble = []
insertion = []
compare_sorts(bubble_sort,insertion_sort)

test_list = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]

pyplot.plot(test_list,bubble, 'ro--', linewidth=2)
pyplot.plot(test_list,insertion, 'go--', linewidth=2)
pyplot.show()
