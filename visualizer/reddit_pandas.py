# Create visual representation of sentiments for a post

import os
import pandas as pd
from json_helper import reddit_worker
import matplotlib.pyplot as plt

def get_graph(vibe_dir, plot_dir):
    file_list = os.listdir(vibe_dir)

    for file_name in file_list:
        try:
            if file_name.endswith(".json"):
                file_path = os.path.join(vibe_dir, file_name)
                df = pd.read_json(file_path)

                if df is not None:
                    vibe_count = df.loc[0].value_counts()
                
                    # Reset graph
                    plt.clf()
                
                    # Plot the data frame
                    plt.bar(vibe_count.index, vibe_count.values)
                    plt.xlabel('Sentiments')
                    plt.ylabel('Count')
                    plt.title(f'{file_name.replace("reddit_r_", "").replace("comments_", "").replace("_sentiment.json", "")}')
                    plt.savefig(f'{plot_dir}/{file_name.replace(".json", ".png")}')

        except Exception as e:
            print(f"Error: {e}")
