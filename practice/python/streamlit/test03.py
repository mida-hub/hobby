import streamlit as st
import plotly.express as px
import pandas as pd
import datetime
import os
from slack_sdk import WebClient

conditions_by_user = {}
conditions_for_df = {}

def set_page_config():
    st.set_page_config(layout="wide")

def fetch_data():
    return pd.read_csv('data/time_series.csv')

def set_conditions_by_user(df):
    start_date = datetime.datetime.strptime(min(df['date']), '%Y-%m-%d')
    end_date = datetime.datetime.strptime(max(df['date']), '%Y-%m-%d')

    conditions_by_user['start_date'] = start_date
    conditions_by_user['end_date'] = end_date
    
    return conditions_by_user

def main_page():
    st.title('Streamlit Practice')

def side_page(conditions_by_user):
    start_date = conditions_by_user['start_date']
    end_date = conditions_by_user['end_date']

    with st.sidebar:
        st.markdown("# Graph Condition")
        condition_start_date = st.date_input('start date', start_date)
        condition_end_date = st.date_input('end date', end_date)
        
        conditions_for_df['condition_start_date'] = condition_start_date
        conditions_for_df['condition_end_date'] = condition_end_date

        return conditions_for_df

def draw_graph(df, conditions_for_df):
    condition_start_date = conditions_for_df['condition_start_date']
    condition_end_date = conditions_for_df['condition_end_date']

    filtered_df = df
    filtered_df = filtered_df[(filtered_df['date'] >= str(condition_start_date))]
    filtered_df = filtered_df[(filtered_df['date'] <= str(condition_end_date))]

    fig = px.line(filtered_df, x='date', y='value', title='time series graph')
    st.write(fig)

    return fig

def send_to_slack(fig):
    client = WebClient(os.environ["SLACK_BOT_TOKEN"])
    image_path = "image/test03.png"
    fig.write_image(image_path)

    upload_text_file = client.files_upload(
                            channels='#github-actions',
                            title="graph.png",
                            file=image_path,
                            initial_comment="graph"
                        )

def side_page_action(fig):
    with st.sidebar:
        st.markdown("# Graph Send")
        # with open("image/test03.png", "rb") as file:
        #     btn = st.download_button(
        #             label="Download Image",
        #             data=file,
        #             file_name="graph.png",
        #             mime="image/png"
        #         )
        if st.button('To Slack'):
            send_to_slack(fig)

def main():
    params = st.experimental_get_query_params()
    set_page_config()
    df = fetch_data()
    conditions_by_user = set_conditions_by_user(df)
    main_page()
    conditions_for_df = side_page(conditions_by_user)
    fig = draw_graph(df, conditions_for_df)
    side_page_action(fig)

    if 'action' in params and 'send_to_slack' == params['action'][0]:
        send_to_slack(fig)

main()
