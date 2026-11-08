import asyncio

class NodeServer(asyncio.Protocol):
    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data):
        message = data.decode()
        print('Data received: {!r}'.format(message))

        tra_dat = str(input("retransmit: ")).encode("ascii")

        print('Send: {!r}'.format(tra_dat))
        self.transport.write(tra_dat)

        print('Close the client socket')
        self.transport.close()