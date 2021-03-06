import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from dash.exceptions import PreventUpdate
import pandas as pd
from datetime import datetime


app = dash.Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}])

app.layout = html.Div([
    html.Div([
        dcc.Interval(id = 'update_title_background_image',
                     interval = 30000,
                     n_intervals = 0),
    ]),
    html.Div([
        dcc.Interval(id = 'update_header_content',
                     interval = 1000,
                     n_intervals = 0),
    ]),

    html.Div(id = 'title_background_image'),
    html.Div([
        html.Img(src = app.get_asset_url('cloudy.png'),
                 style = {'height': '27px'},
                 ),
        html.P('Weather Data',
               style = {'color': 'white',
                        'margin-top': '10px'},
               ),
    ], className = 'title'),

    html.Div(id = 'header_content'),
    html.Div(id = 'main_background_image',
             className = 'main_background_image'),
    html.Div([
        html.Div([
            html.Div(id = 'temperature_card',
                     className = 'adjust_temperature_card'
                     ),
            html.Div(id = 'humidity_card',
                     className = 'adjust_humidity_card'
                     ),
            html.Div(id = 'wind_card',
                     className = 'adjust_wind_card'
                     )
        ], className = 'flexbox_container'),
    ], className = 'adjust_margin'),

    html.Div([
        html.Div([
            html.Div(id = 'weather_forecast1',
                     className = 'adjust_forecast_card1'),
            html.Div(id = 'weather_forecast2',
                     className = 'adjust_forecast_card2'),
            html.Div(id = 'weather_forecast3',
                     className = 'adjust_forecast_card3')
        ], className = 'forecast_flexbox')
    ], className = 'forecast_container_margin'),

], id= "mainContainer",
   style={"display": "flex", "flex-direction": "column"})

@app.callback(Output('weather_forecast3', 'children'),
              [Input('update_header_content', 'n_intervals')])
