#!/usr/bin/env python
# Display a runtext with double-buffering.
from rgbmatrix import RGBMatrix, graphics, RGBMatrixOptions
from arrivals import Arrivals
import time
import sys

class RunText():
    def __init__(self):
        options = RGBMatrixOptions()
        options.rows = 32
        options.cols = 64
        options.chain_length = 1
        options.parallel = 1
        options.hardware_mapping = 'adafruit-hat'
        options.drop_privileges=False
        
        self.arrivals = Arrivals()
        self.matrix = RGBMatrix(options=options)

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("./fonts/5x8.bdf")
        textColor = graphics.Color(255, 0, 0)
        showBelmont = False
        while True:
            pos = 0
            [southport, belmont] = self.arrivals.getArrivalTimes() 
            if showBelmont:
                textColor = graphics.Color(255, 0, 0)
                topText = belmont[0] if len(belmont) > 0 else 'No Trains'
                bottomText = belmont[1] if len(belmont) > 1 else ''
            else:
                textColor = graphics.Color(180, 90, 5)
                topText = southport[0] if len(southport) > 0 else 'No Trains'
                bottomText = southport[1] if len(southport) > 1 else ''
            length = graphics.DrawText(offscreen_canvas, font, pos, 8, textColor, topText)
            graphics.DrawText(offscreen_canvas, font, pos, 16, textColor, bottomText)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
            time.sleep(3)
            while pos+length > 0:
                offscreen_canvas.Clear()
                length = graphics.DrawText(offscreen_canvas, font, pos, 8, textColor, topText)
                graphics.DrawText(offscreen_canvas, font, pos, 16, textColor, bottomText)
                pos -= 1

                time.sleep(0.05)
                offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
            offscreen_canvas.Clear()
            showBelmont = not showBelmont

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

