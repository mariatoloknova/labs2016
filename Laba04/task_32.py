#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():
    i = 0
    while (wall_is_on_the_right() != True):
        if (wall_is_beneath() and wall_is_above()):
            if cell_is_filled():
                i += 1
            else:
                fill_cell()
        if (wall_is_above() != True):
            while (wall_is_above() != True):
                move_up()
                if cell_is_filled():
                    i += 1
                else:
                    fill_cell()
            while (wall_is_beneath() != True):
                move_down()
        move_right()
    mov("ax", i)


if __name__ == '__main__':
    run_tasks()