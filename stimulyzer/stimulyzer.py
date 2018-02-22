'''
Created on 25 Oct 2017

@author: nsamways
'''
#!/usr/bin/env

from PIL import Image, ImageDraw

from ConfigParser import ConfigParser

import random, glob, math 


def main():

    # toggle debugging mode
    debugging = False

    # set some vars
    total_objects_count = []
    total_distractors_count = []
    
    # read in the config file as passed by CLAs
    ( base_config, distractor_list, target_parameters ) = get_configuration()   
    
    # check if there is a target present
    if bool(target_parameters):
        if int(target_parameters["number"]) > 0:
            target_present = True
            print ("Target present")
        else:
            target_present = False            
    else:
        target_present = False
    
    # convert some of the dict items to their proper type, and sensible variable names for easier handling
    stim_width = int(base_config["width"])
    stim_height = int(base_config["height"])
    stim_set_size = int(base_config["number of stimuli"])
    spacer = int(base_config["padding"])
    base_filepath = str(base_config["directory path"])
    
    # set some variables
    stim_size = [stim_width, stim_height]
    maximum_stim_radius = 0 
            
    # calculate the size of the matrix, the offsets etc.
    
    # first calculate the maximum cell size, based on the largest size of object plus padding
    # also get the total number of objects per stimuli
    
    for shapes in distractor_list:
        # get the size of current distractor
        curr_radius = int(shapes["radius"])
        total_distractors_count.append(int(shapes["number"])) 
        if  curr_radius > maximum_stim_radius:
            maximum_stim_radius = curr_radius
    
    total_objects_count = total_distractors_count[:]
    
    # do also for target, if present
    if (target_present):
        # add targets to total count
        total_objects_count.append(int(target_parameters["number"])) 
        # check if the radius is bigger than targets
        if int(target_parameters["radius"]) > maximum_stim_radius:
            maximum_stim_radius = int(target_parameters["radius"])

#     print("total objects count:" + str(total_objects_count))
#     print("total distractors count:" + str(total_distractors_count))
#     exit()
    
    max_cell_height = max_cell_width = 2 * maximum_stim_radius + spacer

    objects_per_width = int(math.floor( stim_width / max_cell_width ))
    objects_per_height = int(math.floor( stim_height / max_cell_height ))

    # now check that the total obs' per width and height, PLUS the extra spacer fits within the stimuli size
    if (objects_per_width * max_cell_width + spacer) > stim_width:
        print("Horizontal padding overlap. Reducing cells per width by 1")
        objects_per_width -= 1
    
    if (objects_per_height * max_cell_height + spacer) > stim_height:
        print("Verticle padding overlap. Reducing cells per width by 1")
        objects_per_height -= 1
#     # we also need to check wheter there are an even or odd number of cols for left/right placement
#     if (objects_per_width % 2 == 0):
#         even_col_number = True
    
    # now we have the max number of slots, we can work out the offsets:
    horizontal_offset = math.floor( (stim_width - ((objects_per_width * max_cell_width + spacer) + spacer )) / 2 )
    verticle_offset = math.floor( (stim_height - ((objects_per_height * max_cell_height + spacer)+ spacer )) / 2 )
    
    # print("picture size = " + str( (objects_per_width * max_cell_width + spacer) + spacer))    
        
    # calculate the number of loci, based on total number of objects etc.
    
    total_loci = objects_per_height * objects_per_width
    
    # calculate the number of empty loci
    num_spacers = int(total_loci - sum(total_objects_count))

    # check there are less objects than loci
    if num_spacers < 0:
        print("There are more objects than available slots. Exiting.")
        exit()


    # print a load of info for debugging
    if (debugging):
        print("Target present:" + str(target_present))
        print("Objects per width:" + str(objects_per_width))
        print("Objects per height:" + str(objects_per_height))
        print("Max stim radius:" + str(maximum_stim_radius))   
        print("Max cell height:" + str(max_cell_width))
        print("Total distractors:" + str(sum(total_distractors_count)))   
        print("Total objects:" + str(sum(total_objects_count)))
        print("Total loci" + str(total_loci))
#        print("Total objects var" + str(total_objects_count))
    # create the base_shape and coordinate matrices
    base_shape_matrix = []
    
    # add the distractors to the base_shape_matrix
    for object_types in range(len(total_distractors_count)):
        for j in range(total_distractors_count[object_types]):
            base_shape_matrix.append(object_types)
#            print("adding:" + str(object_types))
#    print("num Spacers: " + str(num_spacers))

     # now push on the spacers as value: -1
    for instances in range(num_spacers):
        base_shape_matrix.append(-1)
    
    # so now we have base_shape_matrix with all distractors and spacers - the target is added later if it exists
    
    # we will use shuffled copies of the base_shape_matrix for the stims as this will remain the same throughout each iteration

    coord_matrix = [] 
    
    # loop through matrix, giving x,y coordinates for each loci
    
    # set up the x,y list
    coord_pair = []
    
    print("horizontal offset = " + str(horizontal_offset))
    print("verticle offset = " + str(verticle_offset))    
    
    for mat_rows in range(objects_per_height):
        for mat_cols in range(objects_per_width):
            # calculate and push the x,y coordinate tuple on to coord matrix
            # nb. add: offset + one spacer + radius + (2 * radius + spacer)
            coord_pair = ((horizontal_offset + maximum_stim_radius + spacer + (mat_cols * (2 * maximum_stim_radius + spacer))),(verticle_offset + maximum_stim_radius + spacer + (mat_rows * (2 * maximum_stim_radius + spacer))) ) 
            coord_matrix.append(coord_pair) # push the current pair on the the vector    

    # now we have the shape matrix (well, vector), and the coordinate matrix (well, vector) so can start drawing the shapes

    # we need to push the target parameters on to the distractor list now because we need to pass these to the 'draw_polygon' function when the target is called.
    
    distractor_list.append(target_parameters)
    # NB: we have already added the target to the total_objects_count vector, so don't need to do this!
    
    # Main loop for creation of all stimuli        
    for j in range(stim_set_size):
        # we do this for a single stimuli (image)
        
        # duplicate the base_shape matrix, then shuffle it for this stimulus
        current_shape_matrix = base_shape_matrix[:]        

        
