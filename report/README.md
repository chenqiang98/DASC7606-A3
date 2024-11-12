# 3036370891

This folder contains the source code and resources for Assignment 3 of the DASC7606 Deep Learning course.

[Github Forked Repository](https://github.com/chenqiang98/DASC7606-A3)

## File Structure

```
3036370891/
├── 7606A3_3036370891.pdf
├── README.md
├── model_predictions_66.64%.jsonl
├── src/
│   ├── mcqa.py
│   ├── modelling_llama.py
│   ├── tokenization_llama_fast.py
│   └── get_accuracy.py
├── predictions/
│   ├── ...
```

## Description

- **7606A3_3036370891.pdf**: Final report.
- **README.md**: Project documentation.
- **model_predictions_66.64%.jsonl**: predict result with 66.64% accuracy.
- **src/**: Contains the source code files.
    - **mcqa.py**: Main script to run the inference of model.
    - **modelling_llama.py**: Utility functions.
    - **tokenization_llama_fast.py**: Utility functions.
    - **get_accuracy.py**: get accuracy from result jsonl file.
- **predictions/**: All prediction results.


## Result

This section contains 3 different subsections, including the result of experiments on temperature, model scale, and multiple forward passes for majority voting. Each part demonstrates how a single change in hyperparameters or settings can affect the overall performance of the model.

### Test benchmarks

Model: Llama-3.2-1B-Instruct
Num_forward_passes: 8
Temperature: 0.6
Accuracy: 49.66%

### Experiments on Temperature

Model: Llama-3.2-1B-Instruct
Num_forward_passes: 8

**Temperature: (0.2, 0.4, 0.6, 0.8, 1.0)**

(Detailed description on experiments can be found in report.pdf)

| Temperature|Accuracy|File Name|
|------------|--------|---------|
| 0.2        | 48.29% |test_2411081414.jsonl|
| 0.4        | 50.94% |test_2411090730.jsonl|
| 0.6        | 49.66% |test_2411072300.jsonl|
| 0.8        | 48.21% |test_2411091030.jsonl|
| 1.0        | 45.90% |test_2411081107.jsonl|

### Experiments on Model Scale

**Model: (Llama-3.2-1B-Instruct, Llama-3.2-3B-Instruct)**

Num_forward_passes: 8
Temperature: 0.6

|Model|Accuracy|File Name|
|-----|--------|---------|
|1B   |49.66%  |test_2411072300.jsonl|
|3B   |66.64%  |test_2411082338.jsonl|

### Experiments on Forward Passes

Model: Llama-3.2-1B-Instruct

**Num_forward_passes: (4, 8, 16)**

Temperature: 0.6

|Num of forward passes|Accuracy|File Name|
|--------------------|---------|---------|
| 4            |         48.12%|test_2411121831.jsonl|
|8             |         49.66%|test_2411072300.jsonl|
|16            |         51.11%|test_2411081717.jsonl|

## How to Run

### get accuracy:

python3 ./src/get_accuracy.py model_predictions_66.64%.jsonl
