
def parse(data, port, origin):
    if port==80:
        return
    if origin == 'server':
        return
    print "[{}({})] {}".format(origin, port, data.encode('hex'))