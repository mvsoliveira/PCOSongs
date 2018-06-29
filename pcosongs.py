from pypco import PCO

pco = PCO("a44104694953ca93f82bb0d146a5607e13ab463adcf9393fcaadee96600a7be6","0aeb79ec9420b7865805cabc4fd51f72dc716d146ea3b2894fbf0c7d1553b79f")

# for person in pco.people.people.list():
#     print(person)

for song in pco.services.songs.list():
    print(song.data['attributes']['title'])
    for arrangement in song.rel.arrangements.list():
        print(arrangement.data['attributes']['lyrics'])



print('oi')

# for arrangement in pco.services.arrangements.list():
#     print(arrangement)

