import geopandas as gpd
import pandas as pd
import numpy as np
import plotly.express as px
from numpy import nan

def load_file (predicted_file_path):
    pred = pd.read_csv(predicted_file_path)
    return pred
location = '.\\Output_data\\NewPrediction.csv'

def plot_results():
    shp_csv = load_file(location)
    # import shape file
    gdf = gpd.read_file(r'E:\china_2nd\Open src\Proj\Github\Shape_files\eth_admbnda_adm2_csa_bofedb_2021.shp')
    shpcsv = shp_csv.loc[:,['Stations_Feature','Actual Day 1','Predicted Day 1']]

    # Mapping the stations name with shape file name
    Names = ['Addis ','Arba','Awassa ','Combolcha ','Dire','Debre',
            'Gondar','Gore','Jimma','Mekelle','Metehara ','Neghele','Nekemte','Robe']
    sh_name = ['Finfine Special','Gamo','Sidama','South Wello','Siti','East Gojam',
               'Central Gondar','Ilu Aba Bora','Jimma','South Eastern','East Shewa',
               'Guji','East Wellega','Bale']
    shpcsv['ADM2_EN'] = nan

    for rows in range(len(shpcsv)):
        for nm in range(len(Names)):
            if (Names[nm] in shpcsv.loc[rows,'Stations_Feature'] ):
                shpcsv.iloc[rows,shpcsv.columns.get_loc('ADM2_EN')] = sh_name[nm]
            else:
                continue

    # Chopping th feature
    features =  ['TMPMAX','TMPMIN'] #'PRECIP'
    for i in range(len(features)):
        feat = shpcsv.loc[shpcsv['Stations_Feature'].str.contains(features[i])]

        # Merging shapefile with the station predicted data
        Merging_shp = pd.merge(gdf[['ADM2_EN','ADM2_PCODE','geometry']],feat,on='ADM2_EN',how='left')
        Merging_shp.insert(0, 'index', range(0, len(Merging_shp)))
        Merging_shp.insert(0, 'New_ID', range(0, len(Merging_shp)))
        Merging_shp = Merging_shp.set_index('index')
        Merging_shp.crs="EPSG:4326"
        Merging_shp[['Actual Day 1','Predicted Day 1']]= Merging_shp[['Actual Day 1','Predicted Day 1']].fillna(0)

        # creating jason file 
        Merging_shp= Merging_shp.to_crs(epsg=4326)
        lag_json1 = Merging_shp.__geo_interface__

        # plotting Predicted data 
        fig = px.choropleth_mapbox(Merging_shp, geojson=lag_json1,locations='New_ID', color='Predicted Day 1',
                                color_continuous_scale="viridis",
                                range_color=(10, 35),
                                mapbox_style="carto-positron",
                                hover_name="Stations_Feature",
                                hover_data=["Predicted Day 1"],
                                zoom=3, center = {"lat": 14.433773, "lon": 48.625290},
                                opacity=0.5,
                                labels={'predicted':'P TMax'}
                                )
        
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0},
                          coloraxis_colorbar=dict(title="Pred " + str(features[i]) + "(°C)" ) ) 

        fig.show()

        fig = px.choropleth_mapbox(Merging_shp, geojson=lag_json1,locations='New_ID', color='Actual Day 1',
                                color_continuous_scale="viridis",
                                range_color=(10, 35),
                                mapbox_style="carto-positron",
                                hover_name="Stations_Feature",
                                hover_data=["Actual Day 1"],
                                zoom=3, center = {"lat": 14.433773, "lon": 48.625290},
                                opacity=0.5,
                                labels={'Actual':'A TMax'}
                                )
        
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0},
                          coloraxis_colorbar=dict(title="Actual " + str(features[i]) + "(°C)" )) 
        fig.show()


# def load_file (predicted_file_path):
#     pred = pd.read_csv(predicted_file_path)
# plot_results()
