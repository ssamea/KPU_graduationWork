import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import tkinter as tk
from tkinter import ttk
import time
import threading
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib import animation
import numpy as np
from firebase import firebase

firebase = firebase.FirebaseApplication("https://graduate-work-462b3.firebaseio.com/", None)

result = firebase.get('Distribution_DB/Kpu', None)
LARGE_FONT = ("Verdana", 12)
"""
fig = plt.figure()  # figure(도표) 생성
fig1 = plt.figure()
fig2 = plt.figure()
fig3 = plt.figure()
"""

fig = Figure(figsize=(9,6), dpi=100)
fig1 = Figure(figsize=(9,6), dpi=100)
fig2 = Figure(figsize=(9,6), dpi=100)
fig3 = Figure(figsize=(9,6), dpi=100)


ax = fig.add_subplot(111, xlim=(0, 10), ylim=(0, 15))
ax1 = fig1.add_subplot(111, xlim=(0, 10), ylim=(0, 15))
ax2 = fig2.add_subplot(111, xlim=(0, 10), ylim=(0, 15))
ax3 = fig3.add_subplot(111, xlim=(0, 10), ylim=(0, 15))


#ax = plt.subplot(111, xlim=(0, 10), ylim=(0, 15))

"""
ax.set_title('TIP')
ax1.set_title('Olive')
ax2.set_title('Sanyung')
ax3.set_title('JongHap')

ax.set_ylabel('TIP');
ax1.set_ylabel('Olive');
ax2.set_xlabel('Sanyung');
ax3.set_xlabel('JongHap');
"""

max_points = 10
max1_points = 10
max2_points = 10
max3_points = 10
"""
line, = ax.plot([], [], lw=1, c='blue', marker='d', ms=2)
line1, = ax1.plot([], [], lw=1, c='red', marker='d', ms=2)
line2, = ax2.plot([], [], lw=1, c='green', marker='d', ms=2)
line3, = ax3.plot([], [], lw=1, c='yellow', marker='d', ms=2)

line, = ax.plot(np.arange(max_points),
                np.ones(max_points, dtype=np.float) * np.nan, lw=1, c='blue', ms=1)
line1, = ax1.plot(np.arange(max1_points),
                  np.ones(max1_points, dtype=np.float) * np.nan, lw=1, c='red', ms=1)
line2, = ax2.plot(np.arange(max2_points),
                  np.ones(max2_points, dtype=np.float) * np.nan, lw=1, c='green', ms=1)
line3, = ax3.plot(np.arange(max3_points),
                  np.ones(max3_points, dtype=np.float) * np.nan, lw=1, c='yellow', ms=1)
"""

line, = ax.plot([], [], lw=1, c='blue', marker='d', ms=2)
line1, = ax1.plot([], [], lw=1, c='red', marker='d', ms=2)
line2, = ax2.plot([], [], lw=1, c='green', marker='d', ms=2)
line3, = ax3.plot([], [], lw=1, c='yellow', marker='d', ms=2)

line, = ax.plot(np.arange(max_points),
                np.ones(max_points, dtype=np.float) * np.nan, lw=1, c='blue', ms=1)
line1, = ax1.plot(np.arange(max1_points),
                  np.ones(max1_points, dtype=np.float) * np.nan, lw=1, c='red', ms=1)
line2, = ax2.plot(np.arange(max2_points),
                  np.ones(max2_points, dtype=np.float) * np.nan, lw=1, c='green', ms=1)
line3, = ax3.plot(np.arange(max3_points),
                  np.ones(max3_points, dtype=np.float) * np.nan, lw=1, c='yellow', ms=1)

def init():
    return line
def init1():
    return line1
def init2():
    return line2
def init3():
    return line3

def animate(i):

    y = firebase.get('Distribution_DB/TIP/people_number', None)
    old_y = line.get_ydata()
    new_y = np.r_[old_y[1:], y]
    line.set_ydata(new_y)
    return line
