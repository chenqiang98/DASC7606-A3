import json
import os
import sys
from collections import Counter
from matplotlib import pyplot as plt
'''
test_2411072300.jsonl:
python mcqa.py \
    --input_file "data/test.jsonl" \
    --output_file "predictions/test.jsonl"
    --model_path "models/Llama-3.2-1B-Instruct" \
    --num_forward_passes 8
temperature: 0.6 (default)
seed: 42 (default)
Acc: 0.49658703071672355


test_2411081107.jsonl:
python mcqa.py \
    --input_file "data/test.jsonl" \
    --output_file "predictions/test_2411081107.jsonl" \
    --model_path "models/Llama-3.2-1B-Instruct" \
    --num_forward_passes 8                  
temperature: 1.0
seed: 42
Acc: 0.4590443686006826


test_2411081414.jsonl:
python mcqa.py \
    --input_file "data/test.jsonl" \
    --output_file "predictions/test_2411081414.jsonl" \
    --model_path "models/Llama-3.2-1B-Instruct" \
    --num_forward_passes 8                  
temperature: 0.2
seed: 42
Acc: 0.48293515358361777

test_2411090730.jsonl:
python mcqa.py \
    --input_file "data/test.jsonl" \
    --output_file "predictions/test_2411090730.jsonl" \
    --model_path "models/Llama-3.2-1B-Instruct" \
    --num_forward_passes 8                  
temperature: 0.4
seed: 42
Acc: 0.5093856655290102

test_2411091030.jsonl:
python mcqa.py \
    --input_file "data/test.jsonl" \
    --output_file "predictions/test_2411091230.jsonl" \
    --model_path "models/Llama-3.2-1B-Instruct" \
    --num_forward_passes 8                  
temperature: 0.8
seed: 42
Acc: 0.48208191126279865

test_2411121831.jsonl
python mcqa.py \
    --input_file "data/test.jsonl" \
    --output_file "predictions/test_2411121831.jsonl" \
    --model_path "models/Llama-3.2-1B-Instruct" \
    --num_forward_passes 4
temperature: 0.6
seed: 42
Acc: 0.4812286689419795

test_2411081717.jsonl
python mcqa.py \
    --input_file "data/test.jsonl" \
    --output_file "predictions/test_2411081717.jsonl" \
    --model_path "models/Llama-3.2-1B-Instruct" \
    --num_forward_passes 16
temperature: 0.6
seed: 42
Acc: 0.5110921501706485

test_2411082338.jsonl
python mcqa.py \
    --input_file "data/test.jsonl" \
    --output_file "predictions/test_2411082320.jsonl" \
    --model_path "models/Llama-3.2-3B-Instruct" \
    --num_forward_passes 8
temperature: 0.6
seed: 42
Acc: 0.6663822525597269
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

def get_accuracy_and_confidence_table(json_fpath):
    with open(json_fpath, 'r') as f:
        confidence_counter = Counter()
        confidence_correct_counter = Counter()
        length = 0
        correct = 0
        for line in f:
            data = json.loads(line)
            length += 1
            if data['correct']:
                correct += 1
                confidence_correct_counter[data['confidence']] += 1
            confidence_counter[data['confidence']] += 1
    return correct / length, confidence_counter, confidence_correct_counter

if __name__ == '__main__':
    json_fpath = sys.argv[1]
    print(get_accuracy(json_fpath))