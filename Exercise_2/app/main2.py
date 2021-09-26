
import json
import pickle
import pandas as pd
import tensorflow as tf
from tensorflow import keras


def Convert(lst): 
    res_dct = {lst[i]: lst[i+1] for i in range (0, len(lst), 2)} 
    return res_dct

# During app's load
def execute (input_text_app):
    
     
    input_text = []
    input_text.append(input_text_app)
    
    
    # loading
    new_model = tf.keras.models.load_model('data/')

    with open('data/tokenizer.pickle', 'rb') as handle:
        new_tokenizerTF = pickle.load(handle)
    
    with open('data/pad_sequences.pickle', 'rb') as pad_sequences1:
        new_pad_sequences = pickle.load(pad_sequences1)
        
    probability_new_model = tf.keras.Sequential([new_model, tf.keras.layers.Softmax()])



    max_length = 50
    trunc_type='post'
    padding_type='post'


    sequencesNew2 = new_tokenizerTF.texts_to_sequences(input_text)
    padded2 = new_pad_sequences(sequencesNew2, maxlen=max_length, padding=padding_type, truncating=trunc_type)
    predictions = probability_new_model.predict(padded2)


    final_df = pd.DataFrame(predictions.transpose(),  columns = ['Category'])
    topFive_df = final_df.nlargest(5, 'Category')

    prediction_Product_Type_Num= topFive_df.index.tolist()
    prediction_Product_Type_Probability = topFive_df.values.tolist()

    y4 = []
    for x in range(len(prediction_Product_Type_Probability)):
        y4.append(prediction_Product_Type_Probability[x][0])


    df_load = pd.read_pickle(open("data/corpus.pkl", "rb"))
    cols_target = df_load.productType.unique()

    y = cols_target

    listLabels = []
    for i, item in enumerate(y):
        listLabels.append(i)
        listLabels.append(item)
        
    dicLabelsUnique = Convert(listLabels)

    y5 = []
    y6 = []
    for i in range(len(prediction_Product_Type_Num)): 
        for x, xx in dicLabelsUnique.items():
            if prediction_Product_Type_Num[i] == x:
                y5.append(xx)
                y6.append(x)
                
    final_List_Top_Five = []
    for i in range(len(prediction_Product_Type_Num)):
        final_List_Top_Five.append(y5[i])
        final_List_Top_Five.append(y4[i])




    result ={
    "title": input_text_app,
    "top_5_results": [
        {
            "product_type": final_List_Top_Five[0],
            "score": final_List_Top_Five[1]
        },
        {
            "product_type": final_List_Top_Five[2],
            "score": final_List_Top_Five[3]
        },
        {
            "product_type": final_List_Top_Five[4],
            "score": final_List_Top_Five[5]
        },
        {
            "product_type": final_List_Top_Five[6],
            "score": final_List_Top_Five[7]
        },
        {
            "product_type": final_List_Top_Five[8],
            "score": final_List_Top_Five[9]
        }
    ],
    "product_type": final_List_Top_Five[0]
    }
    
    finalJson = json.dumps(result)

    return finalJson

