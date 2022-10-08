import os, discord, time
import asyncio
 
import websockets
abo = None

async def echo(websocket, send = False):
    abo = websocket
    if send:
        async for message in websocket:
            await websocket.send(message)
    else:
        async for message in websocket:
            print(message)


async def main():
    async with websockets.serve(echo, "localhost", 6789):
        await asyncio.Future()  # run forever



client = discord.Client(command_prefix = "!", intents=discord.Intents.all())
__TOKEN = "MTAxMjM0MDM2MDQ1MTcyNzM2MA.G8Zt__.2n_6150ffgi9VS_H9CUjeqEt9wY56kZlGJe-qY"

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    print(message.content)
    args = message.content.split(" ")
    print(args)
    if args[0] == "here":
        handler.channel = message.channel
        print(message.channel)
        channel = message.channel
        await message.channel.send("This channel has been designated to display messages from the websocket.")
   
    echo(abo, True)
    pass

# client.run(__TOKEN)


async def on_register(identifier):
    global channel
    if channel != None:
        await channel.send(identifier+" just connected.")
    pass

async def on_unregister(identifier):
    global channel
    if channel != None:
        await channel.send(identifier+" closed connection with the websocket.")






# bot = interactions.Client(token="MTAxMjM0MDM2MDQ1MTcyNzM2MA.G8Zt__.2n_6150ffgi9VS_H9CUjeqEt9wY56kZlGJe-qY")


# slash = SlashCommand(client, sync_commands=True)
# bot.start()


@client.event
async def on_message(message):
    print(message.content)
    global channel
    if message.content[0] != "!": return
    print('hehe')
    args = message.content[1:].split(" ")
    if args[0] == "here":
        handler.channel = message.channel
        channel = message.channel
        await message.channel.send("This channel has been designated to display messages from the websocket.")
    if len(args) > 0:
        print(handler.all_triggers)
        for v in handler.all_triggers:
            print('asdf')
            if v[0] == args[0]:
                print('dsaf')
                print("passing "+"trigger/"+v[0]+"/"+" ".join(args[1:]))
                await v[2].send("trigger/"+v[0]+"/"+" ".join(args[1:]))
                print('sent!')
    pass

asyncio.run(main())