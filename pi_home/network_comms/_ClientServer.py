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


async def Node(address, port):
    # Get a reference to the event loop as we plan to use
    # low-level APIs.
    loop = asyncio.get_running_loop()

    server = await loop.create_server(
        NodeServer,
        address, port)

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(Node())