#         print (current_shape_matrix)
#         print ("lenght of current_shape_matrix:" +str(len(current_shape_matrix)))
        
        random.shuffle(current_shape_matrix)
        # we've now got a new layout of distractors, and just need to add the target if it is present
        
        # add in the distractor(s) NOTE: we do this now because we need to ensure it is placed correctly
        if (target_present):
            # get a random row in the leftmost column
            first_col_cell = (random.randint(0,(objects_per_height -1)) * objects_per_width )
                     
            col_adjust_size = int(math.floor( objects_per_width / 2.0 ) -1) # we have to subtract one so that the range doesn't hit the middle cell
                        
            # check if position is left or right         
            
            if ("left" in target_parameters["position"]):
                # make sure the target is appended on the left.
                target_place = first_col_cell + random.randint(0,col_adjust_size)
                current_shape_matrix.insert(target_place,(len(total_objects_count) -1))
                # print("target left")
                   
            elif ("right" in target_parameters["position"]):
                # make sure the target is appended to the right.
                target_place = first_col_cell + int(math.ceil(objects_per_width / 2.0))+ random.randint(0,col_adjust_size) + 1
                current_shape_matrix.insert(target_place,(len(total_objects_count) -1))
                #print("target right")
            else:
                print("The target position is not specified, so appending randomly")
                current_shape_matrix.insert(random.randint(0,(len(current_shape_matrix) -1)), (len(total_objects_count) -1)) #  NOTE: len(total_objects_count) will give the next number in the sequence
        
        
        global stim
        # create the 'canvas' and make it global so that the other functions can draw on it
        image = Image.new( "RGB" , stim_size, str(base_config["bg colour"]))
        stim = ImageDraw.Draw(image)
        
#         for i in range(len(current_shape_matrix)):
#             if current_shape_matrix[i] > -1:
#                 print current_shape_matrix[i]
            #else:
        
#         print(str(current_shape_matrix))
#         exit()
        
        # tmpcoords = coord_matrix[:]
        
        # loop through for each individual shape in the shape matrix
        for individual_shape in range(len(current_shape_matrix)):
            if current_shape_matrix[individual_shape] < 0:
                pass # this is a spacer
            else:
                # pass on the centroid coordinates and shape_type to the draw_polygons function
                print("individual shape:" + str(current_shape_matrix[individual_shape]))
                print("size of coord_matrix = " + str(len(coord_matrix)) + " Size of distractor list: " + str(len(current_shape_matrix)))
                paint_polygons(coord_matrix[individual_shape], distractor_list[current_shape_matrix[individual_shape]])
            #    draw_grid(tmpcoords)
        # this should have now drawn all the shapes on.
                
        # set the filename and save the file to the appropriate path / name based on base name and current iteration        
        stim_file_name = str(base_config["base name"]) + "_" + str(j) + ".jpg" 
        
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

def draw_grid(coord_list):
    
    # as debugging, draw the centroid for all points on the grid
    
    for all_points in coord_list:
        curr_point = tuple(all_points)  
        stim.point(curr_point, fill="black")
        print("drawn points: " + str(curr_point))
    

def paint_polygons(shape_coordinates, shape_info):
     
    #stim.polygon(((0,0), (200,200), (0,200)), fill = shape_info["colour"], outline = shape_info["colour"])

    # debugging: draw a green triangle 
     
     
    # set up the vertex list
    vertices = []
     
    # get some 
    poly_radius = int(shape_info["radius"  ])
    poly_vertices = int(shape_info["vertices"])
    
    # calculate the internal angles
    internal_angle =  (2 * math.pi) / poly_vertices
     
    # create the list of vertices
    for  i in range (int(shape_info["vertices"])):
        # create the points as pairs
         
        xi = shape_coordinates[0] + math.ceil((poly_radius * math.sin( (i * internal_angle) + internal_angle /2.0)))
        yi = shape_coordinates[1] + math.ceil((poly_radius * math.cos( (i * internal_angle)+ internal_angle / 2.0)))
         
        point_pair = (xi, yi)
         
        # push new point on to vertex list
        vertices.append( point_pair )
        
    # draw this polygon on to the stimulus image
    
    # make the vertices list a tuple
    vertex_list = tuple(vertices) 
    print(vertex_list)
#    print(shape_info["name"])
    stim.polygon(vertex_list, fill = shape_info["colour"], outline = shape_info["colour"])
         
    return()


# def write_AOIs(coord_list, shape_:
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
