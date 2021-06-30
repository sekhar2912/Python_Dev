#!/usr/bin/python   
from __future__ import division
import json
import os
import cv2 as cv
import numpy as np
import getopt, sys
from random import randint

W = 600
rook_window = "Drawing : Canvas"
size = W, W, 3

counter = 0
grp_col_dict = {}
out_put_dict ={}
uniqueVehType = {}

#------ Spl Category-----

splCtg = {  'Person',
            'Pusher',
            'Moving_Trolley',
            'Rider',
            'Moving_Bicycle',
            'Moving_Motorcycle',
            'Moving_Personal_Mobility_Device',
            'Car',
            'Truck',
            'Animal',
            'Robot',
            'SUV'
            
         }
# Static Data #
dict_of_colorCodes = {
          'Sedan':(93,71,139),
          'SUV':(147,112,219),
          'Pickup':(102,154,255),
          'Van':(255,15,215),
          'Truck':(110,175,230),
          'Bus':(235,120,22),
          'Other':(195,155,10),
          'Ignore':(255,192,203),
          'Object':(110,175,230),
          'Road_Marking':(0,255,0),
          'Person':(0,255,255),
          'General_Obstacle' : (128, 64, 128),
          'Barrier_Arm' : (80, 171, 190),
          'Soft_Branches_Near_Footpath' :(134, 141, 185), 
          'Footpath_Or_Floor' : (0, 255, 0), 
          'Grass_Or_Dirt' : (170, 145, 29),
          'Driveway' : (102, 102, 0),
          'Road' : (250, 0, 0),
          'Traffic_Light_Crossing' : (78, 66, 245),
          'Zebra_Crossing' : (243, 250, 42),
          'Speed_Bump' : (219, 209, 212),
          'Grate' : (76, 39, 146),
          'Tactile_Grid' : (240, 213, 169),
          
}


color_codes_set = {
            (93,71,139),
            (147,112,219),
            (102,154,255),
            (255,15,215),
            (110,175,230),
            (235,120,22),
            (195,155,10),
            (255,192,203),
            (110,175,230),
            # (0,255,255),
            (128, 64, 128),
            (80, 171, 190),
            (134, 141, 185), 
            (0, 255, 0), 
            (170, 145, 29),
            (102, 102, 0),
            (250, 0, 0),
            (78, 66, 245),
            (243, 250, 42),
            (219, 209, 212),
            (76, 39, 146),
            (240, 213, 169)
 }

def difference_two_dict(dictfst,distSec):
    flen =len(dictfst)
    slen =len(distSec)
    if flen > slen:
       return set(dictfst) - set(distSec)
    elif  slen > flen:  
       return set(distSec) - set(dictfst)
    else:
        return {}
    
def dump_output_json(dictionary,fileName):
    with open(fileName, "w") as outfile: 
        json.dump(dictionary,outfile,indent=4,sort_keys=False)

def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i+lv//3], 16) for i in range(0, lv, lv//3))

def create_blank(width, height, rgb_color=(0, 0, 0)):
    """Create new image(numpy array) filled with certain color in RGB"""
    image = np.zeros((height, width, 3), np.uint8)
    color = tuple(reversed(rgb_color))
    image[:] = color
    return image

def draw_polygon(img,ppt,clr = (205, 92, 92)):
    line_type = 8
    isClosed = True
    thickness = 0
    bColor = (0, 0,2550) # blue
    ppt = ppt.reshape((-1, 1, 2))
    cv.fillPoly(img, [ppt], clr, line_type)
    # cv.polylines(img, [ppt], 
    #                   isClosed, bColor, thickness)

def generateOutputJsonDict(uniqueVehType):

    lvalue = {}

    # Creating inside info for "labelMapping" dictionary
    for e in uniqueVehType:
        global counter
        templist = []
        for val in uniqueVehType[e]:
            tempDict = {}
            counter = counter + 1
            tempDict['index'] = counter
            tempDict['color'] = rgb_to_hex(val)
            tempDict['attributes'] = 'null'
            templist.append(tempDict)
        lvalue[e] = templist
  
    emptyList = difference_two_dict(dict_of_colorCodes,uniqueVehType)
    for element in emptyList:
        lvalue[element] = []

    # Creating annotations dictionary


    tmplabeledVal = {
        "road": "null",
        "driveway": "null",
        "zebra_crossing":"null",
        "traffic_light_crossing": "null",
        "tactile_grid": "null",
        "fence": "null",
        "footpath_or_floor": "null",
        "general_obstacle": "null",
        "soft_branches_near_footpath": "null",
        "grass_or_dirt": "null",
        "grate": "null",
        "speed_bump": "null",
        "water_puddle": "null",
        "barrier_arm": "null",
        "glass_wall": "null",
        "door_glass": "null",
        "door_non_glass": "null",
        "table_and_chair": "null",
        "sky": "null",
        "car": 
        [
            "null",
            "null",
            "null"
        ],
        "person": "[]",
        "trolley": "[]",
        "animal": "[]",
        "truck": 
        [
            "null.png",
            "null.png"
        ],
        "personal_mobility_device": "[]",
        "cyclist": "[]",
        "motorcyclist": "[]",
        "robot": "[]"
        }

    annotations = {}
    annotations["combined"] = {
                                "image": "null.png",
                                "indexedImage": "null.png"
                                }
    annotations["labeled"] = tmplabeledVal
    annotations["unlabeled"] = "null"
    out_put_dict["annotations"] = annotations
    out_put_dict["labelMapping"] = lvalue
    out_put_list = []
    out_put_list.append(out_put_dict)

    return out_put_list

