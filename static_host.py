import os
import threading
from config import CONFIG
from ssh_tunnel import start_tunnel
from git_manager import update_redirect_address


server_thread = threading.Thread(target=os.system, args=("server.py 1",)).start()
URL = start_tunnel(PORT=CONFIG["PORT"])
update_redirect_address(URL)