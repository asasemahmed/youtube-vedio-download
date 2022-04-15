from pytube import YouTube
from time import sleep


def check_link(url):

    try:
        yt = YouTube(url)
        return True

    except:
        return False


def download_vedio(url):
    yt = YouTube(url)

    strem1 = yt.streams.get_highest_resolution()

    print("Downloading ....")

    strem1.download()


def download_audio(url):
    yt = YouTube(url)

    strem1 = yt.streams.get_audio_only()

    print("Downloading ....")

    strem1.download()


def download_quality(url, num):
    yt = YouTube(url)

    strem1 = yt.streams.get_by_itag(num)

    print("Downloading ....")

    strem1.download()


print("HELLO in my programe ")

print("_" * 40)

print("\n ASEM AHMED ABDALLAH ")

print("_" * 40)

print("\n")

traise = 3

link_URL = None


out = 0
while traise > 0:

    link_URL = input("Pleas put the link vedio here : ").strip()

    if check_link(link_URL):
        out = 1
        break

    else:
        print("\nYour link is not found ")

        traise -= 1

        continue

if out == 1:

    print("_" * 50)

    print("""
for video (hight quality) enter => 1
for audio (music) enter => 2 
for vedio and quality => 3 \n""")

    choise = int(input("Enter your choise : ").strip())

    print("\n \n")

    if choise == 1:

        download_vedio(link_URL)

    elif choise == 2:

        download_audio(link_URL)

    elif choise == 3:

        print("""
for <360p> => 1
for <720> => 2
        """)

        choise2 = int(input("Enter your choise : ").strip())

        print("\n")

        if choise2 == 1:
            n1 = 18
            download_quality(link_URL, n1)

        elif choise2 == 2:
            n2 = 22
            download_quality(link_URL, n2)

        else:

            print("Eror pleas choise number from the list")

    else:

        print("Eror pleas choise number from the list")
else:

    print("you are out the programe ")


print("Thank you for using my app ")

print("_" * 40)

print("\n ASEM AHMED ABDALLAH ")

print("_" * 40)

sleep(20)
