import json
import os
import sys
'''
test_241108.json:
python mcqa.py \
    --input_file "data/test.jsonl" \
    --output_file "predictions/test.jsonl"
    --model_path "models/Llama-3.2-1B-Instruct" \
    --num_forward_passes 8
temperature: 0.6 (default)
seed: 42 (default)
Acc: 0.49658703071672355

'''
def get_accuracy(json_fpath):
    with open(json_fpath, 'r') as f:
        length = 0
        correct = 0
        for line in f:
            data = json.loads(line)
            length += 1
            if data['correct']:
                correct += 1
    return correct / length

if __name__ == '__main__':
    json_fpath = sys.argv[1]
    print(get_accuracy(json_fpath))