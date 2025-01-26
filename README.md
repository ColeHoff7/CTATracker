# CTATracker
This is a project for tracking the CTA stations nearest me so I can display them on an LED display. Feel free to use it, modifying it with the stations nearest you.

![](https://github.com/ColeHoff7/CTATracker/blob/main/traintracker.gif)

# Requirements
You will need to get an API key from the Chicago Transit Authority [here](https://www.transitchicago.com/developers/traintrackerapply/) This will go in a file `apikey.json` in the `src` directory of this project

### This project uses the following:
 - a Raspberry Pi (any version should do, I am using a raspberry pi 2)
 - a [64x32 bit 4mm pitch RGB LED Board](https://www.adafruit.com/product/3826)
 - a [RGB Matrix Bonnet for Raspberry Pi](https://www.adafruit.com/product/3211)
 - a power supply (check to see what your specific raspberry pi needs but I used [this](https://www.amazon.com/Facmogu-Switching-Transformer-Compatible-5-5x2-1mm/dp/B087LY41PV?crid=19AK1JBA30YN2&dib=eyJ2IjoiMSJ9.k2G2uL_Nwdin6cBMXFiRHFfziB0oU0vrMPj1Q_pZ2pfRGVnOv8hc6YNZJxjnKBE0RmkRQ4FYSApO8e1Eg2yD1ChYpOT78dSguhfpgRAoH-4eaEt-0wTxkj5s6LkBvWwqnmWN4yDJjhy6av4h9TnDk77fMjsfgb982pYkgJU5TOron3Kj_nZsrkVLeiEG-n--oRv9sfrEV596dQwIwPK08PbAitWg77hOcm6wP2BmxVQ62CygR2fciwUyYW49_6AA7ryEA4BxbluylxvrANe_vI3God428GlOUed-LMPjbpFhIAveTKLPxogWdwHoJ0ZUd343iW1GKadZ5_gYQ03Yq_8vq2SDtKdM0oOZfKj_zoQ.KHoCuzDXpxuApVQljyr3qQzarNdP7TXmSCKbWUNfAa8&dib_tag=se&keywords=5V%2B4A%2B20W&qid=1736373892&s=electronics&sprefix=5v%2B4a%2B20w%2Celectronics%2C98&sr=1-2&th=1))

### RGB Board libraries
This project makes use of the [Adafruit RGB matrix installer script](https://github.com/adafruit/Raspberry-Pi-Installer-Scripts/blob/main/rgb-matrix.sh) to install the needed libraries to interface with the RGB board. At the moment you need to install this on your pi yourself, but I plan on writing an install script that will do all of this in the future


# TODO in the future:
- automated install on raspberry pis
- google maps integration to automatically get nearest stations
- bus support