def animate1(i):
    y1 = firebase.get('Distribution_DB/Olive/people_number', None)
    old_y1 = line1.get_ydata()
    new_y1 = np.r_[old_y1[1:], y1]
    line1.set_ydata(new_y1)
    return line1

def animate2(i):
    y2 = firebase.get('Distribution_DB/Sanyung/people_number', None)
    old_y2 = line2.get_ydata()
    new_y2 = np.r_[old_y2[1:], y2]
    line2.set_ydata(new_y2)
    return line2
def animate3(i):
    y3 = firebase.get('Distribution_DB/JongHap/people_number', None)
    old_y3 = line3.get_ydata()
    new_y3 = np.r_[old_y3[1:], y3]
    line3.set_ydata(new_y3)
    return line3

"""
class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)


    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
"""



class Realtime(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Estimation System")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        """
        frame = StartPage(container, self)
        frame1_ = PageOne(container, self)
        frame2_ = PageTwo(container, self)
        frame3_ = PageThree(container, self)

        self.frames[StartPage] = frame
        self.frames[PageOne] = frame1_
        self.frames[PageTwo] = frame2_
        self.frames[PageThree] = frame3_

        frame.grid(row=0, column=0, sticky="nsew")
        frame1_.grid(row=0, column=0, sticky="nsew")
        frame2_.grid(row=0, column=0, sticky="nsew")
        frame3_.grid(row=0, column=0, sticky="nsew")
        """


        for F in (StartPage, PageOne, PageTwo, PageThree):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=("Sanyung"), font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        button1 = ttk.Button(self, text="TIP",
                             command=lambda: controller.show_frame(PageThree))
        button1.pack(side='left')

        button2 = ttk.Button(self, text="JongHap",
                             command=lambda :controller.show_frame(PageOne))
        button2.pack(side='right')

        canvas = FigureCanvasTkAgg(fig, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
      #  canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.canvas = canvas

        """
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        """

        """
        def animate(i):
            y2 = firebase.get('Distribution_DB/Sanyung/people_number', None)
            old_y2 = line2.get_ydata()
            new_y2 = np.r_[old_y2[1:], y2]
            line2.set_ydata(new_y2)
            return line

        self.anim = animation.FuncAnimation(fig, animate, init_func=init, frames=50, interval=200, blit=False)
        """
"""
class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Sanyung", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)

        tk.Button(self, text="JongHap",
                            command=lambda: master.switch_frame(PageOne)).pack(side='right')

        canvas = FigureCanvasTkAgg(fig, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        def animate(i):
            y2 = firebase.get('Distribution_DB/Sanyung/people_number', None)
            old_y2 = line2.get_ydata()
            new_y2 = np.r_[old_y2[1:], y2]
            line2.set_ydata(new_y2)
            return line

        self.anim = animation.FuncAnimation(fig, animate, init_func=init, frames=50, interval=200, blit=False)
"""
class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=("JongHap"), font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Sanyung",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack(side='left')

        button2 = ttk.Button(self, text="Olive",
                             command=lambda :controller.show_frame(PageTwo))
        button2.pack(side='right')

        canvas1 = FigureCanvasTkAgg(fig1, self)
        canvas1.draw()
        canvas1.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
      #  canvas1._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.canvas = canvas1

        """
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        """

        """
        def animate1(i):
            y3 = firebase.get('Distribution_DB/JongHap/people_number', None)
            old_y3 = line3.get_ydata()
            new_y3 = np.r_[old_y3[1:], y3]
            line3.set_ydata(new_y3)
            return line3

        #self.anim1 = animation.FuncAnimation(fig1, animate1, init_func=init1, frames=50, interval=200, blit=False)
        """
"""

class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='blue')
        tk.Label(self, text="JongHap", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Sanyung",
                            command=lambda: master.switch_frame(StartPage)).pack(side='left')

        tk.Button(self, text="Olive",
                            command=lambda: master.switch_frame(PageTwo)).pack(side='right')

        canvas = FigureCanvasTkAgg(fig1, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        def animate1(i):
            y3 = firebase.get('Distribution_DB/JongHap/people_number', None)
            old_y3 = line3.get_ydata()
            new_y3 = np.r_[old_y3[1:], y3]
            line3.set_ydata(new_y3)
            return line3

        self.anim1 = animation.FuncAnimation(fig1, animate1, init_func=init1, frames=50, interval=200, blit=False)

"""
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=("Olive"), font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="JongHap",
                             command=lambda: controller.show_frame(PageOne))
        button1.pack(side='left')

        button2 = ttk.Button(self, text="Tip",
                             command=lambda: controller.show_frame(PageThree))
        button2.pack(side='right')

        canvas2 = FigureCanvasTkAgg(fig2, self)
        canvas2.draw()
        canvas2.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
       # canvas2._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.canvas = canvas2

        """
        toolbar = NavigationToolbar2Tk(canvas2, self)
        toolbar.update()
        """
        """
        def animate2(i):
            y1 = firebase.get('Distribution_DB/Olive/people_number', None)
            old_y1 = line1.get_ydata()
            new_y1 = np.r_[old_y1[1:], y1]
            line1.set_ydata(new_y1)
            return line1
        
        self.anim2 = animation.FuncAnimation(fig2, animate2, init_func=init2, frames=50, interval=200, blit=False)
        """
"""
class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='red')
        tk.Label(self, text="Olive", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="JongHap",
                            command=lambda: master.switch_frame(PageOne)).pack(side='left')
        #button1.pack(side='left')
        tk.Button(self, text="TIP",
                  command=lambda: master.switch_frame(PageThree)).pack(side='right')

        canvas = FigureCanvasTkAgg(fig2, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        def animate2(i):
            y1 = firebase.get('Distribution_DB/Olive/people_number', None)
            old_y1 = line1.get_ydata()
            new_y1 = np.r_[old_y1[1:], y1]
            line1.set_ydata(new_y1)
            return line1

        self.anim2 = animation.FuncAnimation(fig2, animate2, init_func=init2, frames=50, interval=200, blit=False)

"""
class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=("Tip"), font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Olive",
                             command=lambda: controller.show_frame(PageTwo))
        button1.pack(side='left')

        button2 = ttk.Button(self, text="Sanyung",
                             command=lambda: controller.show_frame(StartPage))
        button2.pack(side='right')

        canvas3 = FigureCanvasTkAgg(fig3, self)
        canvas3.draw()
        canvas3.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
      #  canvas3._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.canvas = canvas3
        """
        toolbar = NavigationToolbar2Tk(canvas3, self)
        toolbar.update()
        """
        """
        def animate3(i):
            y = firebase.get('Distribution_DB/TIP/people_number', None)
            old_y = line.get_ydata()
            new_y = np.r_[old_y[1:], y]
            line.set_ydata(new_y)
            return line
        
        self.anim3 = animation.FuncAnimation(fig3, animate3, init_func=init3, frames=50, interval=200, blit=False)
        """
"""
class PageThree(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='pink')
        tk.Label(self, text="TIP", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Olive",
                            command=lambda: master.switch_frame(PageTwo)).pack(side='left')
        #button1.pack(side='left')

        canvas = FigureCanvasTkAgg(fig3, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        def animate3(i):
            y = firebase.get('Distribution_DB/TIP/people_number', None)
            old_y = line.get_ydata()
            new_y = np.r_[old_y[1:], y]
            line.set_ydata(new_y)
            return line

        self.anim3 = animation.FuncAnimation(fig3, animate3, init_func=init3, frames=50, interval=200, blit=False)
"""

app = Realtime()
#app = SampleApp()
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=50, interval=200, blit=False)
anim1 = animation.FuncAnimation(fig1, animate1, init_func=init1, frames=50, interval=200, blit=False)
anim2 = animation.FuncAnimation(fig2, animate2, init_func=init2, frames=50, interval=200, blit=False)
anim3 = animation.FuncAnimation(fig3, animate3, init_func=init3, frames=50, interval=200, blit=False)

app.mainloop()
