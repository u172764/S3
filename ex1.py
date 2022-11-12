import os

# We inform the user about the different options
vide_name = 'video_cortado2.mp4'  # we have cut the video since the original BBB was so slow


# depending on the option the user has chosen we execute a concrete command
def convert_to(name):
    print("720p = 1 \n480p = 2\n360x240 = 3\n160x120 = 4\nSELECCIONA LA OPCIÓN:")
    option1 = int(input())  # user input
    command = ''
    name2 = ''
    if option1 == 1:
        name2 = '720p.mp4'
        command = 'ffmpeg -i {} -s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 {}'.format(name, name2)
    elif option1 == 2:
        name2 = '480p.mp4'
        command = 'ffmpeg -i {} -s hd480 -c:v libx264 -crf 23 -c:a aac -strict -2 {}'.format(name, name2)
    elif option1 == 3:
        name2 = '360x240.mp4'
        command = 'ffmpeg -i {} -vf scale=360:240 {}'.format(name, name2)
    elif option1 == 4:
        name2 = '160x120.mp4'
        command = 'ffmpeg -i {} -vf scale=160:120 {}'.format(name, name2)
    os.system(command)
    return name2


def combine4videos(name1, name2, name3, name4):
    command = ' ffmpeg -i {} -i {} -i {} -i {} -filter_complex \
                "[0:v][1:v]hstack[t];[2:v][3:v]hstack[b];[t][b]vstack[v]; \
                [0:a][1:a][2:a][3:a]amerge=inputs=4[a]" \
                -map "[v]" -map "[a]" -ac 2 -shortest final_video.mp4'.format(name1, name2, name3, name4)
    os.system(command)


def compare_codecs(name):
    video_name = convert_to(name)
    command = "ffmpeg -i {} -c:v libvpx -b:v 2M output.webm".format(video_name)
    os.system(command)
    command = "ffmpeg -i {} -c:v libvpx-vp9 -b:v 2M output2.webm ".format(video_name)
    os.system(command)
    command = "ffmpeg -i {} -c:v libx265 -b:v 2M output.mp4".format(video_name)
    os.system(command)
    command = "ffmpeg -i {} -c:v libaom-av1 -b:v 2M output.mkv".format(video_name)
    os.system(command)
    combine4videos('output.webm', 'output2.webm', 'output.mp4', 'output.mkv')


compare_codecs(vide_name)