def header(n_intervals):
    header_list = ['Time', 'Humidity', 'Temperature', 'Rain', 'Sun Set', 'Sun Rise', 'Wind Speed']
    df = pd.read_csv('weather_data.csv', names = header_list)
    get_temp = df['Temperature'].tail(1).iloc[0].astype(float)
    get_temp_fahr = (get_temp * 9/5) + 32
    now = datetime.now()
    day = now.strftime('%a')
    date = now.strftime('%d/%m/%Y')
    time = now.strftime('%H:%M:%S')
    sun_rise = '06:36'
    sun_set = '19:34'
    if n_intervals == 0:
        raise PreventUpdate

    if get_temp > 21:
        return [
                html.P('Worcester, United Kingdom',
                       style = {'color': 'black',},
                       ),
        ]
    elif get_temp < 21:
        return [
            html.Div([
                html.Div([
                    html.P('16:00',
                           style = {'color': 'white',
                                    'fontSize': 15,
                                    },
                           className = 'time_forecast'
                           ),
                    html.Img(src = app.get_asset_url('gif-rain-cloud-unscreen.gif'),
                             style = {'height': '40px',
                                      'width': '40px'
                                      },
                             className = 'gif_forecast'
                             ),
                    html.P('{0:,.0f}??C'.format(get_temp),
                           style = {'color': 'white',
                                    'fontSize': 15,
                                    },
                           className = 'temperature_forecast'
                           ),
                ], className = 'column_forecast'),
                html.Div([
                    html.P('17:00',
                           style = {'color': 'white',
                                    'fontSize': 15,
                                    },
                           className = 'time_forecast'
                           ),
                    html.Img(src = app.get_asset_url('gif-rain-cloud-unscreen.gif'),
                             style = {'height': '40px',
                                      'width': '40px'
                                      },
                             className = 'gif_forecast'
                             ),
                    html.P('{0:,.0f}??C'.format(get_temp),
                           style = {'color': 'white',
                                    'fontSize': 15,
                                    },
                           className = 'temperature_forecast'
                           ),
                ], className = 'column_forecast'),
                html.Div([
                    html.P('18:00',
                           style = {'color': 'white',
                                    'fontSize': 15,
                                    },
                           className = 'time_forecast'
                           ),
                    html.Img(src = app.get_asset_url('gif-rain-cloud-unscreen.gif'),
                             style = {'height': '40px',
                                      'width': '40px'
                                      },
                             className = 'gif_forecast'
                             ),
                    html.P('{0:,.0f}??C'.format(get_temp),
                           style = {'color': 'white',
                                    'fontSize': 15,
                                    },
                           className = 'temperature_forecast'
                           ),
                ], className = 'column_forecast'),
                html.Div([
                    html.P('19:00',
                           style = {'color': 'white',
                                    'fontSize': 15,
                                    },
                           className = 'time_forecast'
                           ),
                    html.Img(src = app.get_asset_url('gif-rain-cloud-unscreen.gif'),
                             style = {'height': '40px',
                                      'width': '40px'
                                      },
                             className = 'gif_forecast'
                             ),
                    html.P('{0:,.0f}??C'.format(get_temp),
                           style = {'color': 'white',
                                    'fontSize': 15,
                                    },
                           className = 'temperature_forecast'
                           ),
                ], className = 'column_forecast'),
                html.Div([
                    html.P('20:00',
                           style = {'color': 'white',
                                    'fontSize': 15,
                                    },
                           className = 'time_forecast'
                           ),
                    html.Img(src = app.get_asset_url('gif-rain-cloud-unscreen.gif'),
                             style = {'height': '40px',
                                      'width': '40px'
                                      },
                             className = 'gif_forecast'
                             ),
                    html.P('{0:,.0f}??C'.format(get_temp),
                           style = {'color': 'white',
                                    'fontSize': 15,
                                    },
                           className = 'temperature_forecast'
                           ),
                ], className = 'column_forecast'),
                html.Div([
                    html.P('21:00',
                           style = {'color': 'white',
                                    'fontSize': 15,
                                    },
                           className = 'time_forecast'
                           ),
                    html.Img(src = app.get_asset_url('gif-rain-cloud-unscreen.gif'),
                             style = {'height': '40px',
                                      'width': '40px'
                                      },
                             className = 'gif_forecast'
                             ),
                    html.P('{0:,.0f}??C'.format(get_temp),
                           style = {'color': 'white',
                                    'fontSize': 15,
                                    },
                           className = 'temperature_forecast'
                           ),
                ], className = 'column_forecast'),
                html.Div([
                    html.P('22:00',
                           style = {'color': 'white',
                                    'fontSize': 15,
                                    },
                           className = 'time_forecast'
                           ),
                    html.Img(src = app.get_asset_url('gif-rain-cloud-unscreen.gif'),
                             style = {'height': '40px',
                                      'width': '40px'
                                      },
                             className = 'gif_forecast'
                             ),
                    html.P('{0:,.0f}??C'.format(get_temp),
                           style = {'color': 'white',
                                    'fontSize': 15,
                                    },
                           className = 'temperature_forecast'
                           ),
                ], className = 'column_forecast'),
                html.Div([
                    html.P('23:00',
                           style = {'color': 'white',
                                    'fontSize': 15,
                                    },
                           className = 'time_forecast'
                           ),
                    html.Img(src = app.get_asset_url('gif-rain-cloud-unscreen.gif'),
                             style = {'height': '40px',
                                      'width': '40px'
                                      },
                             className = 'gif_forecast'
                             ),
                    html.P('{0:,.0f}??C'.format(get_temp),
                           style = {'color': 'white',
                                    'fontSize': 15,
                                    },
                           className = 'temperature_forecast'
                           ),
                ], className = 'column_forecast'),

            ], className = 'row_forecast'),

        ]

@app.callback(Output('weather_forecast2', 'children'),
              [Input('update_header_content', 'n_intervals')])
