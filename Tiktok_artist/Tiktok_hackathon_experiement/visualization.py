import plotly.express as px
import pandas as pd
import numpy as np
import plotly

def plot(counts,frequency):
    # Create a DataFrame from the counts list
    buckets = [f"{i*5+1}-{i*5+5}" for i in range(len(counts))]  # Generate bucket labels
    df = pd.DataFrame({'frequency_bucket': buckets, 'number_of_users': counts})

    fig = px.bar(df, x='frequency_bucket', y='number_of_users',
                title='User Analysis',
                labels={'frequency_bucket': f'{frequency}', 'number_of_users': 'Number of Users'},
                color='number_of_users',
                color_continuous_scale='RdPu',
                range_color=[0, max(counts)])

    dark_pink = 'rgb(219, 112, 147)'

    fig.update_layout(
        plot_bgcolor='black',  # Background color
        paper_bgcolor='black',
        font=dict(color=dark_pink),  # Text color
        title_font=dict(size=20, color=dark_pink, family="Arial"),
        xaxis=dict(title_font=dict(size=16, color=dark_pink, family="Arial"),
                tickfont=dict(size=14, color=dark_pink, family="Arial")),
        yaxis=dict(title_font=dict(size=16, color=dark_pink, family="Arial"),
                tickfont=dict(size=14, color=dark_pink, family="Arial"))
    )

    return fig

def plot2(counts):
    buckets = [f"{i}0"for i in range(1,11)]  # Generate bucket labels
    df = pd.DataFrame({'frequency_bucket': buckets, 'number_of_users': np.mean(counts, axis=1)})

    fig = px.bar(df, x='frequency_bucket', y='number_of_users',
                title='User Analysis',
                labels={'frequency_bucket': "percentage of song heard", 'number_of_users': 'Number of Users'},
                color='number_of_users',
                color_continuous_scale='RdPu',
                range_color=[0, max(np.mean(counts, axis = 1))])

    dark_pink = 'rgb(219, 112, 147)'

    fig.update_layout(
        plot_bgcolor='black',  # Background color
        paper_bgcolor='black',
        font=dict(color=dark_pink),  # Text color
        title_font=dict(size=20, color=dark_pink, family="Arial"),
        xaxis=dict(title_font=dict(size=16, color=dark_pink, family="Arial"),
                tickfont=dict(size=14, color=dark_pink, family="Arial")),
        yaxis=dict(title_font=dict(size=16, color=dark_pink, family="Arial"),
                tickfont=dict(size=14, color=dark_pink, family="Arial"))
    )
    return fig

