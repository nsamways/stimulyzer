'''
Created on 25 Oct 2017

@author: nsamways
'''
#!/usr/bin/env

from PIL import Image, ImageDraw

from ConfigParser import ConfigParser

import random, glob 

def main():

    # read in the config file as passed by CLAs
    ( base_config, distractor_list, target_parameters ) = get_configuration()   
    
    # calculate the size of the matrix, the offsets, and 
    
    
    stim_size = 
    # calculate the number of loci, total number of objects etc.
    
    # create the shape and 
    
    
    # Main loop for creation of all images        
    for j in range(set_size):

        # create the 'canvas' and make it global
        
        image = Image.new( "RGB" , stim_size, background_colour )
        global image
        
        stim = ImageDraw.Draw(image);   
        
        # loop through for each individual stimulus
        for i in range(object_number):
        


        stim_file_name = base_name + str(j) + ".jpg" 

        image.save(base_filepath + stim_file_name)

        # delete to save memory
        del image;

    
    print("Done")
    
    
if ( __name__ == "__main__"):
    
    main();

def get_configuration( conf_filename = "config.ini" ):

# set up the members
    
    # set up config paresr and read in config items
    cfg = ConfigParser()
    cfg.read( conf_filename )
    
    # get the different sections      
    all_sections = cfg.sections()
#     print(cfg.items('Base Parameters')) 
#     print(cfg.get('Items1','Colour'))

    # get the base section
    for section_name in all_sections:
        
        if ("base_parameters" in section_name):
            # set the base parameters
            
        elif ("distractor" in section_name):
            # set distractor parameters
        elif ("target" in section_name):
            # set the target parameters
            

    for each_section in (all_cfg_sections):
        print(" processing section:" + each_section)
        
        # read in the base parameters
        if  "Base Parameters" in each_section:
            # list through parameters
            pass
            
        elif "Items" in each_section:
            # add the item type to the      
            
            
    # read in the base parameters
    base_name = cfg.get('Base Parameters','Base Name')
    stim_size = width, height = cfg.getint('Base Parameters','Width'), cfg.getint('Base Parameters', 'Height');
    base_filepath = cfg.get('Base Parameters','Directory Path')
    background_colour = cfg.get('Base Parameters','BG Colour')
    set_size = cfg.getint('Base Parameters','Number of stimuli')

    
    object_number = cfg.getint('Items1','Number')
    object_size = cfg.getint('Items1', 'Bounding Size')
    shape_1_colour = cfg.get('Items1','Colour')
    fill = cfg.getboolean('Items1', 'Fill')
    
return(base_params, distractors, target_params)


def paint_polygons():
    


#         # create a random coordinate bounded by min and max
#             x1 = random.randint(0, (width - object_size));
#             x2 = x1 + object_size
# 
#             y1 = random.randint(0, (height - object_size));
#             y2 = y1 + object_size;
#         
#             if (fill):
#                 stim.rectangle(((x1, y1),(x2,y2)), fill = shape_1_colour, outline = shape_1_colour)
#             else:
#                 stim.rectangle(((x1, y1),(x2,y2)), outline = shape_1_colour)