def header(n_intervals):
    header_list = ['Time', 'Humidity', 'Temperature', 'Rain', 'Sun Set', 'Sun Rise', 'Wind Speed']
    df = pd.read_csv('weather_data.csv', names = header_list)
    get_temp = df['Temperature'].tail(1).iloc[0].astype(float)
    get_temp_fahr = (get_temp * 9/5) + 32
    now = datetime.now()
    day = now.strftime('%a')
    date = now.strftime('%d/%m/%Y')
    time = now.strftime('%H:%M:%S')
    sun_rise = '06:36'
    sun_set = '19:34'
    if n_intervals == 0:
        raise PreventUpdate

    if get_temp > 21:
        return [
                html.P('Worcester, United Kingdom',
                       style = {'color': 'black',},
                       ),
        ]
    elif get_temp < 21:
        return [
            html.Div([
                html.Div([
                    html.P('08:00',
                           style = {'color': 'white',
                                    'fontSize': 15,
                                    },
                           className = 'time_forecast'
                           ),
                    html.Img(src = app.get_asset_url('gif-rain-cloud-unscreen.gif'),
                             style = {'height': '40px',
                                      'width': '40px'
                                      },
                             className = 'gif_forecast'
                             ),
                    html.P('{0:,.0f}??C'.format(get_temp),
                           style = {'color': 'white',
                                    'fontSize': 15,
                                    },
                           className = 'temperature_forecast'
                           ),
                ], className = 'column_forecast'),

                html.Div([
                    html.P('09:00',
                           style = {'color': 'white',
                                    'fontSize': 15,
                                    },
                           className = 'time_forecast'
                           ),
                    html.Img(src = app.get_asset_url('gif-rain-cloud-unscreen.gif'),
                             style = {'height': '40px',
                                      'width': '40px'
                                      },
                             className = 'gif_forecast'
                             ),
                    html.P('{0:,.0f}??C'.format(get_temp),
                           style = {'color': 'white',
                                    'fontSize': 15,
                                    },
                           className = 'temperature_forecast'
                           ),
                ], className = 'column_forecast'),
                html.Div([
                    html.Div([
                        html.P('Now',
                               style = {'color': 'white',
                                        'fontSize': 15,
                                        },
                               className = 'time_forecast'
                               ),
                        html.Img(src = app.get_asset_url('gif-rain-cloud-unscreen.gif'),
                                 style = {'height': '40px',
                                          'width': '40px'
                                          },
                                 className = 'gif_forecast'
                                 ),
                        html.P('{0:,.0f}??C'.format(get_temp),
                               style = {'color': 'white',
                                        'fontSize': 15,
                                        },
                               className = 'temperature_forecast'
                               ),
                    ], className = 'column_forecast', style = {'margin-left': '5px'}),
                ], style = {'background-color': 'black',
                            'height': '150px',
                            'margin-top': '-25px',
                            'width': '50px'}),
                html.Div([
                    html.P('11:00',
                           style = {'color': 'white',
                                    'fontSize': 15,
                                    },
                           className = 'time_forecast'
                           ),
                    html.Img(src = app.get_asset_url('gif-rain-cloud-unscreen.gif'),
                             style = {'height': '40px',
                                      'width': '40px'
                                      },
                             className = 'gif_forecast'
                             ),
                    html.P('{0:,.0f}??C'.format(get_temp),
                           style = {'color': 'white',
                                    'fontSize': 15,
                                    },
                           className = 'temperature_forecast'
                           ),
                ], className = 'column_forecast'),
                html.Div([
                    html.P('12:00',
                           style = {'color': 'white',
                                    'fontSize': 15,
                                    },
                           className = 'time_forecast'
                           ),
                    html.Img(src = app.get_asset_url('gif-rain-cloud-unscreen.gif'),
                             style = {'height': '40px',
                                      'width': '40px'
                                      },
                             className = 'gif_forecast'
                             ),
                    html.P('{0:,.0f}??C'.format(get_temp),
                           style = {'color': 'white',
                                    'fontSize': 15,
                                    },
                           className = 'temperature_forecast'
                           ),
                ], className = 'column_forecast'),
                html.Div([
                    html.P('13:00',
                           style = {'color': 'white',
                                    'fontSize': 15,
                                    },
                           className = 'time_forecast'
                           ),
                    html.Img(src = app.get_asset_url('gif-rain-cloud-unscreen.gif'),
                             style = {'height': '40px',
                                      'width': '40px'
                                      },
                             className = 'gif_forecast'
                             ),
                    html.P('{0:,.0f}??C'.format(get_temp),
                           style = {'color': 'white',
                                    'fontSize': 15,
                                    },
                           className = 'temperature_forecast'
                           ),
                ], className = 'column_forecast'),
                html.Div([
                    html.P('14:00',
                           style = {'color': 'white',
                                    'fontSize': 15,
                                    },
                           className = 'time_forecast'
                           ),
                    html.Img(src = app.get_asset_url('gif-rain-cloud-unscreen.gif'),
                             style = {'height': '40px',
                                      'width': '40px'
                                      },
                             className = 'gif_forecast'
                             ),
                    html.P('{0:,.0f}??C'.format(get_temp),
                           style = {'color': 'white',
                                    'fontSize': 15,
                                    },
                           className = 'temperature_forecast'
                           ),
                ], className = 'column_forecast'),
                html.Div([
                    html.P('15:00',
                           style = {'color': 'white',
                                    'fontSize': 15,
                                    },
                           className = 'time_forecast'
                           ),
                    html.Img(src = app.get_asset_url('gif-rain-cloud-unscreen.gif'),
                             style = {'height': '40px',
                                      'width': '40px'
                                      },
                             className = 'gif_forecast'
                             ),
                    html.P('{0:,.0f}??C'.format(get_temp),
                           style = {'color': 'white',
                                    'fontSize': 15,
                                    },
                           className = 'temperature_forecast'
                           ),
                ], className = 'column_forecast'),

            ], className = 'row_forecast'),

        ]

