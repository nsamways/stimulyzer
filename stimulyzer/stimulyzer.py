'''
Created on 25 Oct 2017

@author: nsamways
'''
#!/usr/bin/env

from PIL import Image, ImageDraw

from ConfigParser import ConfigParser

import random, glob, math 


def main():

    # set some vars
    total_objects_count = []

    # read in the config file as passed by CLAs
    ( base_config, distractor_list, target_parameters ) = get_configuration()   
    
    # check if there is a target present
    if bool(target_parameters()):
        target_present = True
    else:
        target_present = False
    
    # convert some of the dict items to their proper type, and sensible variable names for easier handling
    stim_width = int(base_config["width"])
    stim_height = int(base_config["height"])
    stim_set_size = int(base_config["number of stimuli"])
    spacer = int(base_config["padding"])
    
    # determine some variables
    stim_size = [stim_width, stim_height]
            
    # calculate the size of the matrix, the offsets etc.
    
    # first calculate the maximum cell size, based on the largest size of object plus padding
    # also get the total number of objects per stimuli
    
    maximum_stim_radius = 0 
    
    i = 0 # enumerator
    for shapes in distractor_list:
        # get the size of current distractor 
        curr_radius = int(shapes["radius"])
        total_objects_count.append(int(shapes["number"])) 
        if  curr_radius > maximum_stim_radius:
            maximum_stim_radius = curr_radius
    
    # do also for target, if present
    if (target_present):
    
        if int(target_parameters["radius"]) > maximum_stim_radius:
            total_objects_count.append(int(shapes["number"])) 
    
        
    max_cell_height = max_cell_width = 2 * maximum_stim_radius + spacer

    objects_per_width = math.floor( stim_width / max_cell_width)
    objects_per_height = math.floor( stim_height / max_cell_height )

    # now check that the total obs' per width and height, PLUS the extra spacer fits within the stimuli size
    if (objects_per_width * max_cell_width + spacer) > stim_width:
        print("Horizontal padding overlap. Reducing cells per width by 1")
        objects_per_width -= 1
    
    if (objects_per_height * max_cell_height + spacer) > stim_height:
        print("Verticle padding overlap. Reducing cells per width by 1")
        objects_per_height -= 1
    # we also need to check that there are an even number of cols, else we can't have left/right targets
    
    # now we have the max number of slots, we can work out the offsets:
    horizontal_offset = math.floor(( stim_width - (objects_per_width * max_cell_width + spacer)) / 2 )
    verticle_offset = math.floor(( stim_height - (objects_per_height * max_cell_height + spacer)) / 2 )
        
        
    # calculate the number of loci, based on total number of objects etc.
    
    total_loci = objects_per_height * objects_per_width
    
    # calculate the number of empty loci
    num_spacers = total_loci - sum(total_objects_count)

    if target_present:
        num_spacers -= int(target_parameters["number"])

    # check there are less objects than loci
    if num_spacers < 0:
        print("There are more objects than available slots. Exiting.")
        exit()
           
    # now add on the extra padding for symmetry
    print("Target present:" + str(target_present))
    print("Objects per width:" + str(objects_per_width))
    print("Objects per height:" + str(objects_per_height))
    print("Max stim radius:" + str(maximum_stim_radius))   
    print("Max cell height:" + str(max_cell_width))   
    print("Total objects:" + str(sum(total_objects_count)))
    print("Total loci" + str(total_loci))
    
    # create the base_shape and coordinate matrices
    base_shape_matrix = []
    
    for object_types in range(len(total_objects_count)):
        for j in range(total_objects_count[object_types]):
            base_shape_matrix.append(object_types)
    # now push on the spacers as value: -1
    for instances in range(num_spacers):
        base_shape_matrix.append(-1)
    
    
    # we will use shuffled copies of the base_shape_matrix for the stims as this will remain the same throughout each iteration

    coord_matrix = [] 
    
    # loop through matrix, giving x,y coordinates for each loci
    
    # set up the x,y list
    coord_pair = []
    
    for mat_rows in range(objects_per_height):
        for mat_cols in range(objects_per_width):
            # calculate and push the x,y coordinate tuple on to coord matrix
            # nb. add: offset + one spacer + radius + (2 * radius + spacer)
            coord_pair = ((horizontal_offset + maximum_stim_radius + spacer + (mat_cols * (2 * maximum_stim_radius + spacer))),(verticle_offset + maximum_stim_radius + spacer + (mat_rows * (2 * maximum_stim_radius + spacer))) ) 
            coord_matrix.append(coord_pair) # push the current pair on the the vector    

    # now we have the shape matrix (well, vector), and the coordinate matrix (well, vector) so can start drawing the shapes

    # we need to push the target on to the distractor list now because we need to pass the parameters to the 'draw_polygon' function when the target is called.
         
    distractor_list.append(target_parameters)
    
    # Main loop for creation of all stimuli        
    for j in range(stim_set_size):
        # we do this for a single stimuli (image)
        
        # duplicate the base_shape matrix, then shuffle it for this stimulus
        current_shape_matrix = base_shape_matrix        
        random.shuffle(current_shape_matrix)
        
        # add in the distractor(s) NOTE: we do this now because we need to ensure it is placed correctly
        if (target_present):
            # check if position is left or right
            if ("left" in target_parameters["position"]):
                # make sure the target is appended on the left.
                
                
            elif ("right" in target_parameters):
                # make sure the target is appended to the right.
            else:
                print("The target position is not specified, so appending randomly")
                current_shape_matrix.insert(randint(0,len(current_shape_matrix)), len(total_objects_count)) #  NOTE: len(total_objects_count) will give the next number in the sequence
        
        
        global stim
        # create the 'canvas' and make it global so that the other functions can draw on it
        image = Image.new( "RGB" , stim_size, background_colour )
        stim = ImageDraw.Draw(image)

        # loop through for each individual shape in the shape matrix
        for individual_shape in range(len(shape_matrix)):
            if current_shape_matrix[individual_shape] < 0:
                pass # this is a spacer
            else:
                # pass on the centroid coordinates and shape_type to the draw_polygons function
                draw_polygons(coordinate_matrix[individual_shape], distractor_list[current_shape_matrix[individual_shape])
        
        # this should have now drawn all the shapes on.
                
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



def paint_polygons(shape_coordinates, shape_info):
     
    # set up the vertex list
    vertices = []
     
    # get some 
    poly_radius = int ( shape_info["radius"  ])
    poly_vertices = int(shape_info["vertices"])
    
    # calculate the internal angles
    internal_angle = poly_vertices / (2 * math.pi)
     
    # create the list of vertices
    for ( i in range (int(shape_info["Vertices"]))):
        # create the points as pairs
         
        xi = shape_coordinates[0] + math.ceil((poly_radius * math.sin( i * internal_angle)))
        yi = shap_coordinates[1] + math.ceil((poly_radius * math.cos( i * internal_angle)))
         
        point_pair = [xi, yi]
         
        # push new point on to vertex list
        vertices.append( point_pair )
 
    # draw this polygon on to the stimulus image
     
    stim.polygon(vertices,)
         
return()


def write_AOIs(coord_list, shape_:
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
