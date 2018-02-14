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
    
    
    print("Base config:" + str(base_config))
    
    exit()
    
    
    # convert some of the list to sensible variable names for easier handling
    stim_width = int(base_config["Width"])
    stim_height = int(base_config["Height"])
    stim_set_size = int(base_config["Number of Stimuli"])
    
        
    # calculate the size of the matrix, the offsets etc.
    # first calculate the maximum cell size, based on the largest size of distractor plus padding
    
    maximum_stim_radius = 0;
    
    for shapes in distractor_list:
        # get the size of current distractor 
        cur_size = int(shapes["Radius"])

        if  cur_size > maximum_stim_radius:
            maximum_stim_radius = cur_size
    
    if int(target_parameters["Radius"]) > cur_size:
        cur_size = int(target_parameters["Radius"])
    
    
    
    
    # calculate the number of loci, based on total number of objects etc.
    
    objects_per_width = floor( max_cell_width / stim_width )
    objects_per
    
    objects_per_height = 2
    
    # create the shape and coordinate matrix
    shape_matrix = []
    coord_matrix = []
    
    # loop through matrix, giving x,y coordinates for each loci
    
    
    # Main loop for creation of all stimuli        
    for j in range(stim_set_size):
        # we do this for a single stimuli (image)

        # create the 'canvas' and make it global so that the other functions can draw on it
        image = Image.new( "RGB" , stim_size, background_colour )
        global image
        
        stim = ImageDraw.Draw(image)


        # populate the shape matrix NB: the coord matrix remains the same for all stims'
        
        # push all the distractors in to the matrix
        
        # push the 'spaces' on
        
        # shuffle the matrix (randomise it)
        
        # add the target, depending on L or R
        
        # traverse the shape matrix, passing to correct function for drawing on  

   
        
        # loop through for each individual stimulus
        for i in range(object_number):
            pass
        
        # set the filename and save the file to the appropriate path / name based on base name and current iteration        
        stim_file_name = str(base_config["Base Name"]) + "_" + str(j) + ".jpg" 
        
        # save the image  
        image.save(base_filepath + stim_file_name)


        # delete to save memory
        del image;

    
    print("Done")
    
    
def get_configuration( conf_filename = "config.ini" ):

    # set up the distractor as a list as this will contain the multiple dicts
    distractors = []
    base_params = {}
    target_params = {}
    
    # set up config paresr and read in config items
    cfg = ConfigParser()
    cfg.read( conf_filename )
    
    # get the different sections      
    all_sections = cfg.sections()

    # get the base section
    for section_name in all_sections:
        
        if ("Base Parameters" in section_name):
            # set the base parameters
            for all_items in cfg.items(section_name):
                # append each pair to the dict
                for pairs in all_items:
                    base_params[pairs[0]] = pairs[1]
            
            
        elif ("Distractor" in section_name):
            # set distractor parameters
            # this is less easy because there could be multiple distractors and they need to be pushed to a list
            curr_distractor_dict = {}
             
            # set the current distractor
            for all_items in cfg.items(section_name):
                # append each pair to the dict
                for pairs in all_items:
                    print all_items
                    exit()
                    curr_distractor_dict[pairs[0]] = pairs[1]           
             
            # pop the current distractor on to the list
            distractors.append(curr_distractor_dict)
            # delete the temp dict
            del curr_distractor_dict
             
        elif ("Target" in section_name):
            # set the target parameters
            for all_items in cfg.items(section_name):
                # append each pair to the dict
                for pairs in all_items:
                    base_params[pairs[0]] = pairs[1]
            
### Use: all_items = cfg.items(section_name) to give list of lists.  Then convert to dict with: for pairs in all_items: dict[pairs[0]] = pairs[1] 
            
    return(base_params, distractors, target_params)



# def paint_polygons(x_coord, y_coord, shape_info):
#     
#     # set up the vertex list
#     vertices = []
#     
#     # get some 
#     poly_radius = int ( shape_info[  ])
#     
#     # create the list of vertices
#     for ( i in range (int(shape_info["Vertices"]))):
#         # create the points as pairs
#         
#         # x coord
#         xi = x_coord + math.sin()
#         yi = y_coord + math.cos()
#         
#         point_pair = [xi, yi]
#         
#         # push new point on to vertex list
#         vertices.append( point_pair )
# 
#     # draw this polygon on to the stimulus image
#     
#     stim.polygon()
#         
# return()
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

if ( __name__ == "__main__"):
    
    main();