def getArg():
    return sys.argv[1]

#The below func add_values_in_dict is not used . It is for future work
def add_values_in_dict(sample_dict, key, list_of_values):
    """Append multiple values to a key in the given dictionary"""
    if key not in sample_dict:
        sample_dict[key] = list()
    sample_dict[key].extend(list_of_values)
    return sample_dict

def nextColor():
    return (randint(10, 255), 
            randint(50, 255), 
            randint(100, 255))

def groupIdPair(data):
    gr_Id = {}
    for elm in data:
        for poly in elm['polygons']:
            grpId = poly['GroupID']
            if grpId not in gr_Id:
                gr_Id[grpId] = poly['ID']
            else:
                tset = {gr_Id[grpId]}
                tset.add(poly['ID'])
                gr_Id[grpId] = tset
    dup = {}
    for ele in gr_Id:
        if not isinstance(gr_Id[ele],int) and ele != -1:
            dup[ele] = gr_Id[ele]
    return dup

def main():
    black = (0,0,0)
    image = create_blank(W, W, rgb_color=black)
    gr_Id = {}
    fileNameArg = getArg()
    dirname = os.path.dirname(__file__)
    fileDir = os.path.join(dirname, 'data')
    filename = os.path.join(fileDir, fileNameArg)
    f = open(filename,)
    rook_image = np.zeros(size, dtype=np.uint8)
    data = json.load(f)

    gr_Id = groupIdPair(data)   
    for element in data:
        out_put_dict['image_name'] = element['ImageID']
        for poly in element['polygons']:
            if poly['GroupID'] not in  gr_Id:
                id = poly['ID']
                grpId = poly['GroupID']
                clss = poly['class']
                vehType = poly['vehicle_type']
                crdArray = poly['Coordinates']
                reduceArray = [[item / 8 for item in subl] for subl in crdArray]
    
                if grpId not in grp_col_dict and grpId > 0:
      
                    grp_col_dict[grpId] = dict_of_colorCodes.get(vehType)
                ppt = np.array(reduceArray, np.int32)
                    
                if vehType in dict_of_colorCodes:
                    clr = set()
                    el = set() 
                    if vehType in splCtg:
                        if vehType in uniqueVehType.keys():
                           grp_col_dict.pop(grpId)

                    if grpId in grp_col_dict :
                        clr.add(grp_col_dict.get(grpId)) 
                    elif vehType in splCtg: 
                        el = uniqueVehType[vehType]
                        while (True):
                            newClr = nextColor()
                            if newClr not in color_codes_set:
                                color_codes_set.add(newClr)
                                el.add(newClr)
                                clr = el
                                break
                    else:
                        clr.add(dict_of_colorCodes.get(vehType))
                uniqueVehType[vehType] = clr

                draw_polygon(image,ppt,max(clr))
        
        gc ={}
        final_id ={}
        for ele in gr_Id:
            temp = gr_Id[ele]
            clr = (0,0,0)
            counter = 0
            for id in temp:
                if counter == 0:
                    for poly in element['polygons']:
                        if id == poly['GroupID'] :
                            vehType = poly['vehicle_type']
                            if vehType not in splCtg:
                                clr = dict_of_colorCodes[vehType]
                                counter = counter + 1
                            else:
                                while (True):
                                    newClr = nextColor()
                                    t_set = uniqueVehType[vehType]
                                    while newClr in t_set:
                                         newClr = nextColor()
                                    if newClr not in color_codes_set and newClr != (0,0,0):
                                        clr = newClr
                                        counter = counter + 1
                                        t_set.add(newClr)
                                        break
            gc[ele]=clr

        for poly_new in element['polygons']: 
            for grId in gc:
                if grId == poly_new['GroupID']:
                    crdArray = poly_new['Coordinates']
                    reduceArray1 = [[item / 8 for item in subl] for subl in crdArray]
                    ppt1 = np.array(reduceArray1, np.int32)
                    draw_polygon(image,ppt1,gc[grId])
        
       
    f.close()
    outfilename = os.path.join(dirname, 'data/Output_file.json')
    outImagename = os.path.join(dirname, 'data/OutImage.jpg')
    dump_output_json(generateOutputJsonDict(uniqueVehType),outfilename)
    cv.imshow(rook_window, image)
    cv.imwrite(outImagename, image)
    cv.moveWindow(rook_window, W, 200)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
   