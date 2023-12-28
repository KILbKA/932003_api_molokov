from xmlrpc.server import SimpleXMLRPCServer

def get_current_time():
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_function(get_current_time, "get_current_time")
server.serve_forever()