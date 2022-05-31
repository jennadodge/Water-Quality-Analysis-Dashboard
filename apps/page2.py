from dash import Dash, dcc, Output, Input, html  
import dash_bootstrap_components as dbc    
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd                       
import pathlib


# Add a title
title=("Water Quality Analysis")    

#read in data
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()
df = pd.read_csv(DATA_PATH.joinpath('new_priority_by_fips.csv'))

#add graphs

fig1 = px.scatter(
    df, 
    x="Simpson_Ethnic_DI", 
    y="Sum_ContaminantFactor", 
    color="Label",
    size='Num_Contaminants', 
    hover_data=['Sum_ContaminantFactor'],
    labels={
        "Sum_ContaminantFactor": "Total Conataminant Factor",
        "Simpson_Ethnic_DI" : " Simpson Ethnic Index"
                     
            },
)

fig1.update_layout(
    title={
        'text': "Plot of the Adaboost Top Feature Importance",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})

fig2 = px.scatter(
    df, 
    x="Shannon_Race_DI", 
    y="Sum_ContaminantFactor", 
    color="Label",
    size='Num_Contaminants', 
    hover_data=['Sum_ContaminantFactor'],
    labels={
        "Sum_ContaminantFactor": "Total Conataminant Factor",
        "Shannon_Race_DI" : " Shannon Race Index"
                     
            },
)

fig2.update_layout(
    title={
        'text': "Plot of the Adaboost Top Feature Importance",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})

# layout

layout = dbc.Container([
    
    dbc.Row([
        dbc.Col([
            html.H4("Supervised Machine Learning - Binary Classification"),
            html.Li("To have a target for ML models to predict an algorithm had to be developed"
                    " to establish the weights of the features and determine a final priority "
                    "level. In the case of the binary classification models, this target is a high-priority"
                    " (1) or low-priority (0).",className='class-text mb-3'),
            html.Li("We developed an algorithm to establish a high priority target if the Total Contaminant "
                    "Factor was greater than the median and if several other feature values were also greater "
                    "than the median.",className='class-text mb-5'),

        ], xs=12, sm=12, md=12, lg=6, xl=6),
        dbc.Col([
            # html.P("Row 1 column 2"),
            dbc.Card(
                dbc.CardBody([
                    html.H4("The top features of our model according to Random Forest Classification:",className='card-title text-center mb-3'),
                    dbc.CardImg(src="/assets/feature_classification.png",top=False,bottom=True)],
                    className="card text-white bg-secondary")
                , className='mb-5')

        ], xs=12, sm=12, md=12, lg=6, xl=6)
    ], justify="evenly"),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Simpson Ethnic Diversity Index vs Total Contaminant Factor",className='card-header text-center'),
                dbc.CardBody(
                    dcc.Graph('scatter-1',figure=fig1)
                )
            ], className='mb-5'),

        ], xs=12, sm=12, md=12, lg=6, xl=6),

        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Shannon Race Diversity Index vs. Total Contaminant Factor",className='card-header text-center'),
                dbc.CardBody(
                    # html.P("card"),
                    dcc.Graph('scatter-2',figure=fig2)
                )
            ], className='mb-5'),

        ], xs=12, sm=12, md=12, lg=6, xl=6),
    ], justify="evenly"),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Feature Distributions Colored by Priority Target (High or Low)",className='card-header text-center'),
                dbc.CardImg(src='/assets/feature_pairplot.png',top=True, bottom=False,
                    title="Feature Pairplot", alt='Feature Pairplot')

            ], className='mb-5'),


        ], xs=12, sm=12, md=12, lg=6, xl=6),
        dbc.Col([
            dbc.Card(
                dbc.CardBody([
                    html.H5("The top-performing Binary Classification models were the Balanced Random "
                        "Forest Classifier with 98% accuracy and the Easy Ensemble Adaboost Classifier "
                        "with 97% accuracy.",
                        className="card-subtitle mb-3 text-center"),
                    html.H5("Balanced Random Forest Classifier:"),
                    dbc.CardImg(src="/assets/BRFC_accuracy.png",top=True,bottom=False, 
                    className='mb-3'),
                    html.H5("Adaboost Easy Ensemble Classifier:"),
                    dbc.CardImg(src="/assets/Adaboost_accuracy.png",top=False,bottom=True,
                    className='mb-3')
                ], 
            ), className="card text-white bg-secondary mb-3"
            ),

        ], xs=12, sm=12, md=12, lg=6, xl=6),
    ], justify="evenly")

])

