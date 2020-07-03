import numpy as np

with open('transcripts.csv', 'r', encoding='UTF-8') as input_file:
    with open('processed_texts.csv', 'w', encoding='UTF-8') as output_file:    
        for i,line in enumerate(input_file):
            if i != 0:
                output_file.write(line.split('","https://')[0][1:])
        