@app.callback(Output('weather_forecast1', 'children'),
              [Input('update_header_content', 'n_intervals')])
def header(n_intervals):
    header_list = ['Time', 'Humidity', 'Temperature', 'Rain', 'Sun Set', 'Sun Rise', 'Wind Speed']
    df = pd.read_csv('weather_data.csv', names = header_list)
    get_temp = df['Temperature'].tail(1).iloc[0].astype(float)
    get_temp_fahr = (get_temp * 9/5) + 32
    now = datetime.now()
    day = now.strftime('%a')
    date = now.strftime('%d/%m/%Y')
    time = now.strftime('%H:%M:%S')
    sun_rise = '06:36'
    sun_set = '19:34'
    if n_intervals == 0:
        raise PreventUpdate

    if get_temp > 21:
        return [
                html.P('Worcester, United Kingdom',
                       style = {'color': 'black',},
                       ),
        ]
    elif get_temp < 21:
        return [
            html.Div([
            html.Div([
            html.P('00:00',
                   style = {'color': 'white',
                            'fontSize': 15,
                            },
                   className = 'time_forecast'
                   ),
            html.Img(src = app.get_asset_url('gif-rain-cloud-unscreen.gif'),
                     style = {'height': '40px',
                              'width': '40px'
                              },
                     className = 'gif_forecast'
                     ),
                html.P('{0:,.0f}??C'.format(get_temp),
                       style = {'color': 'white',
                                'fontSize': 15,
                                },
                       className = 'temperature_forecast'
                       ),
                ], className = 'column_forecast'),
                html.Div([
                    html.P('01:00',
                           style = {'color': 'white',
                                    'fontSize': 15,
                                    },
                           className = 'time_forecast'
                           ),
                    html.Img(src = app.get_asset_url('gif-rain-cloud-unscreen.gif'),
                             style = {'height': '40px',
                                      'width': '40px'
                                      },
                             className = 'gif_forecast'
                             ),
                    html.P('{0:,.0f}??C'.format(get_temp),
                           style = {'color': 'white',
                                    'fontSize': 15,
                                    },
                           className = 'temperature_forecast'
                           ),
                ], className = 'column_forecast'),
                html.Div([
                    html.P('02:00',
                           style = {'color': 'white',
                                    'fontSize': 15,
                                    },
                           className = 'time_forecast'
                           ),
                    html.Img(src = app.get_asset_url('gif-rain-cloud-unscreen.gif'),
                             style = {'height': '40px',
                                      'width': '40px'
                                      },
                             className = 'gif_forecast'
                             ),
                    html.P('{0:,.0f}??C'.format(get_temp),
                           style = {'color': 'white',
                                    'fontSize': 15,
                                    },
                           className = 'temperature_forecast'
                           ),
                ], className = 'column_forecast'),
                html.Div([
                    html.P('03:00',
                           style = {'color': 'white',
                                    'fontSize': 15,
                                    },
                           className = 'time_forecast'
                           ),
                    html.Img(src = app.get_asset_url('gif-rain-cloud-unscreen.gif'),
                             style = {'height': '40px',
                                      'width': '40px'
                                      },
                             className = 'gif_forecast'
                             ),
                    html.P('{0:,.0f}??C'.format(get_temp),
                           style = {'color': 'white',
                                    'fontSize': 15,
                                    },
                           className = 'temperature_forecast'
                           ),
                ], className = 'column_forecast'),
                html.Div([
                    html.P('04:00',
                           style = {'color': 'white',
                                    'fontSize': 15,
                                    },
                           className = 'time_forecast'
                           ),
                    html.Img(src = app.get_asset_url('gif-rain-cloud-unscreen.gif'),
                             style = {'height': '40px',
                                      'width': '40px'
                                      },
                             className = 'gif_forecast'
                             ),
                    html.P('{0:,.0f}??C'.format(get_temp),
                           style = {'color': 'white',
                                    'fontSize': 15,
                                    },
                           className = 'temperature_forecast'
                           ),
                ], className = 'column_forecast'),
                html.Div([
                    html.P('05:00',
                           style = {'color': 'white',
                                    'fontSize': 15,
                                    },
                           className = 'time_forecast'
                           ),
                    html.Img(src = app.get_asset_url('gif-rain-cloud-unscreen.gif'),
                             style = {'height': '40px',
                                      'width': '40px'
                                      },
                             className = 'gif_forecast'
                             ),
                    html.P('{0:,.0f}??C'.format(get_temp),
                           style = {'color': 'white',
                                    'fontSize': 15,
                                    },
                           className = 'temperature_forecast'
                           ),
                ], className = 'column_forecast'),
                html.Div([
                    html.P('06:00',
                           style = {'color': 'white',
                                    'fontSize': 15,
                                    },
                           className = 'time_forecast'
                           ),
                    html.Img(src = app.get_asset_url('gif-rain-cloud-unscreen.gif'),
                             style = {'height': '40px',
                                      'width': '40px'
                                      },
                             className = 'gif_forecast'
                             ),
                    html.P('{0:,.0f}??C'.format(get_temp),
                           style = {'color': 'white',
                                    'fontSize': 15,
                                    },
                           className = 'temperature_forecast'
                           ),
                ], className = 'column_forecast'),
                html.Div([
                    html.P('07:00',
                           style = {'color': 'white',
                                    'fontSize': 15,
                                    },
                           className = 'time_forecast'
                           ),
                    html.Img(src = app.get_asset_url('gif-rain-cloud-unscreen.gif'),
                             style = {'height': '40px',
                                      'width': '40px'
                                      },
                             className = 'gif_forecast'
                             ),
                    html.P('{0:,.0f}??C'.format(get_temp),
                           style = {'color': 'white',
                                    'fontSize': 15,
                                    },
                           className = 'temperature_forecast'
                           ),
                ], className = 'column_forecast'),

                ], className = 'row_forecast')

        ]

