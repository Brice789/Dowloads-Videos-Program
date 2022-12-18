import os
from pytube.__main__ import YouTube

def passmooitonlien(link):
    youtubeObject = Youtube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution
    try:
        youtubeObject.download()
    except:
        print("votre fonction n'a pas pu etre télécharger")
    print("fecilitation, voici votre vidéo")

link = input("met ton lien youtube ici:" )
passmooitonlien(link)

