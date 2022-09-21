
import tkinter as tk
from idlelib.tooltip import Hovertip
import threading
import time
import functools


class TKDotPackSimulator(threading.Thread):

    def __init__(self, pixel_width=20):
        w, h = 16,16
        # 2维列表
        self.matrix = [[0 for x in range(w)] for y in range(h)] 
        self.pixel_width = pixel_width 
        threading.Thread.__init__(self)
        self.start()

    def quit(self):
        self.root.quit()

    def mouse_enter(self,event,coordinates):
      print("Enter:", coordinates)
      
    def mouse_leave(self, event, coordinates):
      print("Leave:", coordinates)

    def create_pixels(self):
      for i in range(16):
        for j in range(16):
            frame = tk.Frame(
                master=self.root,
                width=self.pixel_width, 
                height=self.pixel_width,
                bg="black", # background='#000000' hex
                borderwidth=1,
                relief = tk.RAISED,
                # highlightcolor="red",
            )
            self.matrix[i][j] = frame
            frame.grid(row=i, column=j)
            # 闭包，绑定参数
          
            Hovertip(frame,f'{i},{j}')
            '''
            mouse_enter = functools.partial(self.mouse_enter, coordinates=(i,j))
            frame.bind('<Enter>', mouse_enter)
            mouse_leave = functools.partial(self.mouse_leave, coordinates=(i,j))
            frame.bind('<Leave>', mouse_leave)
            '''

    def set_pixel(self,x,y,color):
        self.matrix[x][y].config(bg = color)
    
    def clear(self):
        for i in range(16):
            for j in range(16):
                self.matrix[i][j].config(bg = 'black')

    def run(self):
        self.root = tk.Tk()
        self.root.title('DotPack Simulator')
        self.root.protocol("WM_DELETE_WINDOW", self.quit)
        self.create_pixels()
        self.root.mainloop()
