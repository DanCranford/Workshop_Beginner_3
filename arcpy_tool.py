#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def export_county_data(county_to_export, input_fc, output_folder, symbology_layer):
    '''
    This function creates a feature layer for a single county's highways.
    It exports that data into kmz and excel files.
    
    INPUTS:
    county_to_export : string - county which you would like to export
    input_fc : feature class - highway data with county attributed
    output_folder : string/folder path - folder where we want to create files
    symbology_layer : .lyr/.lyrx file - file with symbology stored for highways
    
    '''
    
    # create a new folder
    new_folder = arcpy.management.CreateFolder(output_folder, county_to_export)
    
    # generate a query for the data from the county input
    query = "NAMELSAD = '{}'".format(county_to_export)
    
    # create a feature layer for just the county we want
    flyr = arcpy.management.MakeFeatureLayer(input_fc, county_to_export, query)
    
    # add symbology to that feature layer
    arcpy.management.ApplySymbologyFromLayer(flyr, symbology_layer)
    
    # export kmz
    arcpy.conversion.LayerToKML(flyr, r'{}/{}/{} Highways.kmz'.format(output_folder, county_to_export, county_to_export))
    
    # export excel
    arcpy.conversion.TableToExcel(flyr, r'{}/{}/{} Highways.xls'.format(output_folder, county_to_export, county_to_export))
    
    return new_folder


# In[ ]:


import arcpy


# In[ ]:


county = arcpy.GetParameterAsText(0)
fc_intersect = arcpy.GetParameterAsText(1)
output_folder = arcpy.GetParameterAsText(2)
symbol_layer = arcpy.GetParameterAsText(3)


# In[ ]:





# In[ ]:


arcpy.AddMessage('Starting Export...')


# In[ ]:


export_county_data(county,
                   fc_intersect,
                   output_folder,
                   symbol_layer)

