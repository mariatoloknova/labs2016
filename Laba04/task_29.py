#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    i =0
    while(i != 3 and wall_is_on_the_right() != True):
        move_right()
        i=0
        if cell_is_filled() and wall_is_on_the_right() != True:
            move_right()
            i += 1
            if cell_is_filled() and wall_is_on_the_right()!= True:
                move_right()
                i += 1
                if cell_is_filled() and wall_is_on_the_right() != True:
                    i += 1


if __name__ == '__main__':
    run_tasks()