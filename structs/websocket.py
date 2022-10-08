import asyncio, websockets
# from structs import discord, handler

connections = {}

async def on_register(websocket, identifier):
    if connections.get(identifier) == None:
        print("Registered "+identifier)
        connections[identifier] = [websocket,{}]
        # await discord.on_register(identifier)

async def on_unregister(identifier, *err):
    if connections.get(identifier):
        print("Unregistered "+identifier)
        # await discord.on_unregister(identifier)
        print(identifier, connections[identifier])
        # await handler.on_unregister(identifier, connections[identifier])
        del connections[identifier]
    if err:
        print(err)

async def connect(websocket, path):
    identifier = await websocket.recv()
    await on_register(websocket, identifier)
    try:
        async for message in websocket:
            await websocket.send(message)
            print(identifier, connections[identifier], message)
            for i in connections[identifier]:
                print(i)
                print("f")
            # connections[identifier][2].send("trigger/"+v[0]+"/"+" ".join())
            # await handler.on_message_received(identifier, connections[identifier], message)
    except Exception as e:
        print(e)
        await on_unregister(identifier, f"{e.args}") 
    finally:
        await on_unregister(identifier)
    pass

def init():
    print("alive")
    server = websockets.serve(connect, "localhost", 6789)
    asyncio.get_event_loop().run_until_complete(server)
    print("Websocket alive")

init()
#loop forever init() using asyncio 
asyncio.get_event_loop().run_forever()
