from Week4.shorts.museum.artists import get_artists

def main():
    artist = input("artist: ")
    artists = get_artists(query=artist, limit=3)
    for artist in artists:
        print(f"* {artist}")


main()
