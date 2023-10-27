import webbrowser, time

links = [
    'https://www.youtube.com/watch?v=9AZA6fREkoA',
    'https://www.youtube.com/watch?v=IzyTGeoYPLk',
    'https://www.youtube.com/watch?v=ixWNXktzO6U',
    'https://www.youtube.com/watch?v=fHSwm9BRT1c',
    'https://www.youtube.com/watch?v=FhImbRQTRxg',
    'https://www.youtube.com/watch?v=iyq6dnXkLpM',
    'https://www.youtube.com/watch?v=XOD_0x6Re6o'
]

print("Maybe lower your volume, auto playing in 3 seconds!")

time.sleep(3)

for link in links:
    webbrowser.open(link)