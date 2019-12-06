from requests import session
import argparse
import json
from os import system
import validators
import sys

def main():

    parseData = parse_cli()
    # print(parseData)
    tempUrl = make_url(parseData['url'])

    with session() as session:
        respons = session.get(url=tempUrl)
    
    musicData = dict(json.loads(respons.content))
    
    # wanted = ['plays','id','title','link','artist',\
    #     'song','likes','dislikes','downloads','photo']

    print("\033[93m=================|Music Info|=======================\33[0m")
    print('\033[95mSong: \033[33m',musicData['song'],'  ','\033[95martist: \033[33m',musicData['artist'])
    print('\33[31m♥',musicData['likes'],'\33[0m | ','\33[34m⮮',musicData['downloads'],'\33[0m | ','\33[36m⯈',musicData['plays'])
    print("\033[93m====================================================\33[0m")
    
    fileName = str(musicData['song']).replace(' ',"")+'-'+str(musicData['artist']).replace(' ',"")

    #download music with user option
    download_file(
        rj_url=musicData['link'],
        path=parseData['dir'],
        connection=parseData['connection'],
        filename=fileName+'.mp3'
    )

    #download cover of music 
    if parseData['photo'] == True:
        photoFileName=musicData['title']+'.jpg'
        print(photoFileName)
        download_file(
            rj_url=musicData['photo'],
            path=parseData['dir'],
            connection=parseData['connection'],
            filename=fileName+'.jpg'
        )

    #download lyric of music
    if parseData['lyric'] == True:
        lyric = musicData['lyric']
        with open(parseData['dir']+'/%s-lyric.txt'%fileName,'w') as ltxtfile:
            for row in lyric:
                ltxtfile.write(row)

def download_file(rj_url,path,connection,filename):
    result = system("aria2c -c -x{0} -d {1} -o {2} {3}".format(connection,path,filename,rj_url))
    if result !=0:
        print('sorry somthing is wrong ')
        sys.exit()

def parse_cli():

    #create a parser for cli
    parser = argparse.ArgumentParser(
        description="radiojavan.com music downloader",
        prog= "rjdl"
    )

    #add --link ,-l argument to our parser

    parser.add_argument(
        'url',
        type=str,
        action='store',
        help = "the link of music in radiojavan.com"
    )

    parser.add_argument(
        '-d',
        '--dir',
        metavar='',
        type=str,
        action='store',
        required=False,
        default='~/Downloads/',
        help = "the path for saving mp3 file.  Default: ~/Downloads"
    )

    parser.add_argument(
        '-c',
        '--connection',
        choices=range(1,17),
        metavar='',
        type=int,
        action='store',
        required=False,
        default=1,
        help = "The maximum number of connections to one server for each download.  Default: 1"
    )
    
    parser.add_argument(
        '-l',
        '--lyric',
        action='store_true',
        required=False,
        help = "download lyric of music and save it in specified dir.  Default: ~/Downloads"
    )

    parser.add_argument(
        '-p',
        '--photo',
        action='store_true',
        required=False,
        help = "download photo of music and save it in specified dir.  Default: ~/Downloads"
    )

    # parser.add_argument(
    #     '-j',
    #     '--json',
    #     action='store_true',
    #     required=False,
    #     help = "print all information about song and save as json file in specified path Default: ~/Downloads"
    # )

    #call parser to parse terminal argum~/Downloadsent
    cli_args = parser.parse_args()
    try:
        if not(validators.url(cli_args.url) and 'radiojavan.com'in cli_args.url):
            raise parser.error
    except BaseException as f:
        print("url is wrong make sure is from radiojavan.com")
        sys.exit()

    return vars(cli_args)

def make_url(user_url:str):

    rjAPI="https://api-rj-app.com/api2/mp3?id="
    song_name =user_url.split("/")[-1]
    return rjAPI+song_name

if __name__ == "__main__":
    main()