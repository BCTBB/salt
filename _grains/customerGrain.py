# add a Customer grain such that the value is the hostname, on minion check-in
def customerName():
    import socket
    hostname = socket.gethostname().lower()
    return {'Customer': str(hostname)}