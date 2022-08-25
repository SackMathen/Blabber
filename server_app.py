# file is complete for starting and stopping the server. need to add buttons for dark mode and voice.
# could also do something for commands. well look into it later.
import tkinter as tk
import socket
import threading

# start of the server GUI

window = tk.Tk()
window.title("Sever")

# Top frame consisting of two buttons widgets (i.e. btnStart, btnStop)
topFrame = tk.Frame(window)
btnStart = tk.Button(topFrame, text="Connect", command=lambda: start_server())
btnStart.pack(side=tk.LEFT)
btnStop = tk.Button(topFrame, text="Stop", command=lambda: stop_server(), state=tk.DISABLED)
btnStop.pack(side=tk.LEFT)
topFrame.pack(side=tk.TOP, pady=(5, 0))

# Middle frame consisting of two labels for displaying the host and port info
middleFrame = tk.Frame(window)
lblHost = tk.Label(middleFrame, text="Host: X.X.X.X")
lblHost.pack(side=tk.LEFT)
lblPort = tk.Label(middleFrame, text="Port:XXXX")
lblPort.pack(side=tk.LEFT)
middleFrame.pack(side=tk.TOP, pady=(5, 0))

# The client frame shows the client area
clientFrame = tk.Frame(window)
lblLine = tk.Label(clientFrame, text="*******************CLIENT LIST*****************").pack()
scrollBar = tk.Scrollbar(clientFrame)
scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
tkDisplay = tk.Text(clientFrame, height=15, width=40)
tkDisplay.pack(side=tk.LEFT, fill=tk.Y, padx=(5, 0))
# Insert demo connected user names
tkDisplay.insert(tk.END, "User 1\n")
tkDisplay.insert(tk.END, "User 2\n")
tkDisplay.insert(tk.END, "User 3\n")
tkDisplay.insert(tk.END, "User 4\n")
tkDisplay.insert(tk.END, "User 5\n")
tkDisplay.insert(tk.END, "User 6\n")
tkDisplay.insert(tk.END, "User 7\n")
tkDisplay.insert(tk.END, "User 8\n")
scrollBar.config(command=tkDisplay.yview)
tkDisplay.config(yscrollcommand=scrollBar.set, background="#F4F6F7", highlightbackground="grey", state="disabled")
clientFrame.pack(side=tk.BOTTOM, pady=(5, 10))


def start_server():
    btnStart.config(state=tk.DISABLED)
    btnStop.config(state=tk.NORMAL)


def stop_server():
    btnStart.config(state=tk.NORMAL)
    btnStop.config(state=tk.DISABLED)

# end of server GUI

window.mainloop()


# beginning of the server backend.
server = None
HOST_ADDR = "0.0.0.0"
HOST_PORT = 8080
client_name = " "
clients = []
clients_names = []


# Start server function
def start_server():
    global server, HOST_ADDR, HOST_PORT # code is fine without this
    btnStart.config(state=tk.DISABLED)
    btnStop.config(state=tk.NORMAL)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST_ADDR, HOST_PORT))
    server.listen(5)  # server is listening for client connection

    threading._start_new_thread(accept_clients, (server, " "))

    lblHost["text"] = "Host: " + HOST_ADDR
    lblPort["text"] = "Port: " + str(HOST_PORT)

# end of start server function
