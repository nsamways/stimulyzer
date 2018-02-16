'''
Created on 25 Oct 2017

@author: nsamways
'''
#!/usr/bin/env

from PIL import Image, ImageDraw

from ConfigParser import ConfigParser

import random, glob, math 

def main():

    # read in the config file as passed by CLAs
    ( base_config, distractor_list, target_parameters ) = get_configuration()   
    
    # check if there is a target present
    if bool(target.parameters()):
        target_present = True
    else:
        target_present = False
    
    # convert some of the dict items to their proper type, and sensible variable names for easier handling
    stim_width = int(base_config["width"])
    stim_height = int(base_config["height"])
    stim_set_size = int(base_config["number of stimuli"])
    
    # determine some variables
    stim_size = [stim_width, stim_height]
            
    # calculate the size of the matrix, the offsets etc.
    
    
    # first calculate the maximum cell size, based on the largest size of object plus padding
    # also get the total number of objects per stimuli
    
    maximum_stim_radius = 0
    total_objects_per_stim = 0 
    
    i = 0 # enumerator
    for shapes in distractor_list:
        # get the size of current distractor 
        i+=1
        cur_size = int(shapes["radius"])
        total_objects_per_stim += int(shapes["number"]) 
        if  cur_size > maximum_stim_radius:
            maximum_stim_radius = cur_size
    
    # do for target, if present
    if (target_present):
    
        if int(target_parameters["radius"]) > maximum_stim_radius:
            maximum_stim_radius = int(target_parameters["number"])
    
        total_objects_per_stim += int(target_parameters["number"])
        
    max_cell_height = max_cell_width = maximum_stim_radius + int(base_config["padding"])


    objects_per_width = math.floor( stim_width / max_cell_width)
    objects_per_height = math.floor( stim_height / max_cell_height )

    # now check that the total obs' per width and height, PLUS the extra spacer fits within the stimuli size
    if (objects_per_width * max_cell_width + int(base_config["padding"])) > stim_width:
        print("Horizontal padding overlap. Reducing cells per width by 1")
        objects_per_width -= 1
    
    if (objects_per_height * max_cell_height + int(base_config["padding"])) > stim_height:
        print("Verticle padding overlap. Reducing cells per width by 1")
        objects_per_height -= 1
        
    # calculate the number of loci, based on total number of objects etc.
    
    total_loci = objects_per_height * objects_per_width
    
    # calculate the number of empy loci
    num_spacers = total_loci - total_objects_per_stim

    # check there are less objects than loci
    if num_spacers < 0:
        print("There are more objects than available slots. Exiting.")
        exit()
         
    # create a list of distractors in the form: [[type, number],[type, number]]
    for current_distractor_idx in range(len(distractor_list)):
        number_of_current_distractor = (distrator_list[current_distractor_idx][""])
    
    # append spacers
    
    # now add on the extra padding for symmet
    print("Target present:" + str(target_present))
    print("Objects per width:" + str(objects_per_width))
    print("Objects per height:" + str(objects_per_height))
    print("Max stim radius:" + str(maximum_stim_radius))   
    print("Max cell height:" + str(max_cell_width))   
    print("Total objects:" + str(total_objects_per_stim))
    print("Total loci" + str(total_loci))
    
    # create the base_shape and coordinate matrices
    base_shape_matrix = []
    coord_matrix = []
    
    
    
    # loop through matrix, giving x,y coordinates for each loci
    for mat_rows in range():
        for mat_cols in range():
            # calculate and push the x,y coordinate tuple
            
    
    # Main loop for creation of all stimuli        
    for j in range(stim_set_size):
        # we do this for a single stimuli (image)
        
        # dupliceate the base_shape matrix, then shuffle it for this stimulus
        current_shape_matrix = base_shape_matrix
        
        random.shuffle(current_shape.matrix)
        
        # add in the distractor(s) NOTE: we do this now because we need to ensure it is places correctly
        
        draw_po
        
        
        global stim
        # create the 'canvas' and make it global so that the other functions can draw on it
        image = Image.new( "RGB" , stim_size, background_colour )
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
                name, value = all_items
                base_params[name] = value
                
        elif ("Distractor" in section_name):
            # set distractor parameters
            # this is different because there could be multiple distractors and they need to be pushed on to a list
            curr_distractor_dict = {}
             
            # set the current distractor
            for all_items in cfg.items(section_name):
                # append each pair to the dict
                name, value = all_items
                curr_distractor_dict[name] = value           
             
            # pop the current distractor on to the list
            distractors.append(curr_distractor_dict)
            # delete the temp dict
            del curr_distractor_dict
             
        elif ("Target" in section_name):
            # set the target parameters
            for all_items in cfg.items(section_name):
                # append each pair to the dict
                name, value = all_items
                target_params[name] = value     
                       
    return(base_params, distractors, target_params)



def paint_polygons(x_coord, y_coord, shape_info):
     
    # set up the vertex list
    vertices = []
     
    # get some 
    poly_radius = int ( shape_info[  ])
     
    # create the list of vertices
    for ( i in range (int(shape_info["Vertices"]))):
        # create the points as pairs
         
        # x coord
        xi = x_coord + math.sin()
        yi = y_coord + math.cos()
         
        point_pair = [xi, yi]
         
        # push new point on to vertex list
        vertices.append( point_pair )
 
    # draw this polygon on to the stimulus image
     
    stim.polygon()
         
return()
        # create a random coordinate bounded by min and max
            x1 = random.randint(0, (width - object_size));
            x2 = x1 + object_size
 
            y1 = random.randint(0, (height - object_size));
            y2 = y1 + object_size;
         
            if (fill):
                stim.rectangle(((x1, y1),(x2,y2)), fill = shape_1_colour, outline = shape_1_colour)
            else:
                stim.rectangle(((x1, y1),(x2,y2)), outline = shape_1_colour)

if ( __name__ == "__main__"):
    
    main();
