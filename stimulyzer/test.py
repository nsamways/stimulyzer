'''
Created on 25 Oct 2017

@author: nsamways
'''
#!/usr/bin/env

from PIL import Image, ImageDraw
from ConfigParser import ConfigParser
import random

def main():

# read in the config file as passed by CLAs

    cfg = ConfigParser()
    cfg.read('config.ini')
#     print(cfg.sections())
#     print(cfg.items('Base Parameters')) 
#     print(cfg.get('Items1','Colour'))
    
    base_name = cfg.get('Base Parameters','Base Name')
    stim_size = width, height = cfg.getint('Base Parameters','Width'), cfg.getint('Base Parameters', 'Height');
    base_filepath = cfg.get('Base Parameters','Directory Path')
    background_colour = cfg.get('Base Parameters','BG Colour')
    set_size = cfg.getint('Base Parameters','Number of stimuli')

    
    object_number = cfg.getint('Items1','Number')
    object_size = cfg.getint('Items1', 'Bounding Size')
    shape_1_colour = cfg.get('Items1','Colour')
    fill = cfg.getboolean('Items1', 'Fill')
    
    for j in range(set_size):

        image = Image.new( "RGB" , stim_size, background_colour )
        stim = ImageDraw.Draw(image);   

        for i in range(object_number):

        # create a random coordinate bounded by min and max
            x1 = random.randint(0, (width - object_size));
            x2 = x1 + object_size

            y1 = random.randint(0, (height - object_size));
            y2 = y1 + object_size;
        
            if (fill):
                stim.rectangle(((x1, y1),(x2,y2)), fill = shape_1_colour, outline = shape_1_colour)
            else:
                stim.rectangle(((x1, y1),(x2,y2)), outline = shape_1_colour)


        stim_file_name = base_name + str(j) + ".jpg" 

        image.save(base_filepath + stim_file_name)

        # delete to save memory
        del image;

    
    print("Done")
    
    
if ( __name__ == "__main__"):
    
    main();
    