@app.callback(Output('wind_card', 'children'),
              [Input('update_header_content', 'n_intervals')])
def header(n_intervals):
    header_list = ['Time', 'Humidity', 'Temperature', 'Rain', 'Sun Set', 'Sun Rise', 'Wind Speed']
    df = pd.read_csv('weather_data.csv', names = header_list)
    wind_speed = '10 km/h'
    direction = 'North'
    air_quality = 'Excellent'
    pressure = '10134 mbar'
    if n_intervals == 0:
        raise PreventUpdate

    return [
        html.Div([
            html.Img(src = app.get_asset_url('CleanBareAmericanwirehair-max-1mb.gif'),
                     style = {'height': '125px',
                              },
                     className = 'turbine_image'
                     ),
            html.Div([
                html.Div([
                    html.Div([
                        html.P('Wind speed ',
                               style = {'color': 'white',
                                        'fontSize': 15,
                                        },
                               className = 'wind'
                               ),
                        html.P(wind_speed,
                               style = {'color': 'white',
                                        'fontSize': 15,
                                        },
                               className = 'speed'
                               ),
                    ], className = 'wind_speed'),
                    html.Div([
                        html.P('Direction ',
                               style = {'color': 'white',
                                        'fontSize': 15,
                                        },
                               className = 'direction'
                               ),
                        html.P(direction,
                               style = {'color': 'white',
                                        'fontSize': 15,
                                        },
                               className = 'direction_value'
                               ),

                    ], className = 'wind_direction'),

                ], className = 'wind_speed_direction'),

                html.Div([

                    html.Div([
                        html.P('Air Quality ',
                               style = {'color': 'white',
                                        'fontSize': 15,
                                        },
                               className = 'air'
                               ),
                        html.P(air_quality,
                               style = {'color': '#4AEC1E',
                                        'fontSize': 15,
                                        },
                               className = 'air_value'
                               ),

                    ], className = 'air_quality'),

                    html.Div([
                        html.P('Pressure ',
                               style = {'color': 'white',
                                        'fontSize': 15,
                                        },
                               className = 'pressure'
                               ),
                        html.P(pressure,
                               style = {'color': 'white',
                                        'fontSize': 15,
                                        },
                               className = 'pressure_value'
                               ),

                    ], className = 'air_pressure'),
                ], className = 'air_and_pressure')

            ], className = 'wind_content')
        ], className = 'image_wind'),

    ]

