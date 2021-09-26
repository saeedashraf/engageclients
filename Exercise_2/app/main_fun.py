
import json
import pickle
import pandas as pd
import tensorflow as tf
from tensorflow import keras
import tensorflow_datasets as tfds
import tensorflow_recommenders as tfrs

## some codes for transforming are aadded here


def Convert(lst): 
    res_dct = {lst[i]: lst[i+1] for i in range (0, len(lst), 2)} 
    return res_dct

## ##



# During app's load
def execute (input_text_app):
    
    ...
    input_text = []
    input_text.append(input_text_app)
    
    
    # loading
    user_model = tf.keras.models.load_model('data/user_model')
    page_model = tf.keras.models.load_model('data/pagge_model')

    index.index_from_dataset(
      tf.data.Dataset.zip((pages.batch(100), pages.batch(100).map(model.page_model)))
    )

    # Get recommendations.
    _, page_name = index(tf.constant(["42"]))
    print(f"Recommendations for user 42: {page_name[0, :3]}")


    ## some codes for transforming are aadded here

    ## ##

    result ={
    "user_id": input_text_app[0],
    "os": input_text_app[1],
    "browser": input_text_app[2],
    "plan": input_text_app[3],
    "page": input_text_app[4],

    "top_3_results": [
        {
            "product_type": page_name[0]
        },
        {
            "product_type": page_name[1]
        },
        {
            "product_type": page_name[2]
        }
    ],
    "product_type": final_List_Top_Five[0]
    }
    
    finalJson = json.dumps(result)

    return finalJson

