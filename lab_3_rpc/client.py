import xmlrpc.client

with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
    print("Current time on the server: %s" % proxy.get_current_time())