@app.callback(Output('humidity_card', 'children'),
              [Input('update_header_content', 'n_intervals')])
def header(n_intervals):
    header_list = ['Time', 'Humidity', 'Temperature', 'Rain', 'Sun Set', 'Sun Rise', 'Wind Speed']
    df = pd.read_csv('weather_data.csv', names = header_list)
    get_humi = df['Humidity'].tail(1).iloc[0].astype(float)
    if n_intervals == 0:
        raise PreventUpdate

    return [
        html.Div([
            html.Img(src = app.get_asset_url('wet.png'),
                     style = {'height': '50px'
                              },
                     className = 'wet_image'
                     ),
        html.Div([
            html.P('Humidity',
                   style = {'color': 'white',
                            'fontSize': 15,
                            },
                   className = 'humidity'
                   ),
            html.P('{0:,.0f}%'.format(get_humi),
                   style = {'color': 'white',
                            'fontSize': 60,
                            'font-weight': 'bold'
                            },
                   className = 'humidity_value'
                   ),
        ], className = 'humidity_value_flex'),

            ], className = 'humidity_wet_image')

    ]

@app.callback(Output('temperature_card', 'children'),
              [Input('update_header_content', 'n_intervals')])
def header(n_intervals):
    header_list = ['Time', 'Humidity', 'Temperature', 'Rain', 'Sun Set', 'Sun Rise', 'Wind Speed']
    df = pd.read_csv('weather_data.csv', names = header_list)
    get_temp = df['Temperature'].tail(1).iloc[0].astype(float)
    get_temp_fahr = (get_temp * 9/5) + 32
    now = datetime.now()
    day = now.strftime('%a')
    date = now.strftime('%d/%m/%Y')
    time = now.strftime('%H:%M:%S')
    sun_rise = '06:36'
    sun_set = '19:34'
    if n_intervals == 0:
        raise PreventUpdate

    if get_temp > 21:
        return [
                html.P('Worcester, United Kingdom',
                       style = {'color': 'black',},
                       ),
        ]
    elif get_temp < 21:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Div([
                            html.Div([
                                html.P('{0:,.0f}??C'.format(get_temp) + ' ' + '|' + ' ' + '{0:,.0f}??F'.format(
                                    get_temp_fahr),
                                       style = {'color': 'white',
                                                'fontSize': 15,
                                                },
                                       className = 'fahrenheit'
                                       ),
                                html.Div([
                                    html.P('{0:,.0f}'.format(get_temp),
                                           style = {'color': '#f4b701',
                                                    'fontSize': 60,
                                                    'font-weight': 'bold',
                                                    },
                                           ),
                                    html.Div([
                                        html.P('??C',
                                               style = {'color': 'white',
                                                        'fontSize': 25,
                                                        'margin-top': '15px',
                                                        },
                                               ),
                                        html.Img(src = app.get_asset_url('gif-rain-cloud-unscreen.gif'),
                                                 style = {'height': '40px',
                                                          },
                                                 className = 'gif_position'
                                                 ),
                                    ], className = 'gif_image')
                                ], className = 'temperature_row'),
                            ], className = 'fahrenheit_column'),

                            html.P('Rainy',
                                   style = {'color': 'white',
                                            'fontSize': 15,
                                            },
                                   className = 'status'
                                   ),
                        ], className = 'rainy_status'),

                        html.Div([
                            html.P(day + '.' + ' ' + date,
                                   style = {'color': 'white',
                                            'fontSize': 15,
                                            },
                                   className = 'date_time'
                                   ),
                            html.P(time,
                                   style = {'color': 'white',
                                            'fontSize': 25,
                                            'font-weight': 'bold',
                                            },
                                   className = 'time'
                                   ),
                        ], className = 'date_time_time')
                    ], className = 'date_time_row'),
                    html.Div([
                        html.Div([
                            html.P('Sun Rise: ',
                                   style = {'color': 'white',
                                            'fontSize': 15,
                                            },
                                   className = 'sun_rise'
                                   ),
                            html.P(sun_rise,
                                   style = {'color': '#f4b701',
                                            'fontSize': 20,
                                            'font_weight': 'bold'
                                            },
                                   className = 'rise_value'
                                   ),
                        ], className = 'sun_rise_value'),
                        html.Div([
                            html.P('Sun Set: ',
                                   style = {'color': 'white',
                                            'fontSize': 15,
                                            },
                                   className = 'sun_set'
                                   ),
                            html.P(sun_set,
                                   style = {'color': '#f4b701',
                                            'fontSize': 20,
                                            'font_weight': 'bold'
                                            },
                                   className = 'set_value'
                                   ),
                        ], className = 'sun_set_value')

                    ], className = 'sun'),
                ], className = 'sun_rise_set_column'),

                html.Div([
                    html.P('Max: ' + '{0:,.0f}??C'.format(get_temp),
                           style = {'color': 'white',
                                    'fontSize': 15,
                                    },
                           className = 'max'
                           ),
                    html.P('Min: ' + '{0:,.0f}??C'.format(get_temp),
                           style = {'color': 'white',
                                    'fontSize': 15,
                                    },
                           className = 'min'
                           ),
                ], className = 'max_min'),
            ], className = 'max_min_row'),

        ]

