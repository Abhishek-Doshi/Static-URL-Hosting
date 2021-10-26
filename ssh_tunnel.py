from pyngrok import ngrok
from config import CONFIG

def get_active_tunnels():
    active_tunnels = []
    for tunnel in ngrok.get_tunnels():
        active_tunnels.append(tunnel.data['public_url'])
    return active_tunnels

def start_tunnel(PORT=CONFIG["PORT"]):
    ssh_tunnel = ngrok.connect(PORT, bind_tls=True)
    return ssh_tunnel.data['public_url']