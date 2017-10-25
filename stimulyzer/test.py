'''
Created on 25 Oct 2017

@author: nsamways
'''
#!/usr/bin/env

from PIL import Image, ImageDraw
import random

def main():
    
    base_name = "stimuli_"
    
    stim_size = width, height = 640, 480
    border_bound = 10
    
    object_number = 30
    background_colour = "green"
    set_size = 10
    
    object_size = 50
    
    shape_1_colour = "red"

    for j in range(set_size):

        base_filepath = '/home/nsamways/stims/'
        
        image = Image.new( "RGB" , stim_size, background_colour )
        stim = ImageDraw.Draw(image);   

        for i in range(object_number):

        # create a random coordinate bounded by min and max
            x1 = random.randint(0, (width - object_size));
            x2 = x1 + object_size

            y1 = random.randint(0, (height - object_size));
            y2 = y1 + object_size;
        
            stim.rectangle(((x1, y1),(x2,y2)), fill = shape_1_colour, outline = shape_1_colour)


        stim_file_name = base_name + str(j) + ".jpg" 
    #draw.ellipse((0, 0, 180, 180), fill = 'white', outline ='blue')
    # draw.rectangle(((20,20),(40,40)), fill = 'white', outline = 'blue')
    #draw.rectangle(((0, 00), (100, 100)), fill="black")

 #       image.show();
        image.save(base_filepath + stim_file_name)

        # delete to save memory
        del image;

    
    print("Done")
    
    
if ( __name__ == "__main__"):
    
    main();
    
