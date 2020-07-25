import numpy as np

num_lines = 1000

with open('transcripts.csv', 'r', encoding='UTF-8') as input_file:
    with open('processed_texts_'+str(num_lines)+'.csv', 'w', encoding='UTF-8') as output_file:
        for i,line in enumerate(input_file):
            if i != 0:
                parts = line.split('","https://www.ted.com/talks/')
                if len(parts) == 2:
                    text = parts[0][1:].replace('""','"')
                    output_file.write(text+'\n')
                if i == num_lines:
                    break
        
