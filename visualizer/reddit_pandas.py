# Create visual representation of sentiments for a post

import os
import pandas as pd
from json_helper import reddit_worker
import matplotlib.pyplot as plt

def get_graph(vibe_dir, plot_dir):
    file_list = os.listdir(vibe_dir)

    for file_name in file_list:
        if file_name.endswith(".json"):
            file_path = os.path.join(vibe_dir, file_name)
            json_data = reddit_worker.read_json(file_path)
            df = json_to_pandas(json_data)

            if df is not None:
                vibe_count = df.loc[0].value_counts()

                # Reset graph
                plt.clf()

                vibe_str = [str(vibe) for vibe in vibe_count.index]
                
                # Plot the data frame
                plt.bar(vibe_str, vibe_count.values)
                plt.xlabel('Sentiments')
                plt.ylabel('Count')
                plt.title(f'{file_name.replace("reddit_r_", "").replace("comments_", "").replace("_sentiment.json", "")}')
                plt.savefig(f'{plot_dir}/{file_name.replace(".json", ".png")}')

def json_to_pandas(json_data):
    try:
        df = pd.DataFrame([json_data])
        return df

    except Exception as e:
        print(f"Error: {e}")
