import discord as dc
import random as rd
import threading as tr
import names
import time
import random
import generate

link = 'https://discordapp.com/oauth2/authorize?client_id=574756002822488078&scope=bot&permissions=202578944'
token = 'NTc0NzU2MDAyODIyNDg4MDc4.XM-C5g.825vPHCeWahmL-ejbFaG04xzH-Y'
error_msg = "Oof."


class MyClient(dc.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        self.a = generate.Board()

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content.startswith('!Behold!'):
            await message.channel.send("{} name is {}.".format(random.choice(['His', 'Her']), names.name_gen(1)[0]))
        elif message.content.lower().startswith('!list a city'):
            await message.channel.send(names.name_dump(100))
        elif message.content.lower().startswith('!new map plz'):
            self.a.generate()
        elif message.content.lower().startswith('!show me the'):
            try:
                if message.content.lower().endswith('mountains'):
                    await message.channel.send(self.a.output('ele'))
                elif message.content.lower().endswith('climate'):
                    await message.channel.send(self.a.output('hot'))
                elif message.content.lower().endswith('ecosystems'):
                    await message.channel.send(self.a.output('bio'))
                elif message.content.lower().endswith('fertility'):
                    await message.channel.send(self.a.output('fer'))
            except:
                await message.channel.send(error_msg + "It would appear there is no map.  We gotcha covered.")
                if not self.a.lock:
                    tr.Thread(target=self.a.generate).start()

                while self.a.lock:
                    pass

                if message.content.lower().endswith('mountains'):
                    await message.channel.send(self.a.output('ele'))
                elif message.content.lower().endswith('climate'):
                    await message.channel.send(self.a.output('hot'))
                elif message.content.lower().endswith('ecosystems'):
                    await message.channel.send(self.a.output('bio'))
                elif message.content.lower().endswith('fertility'):
                    await message.channel.send(self.a.output('fer'))
        elif message.content.lower().startswith('!help'):
            await message.channel.send("THINGS YOU CAN SAY:\n-Show me the (mountains/climate/ecosystems/fertility)\n"
                                       "-Behold!\n-List a city.\n-New map plz.\n-Echo\n\nMore things will continue to be added.")
        elif message.content.lower().startswith('!echo'):
            if message.author != 'Sciiva Thathne#6841':
                await message.channel.send(message.content)


client = MyClient()
client.run(token)

