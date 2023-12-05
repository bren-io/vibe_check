#---------------------------
# This script uses the pandas module to produce graphical representations of the files in /data
#
#
#------------------------------------------

import pandas
import json

def json_to_pandas(json_data):
    try:
        df = pandas.DataFrame([json_data])
        return df

    except Exception as e:
        print(f"Error: {e}")