@app.callback(Output('main_background_image', 'children'),
              [Input('update_header_content', 'n_intervals')])
def update_graph(n_intervals):
    header_list = ['Time', 'Humidity', 'Temperature', 'Rain', 'Sun Set', 'Sun Rise', 'Wind Speed']
    df = pd.read_csv('weather_data.csv', names = header_list)
    get_temp = df['Temperature'].tail(1).iloc[0].astype(float)
    if n_intervals == 0:
        raise PreventUpdate

    if get_temp > 21:

     return [
        html.Div(style = {'background-image': 'url("/assets/sunny-day (1).jpg")',
                          'background-repeat': 'no-repeat',
                          'background-size': 'auto'
                          },
                 className = 'main_background_image'),
     ]

    elif get_temp < 21:
        return [
            html.Div(style = {'background-image': 'url("/assets/cloudy-day (2).jpg")',
                              'background-repeat': 'no-repeat',
                              'background-size': 'auto'
                              },
                     className = 'main_background_image'),

        ]

@app.callback(Output('header_content', 'children'),
              [Input('update_header_content', 'n_intervals')])
def header(n_intervals):
    header_list = ['Time', 'Humidity', 'Temperature', 'Rain', 'Sun Set', 'Sun Rise', 'Wind Speed']
    df = pd.read_csv('weather_data.csv', names = header_list)
    get_temp = df['Temperature'].tail(1).iloc[0].astype(float)
    if n_intervals == 0:
        raise PreventUpdate

    if get_temp > 21:
        return [
            html.Div([
                html.P('Worcester, United Kingdom',
                       style = {'color': 'white',
                                'margin-top': '10px'},
                       ),
                html.Div([
                    html.Img(src = app.get_asset_url('sunny.png'),
                             style = {'height': '27px'},
                             ),

                    html.P('{0:,.0f}??C'.format(get_temp),
                           style = {'color': 'white',
                                    'margin-top': '10px'},
                           ),
                ], className = 'adjust_header_content'),
            ], className = 'adjust_city_name'),
        ]
    elif get_temp < 21:
        return [
            html.Div([
                html.P('Worcester, United Kingdom',
                       style = {'color': 'white',
                                'margin-top': '10px'},
                       ),
                html.Div([
                    html.Img(src = app.get_asset_url('rain.png'),
                             style = {'height': '27px'},
                             ),
                    html.P('{0:,.0f}??C'.format(get_temp),
                           style = {'color': 'white',
                                    'margin-top': '10px'},
                           ),
                ], className = 'adjust_header_content'),
            ], className = 'adjust_city_name'),
        ]

