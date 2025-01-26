#!/usr/bin/env python
from rgbmatrix import RGBMatrix, graphics, RGBMatrixOptions
from arrivals import Arrivals
from PIL import Image
import time
import sys
import random
import os
from constants import Colors

class RunText():
    def __init__(self):
        options = RGBMatrixOptions()
        options.rows = 32
        options.cols = 64
        options.chain_length = 1
        options.parallel = 1
        options.brightness = 60
        options.hardware_mapping = 'adafruit-hat'
        options.drop_privileges=False
        
        self.arrivals = Arrivals()
        self.matrix = RGBMatrix(options=options)
        script_dir = os.path.dirname(__file__)
        abs_file_path = os.path.join(script_dir, "sprites/ctav1.png")

        self.image = Image.open(abs_file_path).convert('RGB')

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        script_dir = os.path.dirname(__file__)
        abs_font_path = os.path.join(script_dir, 'fonts/5x8.bdf')
        font.LoadFont(abs_font_path)
        curr_station = 0
        stations_len = len(self.arrivals.stations)
        img_width, img_height = self.image.size
        pos = 0
        iterator = -1
        ypos = 0
        while True:
            move = True
            station = self.arrivals.stations[curr_station]
            arrival_times = self.arrivals.getArrivalTimes(station)
            text_color = graphics.Color(**Colors.get(station['line'], (255,255,255)))
            topText = arrival_times[0] if len(arrival_times) > 0 else 'No Trains'
            bottomText = arrival_times[1] if len(arrival_times) > 1 else ''
            
            while move:
                offscreen_canvas.Clear()
                r = random.randint(0,100)
                if ypos == 0:
                    #random bumps in the train animation
                    if r > 99:
                        ypos = 1
                else:
                    ypos = 0
                offscreen_canvas.SetImage(self.image, pos, ypos)
                pos += iterator
                time.sleep(0.05)
                
                graphics.DrawText(offscreen_canvas, font, 0, 24, textColor, topText)
                graphics.DrawText(offscreen_canvas, font, 0, 32, textColor, bottomText)
                offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
                if iterator < 0:
                    if pos+img_width-64 < 0:
                        move = False
                else:
                    if pos+img_width-64 > img_width-64:
                        move = False
            time.sleep(1)
            offscreen_canvas.Clear()
            curr_station = (curr_station + 1) % stations_len
            iterator *= -1

    def process(self):
        try:
            print("Press CTRL-C to stop")
            self.run()
        except KeyboardInterrupt:
            print("Exiting...")
            sys.exit(0)
        return True



if __name__ == '__main__':
    run_text = RunText()
    if(not run_text.process()):
        print('error')

