from django.contrib.auth.models import User
from adventure.models import Player, Room


Room.objects.all().delete()

r_outside = Room(title="Outside Cave Entrance",
                 description="North of you, the cave mount beckons")

r_foyer = Room(title="Foyer", description="""Dim light filters in from the south. Dusty
passages run north and east.""")

r_overlook = Room(title="Grand Overlook", description="""A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""")

r_narrow = Room(title="Narrow Passage", description="""The narrow passage bends here from west
to north. The smell of gold permeates the air.""")

r_treasure = Room(title="Treasure Chamber", description="""You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")

r_darkplace = Room(title="Dark Place",
                   description="""Even in a dark place you can find a bright light.""")

r_wonderland = Room(title="Wonderland",
                    description="""You've found the best place to be! Here you don't have to worry about anything.""")

r_mercury = Room(
    title="Mercury", description="""Way too hot in this place, try to get out as soon as you can.""")

r_starlane = Room(title="Starlane",
                  description="""The stars are in your favor and they are showing..a not so good day for you :(.""")

r_outside.save()
r_foyer.save()
r_overlook.save()
r_narrow.save()
r_treasure.save()
r_darkplace.save()
r_wonderland.save()
r_mercury.save()
r_starlane.save()

# Link rooms together
r_outside.connectRooms(r_foyer, "n")
r_foyer.connectRooms(r_outside, "s")

r_foyer.connectRooms(r_overlook, "n")
r_overlook.connectRooms(r_foyer, "s")

r_foyer.connectRooms(r_narrow, "e")
r_narrow.connectRooms(r_foyer, "w")

r_narrow.connectRooms(r_treasure, "n")
r_treasure.connectRooms(r_narrow, "s")

r_darkplace.connectRooms(r_wonderland, "e")
r_wonderland.connectRooms(r_darkplace, "w")

r_starlane.connectRooms(r_darkplace, "n")
r_mercury.connectRooms(r_wonderland, "s")

r_darkplace.connectRooms(r_outside, "e")
r_outside.connectRooms(r_darkplace, "w")

r_narrow.connectRooms(r_starlane, "n")
r_starlane.connectRooms(r_narrow, "s")

r_starlane.connectRooms(r_overlook, "e")
r_overlook.connectRooms(r_starlane, "w")

r_wonderland.connectRooms(r_outside, "e")
r_outside.connectRooms(r_wonderland, "w")

players = Player.objects.all()
for p in players:
    p.currentRoom = r_outside.id
    p.save()
