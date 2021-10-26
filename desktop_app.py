import webview
import threading, os, time

def destroy(window):
    time.sleep(3)
    window.destroy()

server_thread = threading.Thread(target=os.system, args=("static_host.py 1",)).start()
window = webview.create_window('Loading Screen', 'Loading', frameless=True, width=600, height=320)
webview.start(destroy, window)

webview.create_window('Desktop App', 'http://127.0.0.1:5000/', width=1200, height=600)
webview.start()