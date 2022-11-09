import os

# We inform the user about the different options
print("720p = 1 \n480p = 2\n360x240 = 3\n160x120 = 4\nSELECCIONA LA OPCIÓN:")
option = int(input())  # user input
vide_name = 'BigBuckBunny_512kb.mp4'


# depending on the option the user has chosen we execute a concrete command
def convert_to(option, name):
    command = ''
    if option == 1:
        command = 'ffmpeg -i {} -s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 720p.mp4'.format(name)
    elif option == 2:
        command = 'ffmpeg -i {} -s hd480 -c:v libx264 -crf 23 -c:a aac -strict -2 480p.mp4'.format(name)
    elif option == 3:
        command = 'ffmpeg -i {} -vf scale=360:240 360x240.mp4'.format(name)
    elif option == 4:
        command = 'ffmpeg -i {} -vf scale=160:120 160x120.mp4'.format(name)

    os.system(command)


convert_to(option, vide_name)

"ffmpeg -i input.mp4 -c:v libvpx -b:v 1M -c:a libvorbis output.webm" #convert vp8
"ffmpeg -i input.mp4 -c:v libvpx-vp9 -b:v 2M -pass 1 -an -f null /dev/null && \
ffmpeg -i input.mp4 -c:v libvpx-vp9 -b:v 2M -pass 2 -c:a libopus output.webm" #convert vp9
"ffmpeg -i input -c:v libx265 -crf 26 -preset fast -c:a aac -b:a 128k output.mp4" #convert to 265
"ffmpeg -i input.mp4 -c:v libaom-av1 -crf 30 -b:v 0 av1_test.mkv" #convert to av1





