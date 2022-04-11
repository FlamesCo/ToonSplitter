
import os
from signal import pause
import sys
import argparse
from subprocess import call
import os
print("Welcome to ToonSplitter.py")
## this prints the ai to run the main function in the program
def main():
    print(main())

    parser = argparse.ArgumentParser(description='Sprite sheet splitter')
    parser.add_argument('-s', '--spritesheet', required=True, help='Spritesheet image')
    parser.add_argument('-o', '--output', required=True, help='Output directory')
    parser.add_argument('-x', '--tilesize-x', type=int, default=16, help='Tile size in X axis')
    parser.add_argument('-y', '--tilesize-y', type=int, default=16, help='Tile size in Y axis')


## ask what url to use
    args = parser.parse_args()
    print("Using spritesheet: " + args.spritesheet)
    print("Using output directory: " + args.output)
    print("Using tile size: " + str(args.tilesize_x) + "x" + str(args.tilesize_y))
    print("Splitting spritesheet...")
    #split_spritesheet(args.spritesheet, args.output, args.tilesize_x, args.tilesize_y)
    print("Done!")
print("What will you like to split?")
print("Type 1 for a spritesheet")
print("Type 2 for a sprite")
### if 1 is selected then run the spritesheet function
if input() == "1":
    print("You have selected spritesheet")
    print("What is the url of the spritesheet?")
    print("Example:" + "  " + str(input()))
    print("What is the output directory?")
    print("Example:" + "  " + str(input()))
    print("What is the tile size in X axis?")
    print("Example:" + "  " + str(input()))
    print("What is the tile size in Y axis?")
    print("Example:" + "  " + str(input()))
    print("Splitting spritesheet...")
    print("Done!")
print("What will you like to split?")
print("Example:" + " " + str(input()))
print("What is the url of the sprite?")
print("Example:" + " " + str(input()))
print("What is the output directory?")
print("Example:" + " " + str(input()))
print("Logging complete...")
## render the file to pictures folder in icloud
os.system("open -a /Applications/iCloud\ Drive.app")
## generate a ai generated picture 32x32 of the sprite sheet and splice it into the sprite sheet by rows of columns
imoress = "convert -crop 32x32 " + str(input()) + " " + str(input()) + "/" + str(input()) + ".png"
print(imoress,"Done!")
print("Exiting...")
print("Thank you for using ToonSplitter.py")
pause()
print("Waiting...")
print("Thank you for using ToonSplitter.py")
os.exit(0)