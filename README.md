# NNUE-kit

## Overview
This project is designed to help users train an NNUE (Efficiently Updatable Neural Network) and integrate it into their chess engines using the NNUE probe and provided examples.

## Getting Started
### 1. Generating Validation Data
Training an NNUE is straightforward. First, download the necessary binary from:
[FireFather/sf-nnue-aio](https://github.com/FireFather/sf-nnue-aio/releases/tag/08-01-2022-AIO)

Once downloaded, unpack it on your device and run the following command to generate validation data:
```sh
gensfen depth 8 loop 10000000
```
This process will create a binary file in the same directory as the SFEN generator. Rename it to `val.bin` and move it to the project root.

### 2. Generating Training Data
Next, generate the training dataset with:
```sh
gensfen depth 8 loop 100000000
```

### 3. Training the NNUE Model
Run the following command to start the training process:
```sh
python main.py
```
**Note:** Training an NNUE is highly resource-intensive. It is recommended to use cloud-based services like AWS instead of a local machine.

After the training is complete, the results will be stored in:
```
/logs/lightning_logs/version_x/
```
Look for a checkpoint (`ckpt`) file corresponding to the epoch you trained. For example, if you trained for 120 epochs, search for a file with `epoch=120.ckpt`.

### 4. Quantizing the Model
Move the `ckpt` file to the project root (next to `main.py`) and run:
```sh
python main.py quantize
```
This will convert the checkpoint into a `.jnn` file.

### 5. Installing the NNUE Probe
Navigate to the folder containing `setup.py` (included with the NNUE probe) and install it:
```sh
python setup.py install
```

### 6. Using the NNUE Probe
Refer to `example.py` to understand how the probe works and integrate it into your own project.

## Pre-Trained NNUE
Since training can take a significant amount of time, a pre-trained NNUE is available in the [Releases](https://github.com/github-jimjim/NNUE-kit/releases/).
Make sure to leave a star if that helped you. :)

## Acknowledgments
Special thanks to:
- [DanielUranga/TensorFlowNNUE](https://github.com/DanielUranga/TensorFlowNNUE) for providing the model.