@app.callback(Output('title_background_image', 'children'),
              [Input('update_title_background_image', 'n_intervals')])
def background_image(n_intervals):
    if n_intervals == None or n_intervals % 10 == 1:
        img = html.Div(style = {'background-image': 'url("/assets/1.jpg")',
                                'background-repeat': 'no-repeat',
                                'background-size': 'auto'
                                },
                       className = 'title_background_image'),
    elif n_intervals % 10 == 2:
        img = html.Div(style = {'background-image': 'url("/assets/2.jpg")',
                                'background-repeat': 'no-repeat',
                                'background-size': 'auto'
                                },
                       className = 'title_background_image'),
    elif n_intervals % 10 == 3:
        img = html.Div(style = {'background-image': 'url("/assets/3.jpg")',
                                'background-repeat': 'no-repeat',
                                'background-size': 'auto'
                                },
                       className = 'title_background_image'),
    elif n_intervals % 10 == 4:
        img = html.Div(style = {'background-image': 'url("/assets/4.jpg")',
                                'background-repeat': 'no-repeat',
                                'background-size': 'auto'
                                },
                       className = 'title_background_image'),
    elif n_intervals % 10 == 5:
        img = html.Div(style = {'background-image': 'url("/assets/5.jpg")',
                                'background-repeat': 'no-repeat',
                                'background-size': 'auto'
                                },
                       className = 'title_background_image'),
    elif n_intervals % 10 == 6:
        img = html.Div(style = {'background-image': 'url("/assets/6.jpg")',
                                'background-repeat': 'no-repeat',
                                'background-size': 'auto'
                                },
                       className = 'title_background_image'),
    elif n_intervals % 10 == 7:
        img = html.Div(style = {'background-image': 'url("/assets/7.jpg")',
                                'background-repeat': 'no-repeat',
                                'background-size': 'auto'
                                },
                       className = 'title_background_image'),
    elif n_intervals % 10 == 8:
        img = html.Div(style = {'background-image': 'url("/assets/8.jpg")',
                                'background-repeat': 'no-repeat',
                                'background-size': 'auto'
                                },
                       className = 'title_background_image'),
    elif n_intervals % 10 == 9:
        img = html.Div(style = {'background-image': 'url("/assets/9.jpg")',
                                'background-repeat': 'no-repeat',
                                'background-size': 'auto'
                                },
                       className = 'title_background_image'),
    elif n_intervals % 10 == 0:
        img = html.Div(style = {'background-image': 'url("/assets/10.jpg")',
                                'background-repeat': 'no-repeat',
                                'background-size': 'auto'
                                },
                       className = 'title_background_image'),
    else:
        img = "None"
    return img


if __name__ == '__main__':
    app.run_server(debug=False)
