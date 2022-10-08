from structs import discord, websocket
import asyncio

__TOKEN = "MTAxMjM0MDM2MDQ1MTcyNzM2MA.G8Zt__.2n_6150ffgi9VS_H9CUjeqEt9wY56kZlGJe-qY"


websocket.init()

asyncio.get_event_loop().create_task(discord.client.start(__TOKEN))
asyncio.get_event_loop().run_forever()