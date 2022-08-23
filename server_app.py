import tkinter as tk
window = tk.Tk()
window.title("SERVER")

# top frame has two buttons to start and stop the server side.
topFrame = tk.Frame(window)
btnStart = tk.Button(topFrame, text="CONNECT", command=lambda : start_server())
btnStart.pack(side=tk.LEFT)
btnStop = tk.Button(topFrame, text="DISCONNECT", command=lambda : stop_server(), state=tk.DISABLED)
btnStop.pack(side=tk.LEFT)
topFrame.pack(side=tk.TOP, pady=(5, 0))

#middle frame for showing host and port info
middleFrame =
