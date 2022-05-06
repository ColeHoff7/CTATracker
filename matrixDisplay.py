#!/usr/bin/env python
from rgbmatrix import RGBMatrix, graphics, RGBMatrixOptions
from arrivals import Arrivals
from PIL import Image
import time
import sys
import random

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
        self.image = Image.open('./sprites/ctav1.png').convert('RGB')

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("./fonts/5x8.bdf")
        textColor = graphics.Color(255, 0, 0)
        showBelmont = False
        img_width, img_height = self.image.size
        pos = 0
        iterator = -1
        ypos = 0
        while True:
            move = True
            [southport, belmont] = self.arrivals.getArrivalTimes() 
            if showBelmont:
                textColor = graphics.Color(255, 0, 0)
                topText = belmont[0] if len(belmont) > 0 else 'No Trains'
                bottomText = belmont[1] if len(belmont) > 1 else ''
            else:
                textColor = graphics.Color(180, 90, 5)
                topText = southport[0] if len(southport) > 0 else 'No Trains'
                bottomText = southport[1] if len(southport) > 1 else ''
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
            showBelmont = not showBelmont
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

