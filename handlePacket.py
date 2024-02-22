# coding=utf-8

import urllib2


class handlePacket():
    DEFAULT_PACKET = "__dd__"

    def __init__(self):
        self.url = "http://192.168.43.194/ape/?sockid=1"
        self.key = "ùaCmphx0e9xZq1xSvxTQE2g==22lmlhnOr4C9Ozq4X4sfZVyFLr0RyVvW1aZE568Bo8r/tDnx4JXpMWJqQ/zH7eE0vy33rJJAlWrTO4ZvGG2ahXOaQLFf+p0vkVSNx7FDpJP6weu+QG289tjLFX/fZf/ClR+DaPGYQqaqCnEHdfNBIxiyQjdwqInkgXv9WfW1DZvHqFsn9RWPGr2N6O1RHgghp2ylIMhWR++lAXR+0dl2a/qSWiLsmczGPJ8qRHuHzL7v1aIku//wokHBkOaKBGxvdITGjPN7HbrYFQtkJgQKfg=="
        

    def send(self, data, server):
        post_data = (str(data))
        req = urllib2.Request(self.url, post_data)
        response = urllib2.urlopen(req)
        responseMsg = response.read()
        # self._handleEditPacket(responseMsg, server, post_data[-1])
        
        # Test
        if  "cC-?" in post_data:
            responseMsg = "ùBM%|perro|"
            self._handleEditPacket(responseMsg, server, post_data[-1])

        return response.read()
    
    def _handleEditPacket(self, responseMsg, server, endCharacter):
        if self.DEFAULT_PACKET in responseMsg:
            return
        responseMsg = self.key + responseMsg + endCharacter
        print "ENVIO-SERVER [{}] -> {}".format(1, responseMsg)
        server.sendall(responseMsg)
