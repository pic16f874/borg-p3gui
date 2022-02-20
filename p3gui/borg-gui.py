#!/usr/bin/python3
#from curses import wrapper
import time
import curses

def main(stdscr):
    # Clear screen
    stdscr.clear()

    curses.cur_set(0)

    text = "hello"
    h, w = stdscr.getmaxyx()
    x = w//2 - len(text)//2
    y = h//2
    stdscr.addstr(y, x, text)



    begin_x = 2; begin_y = 2; height = 5; width = 40;
    
#    win = curses.newwin(height, width, begin_y, begin_x)

    # This raises ZeroDivisionError when i == 10.
#    for i in range(0, 10):
#        v = i-10
#        stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10/v))

    stdscr.refresh()
    stdscr.getkey()

#wrapper(main)
curses.wrapper(main)
