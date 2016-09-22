#!/usr/bin/python3

from pyrob.api import *

def find_exit():
    while(wall_is_on_the_left() != True):
        move_left()
        if wall_is_beneath() == False:
            break
    if wall_is_beneath():
        while(wall_is_on_the_right() != True):
            move_right()
            if wall_is_beneath() == False:
                break

@task(delay=0.01)
def task_8_30():
    find_exit()
    while(wall_is_beneath() == False):
        while(wall_is_beneath() == False):
            move_down()
        find_exit()
    while(wall_is_on_the_left() != True):
        move_left()


if __name__ == '__main__':
    run_tasks()