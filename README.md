# NNUE-kit

## Overview
NNUE-kit is designed to help users train an NNUE (Efficiently Updatable Neural Network) and integrate it into their chess engines using NNUE probes and provided examples. This guide will walk you through setting up, training, and deploying your NNUE model efficiently.

## Getting Started

### 1. Generating Validation Data
To begin, download the necessary binary from:
[FireFather/sf-nnue-aio](https://github.com/FireFather/sf-nnue-aio/releases/tag/08-01-2022-AIO)

Once downloaded, unpack it on your device and execute the following command to generate validation data:
```sh
./gensfen depth 8 loop 10000000
```
This process will generate a binary file in the same directory as the SFEN generator. Rename it to `val.bin` and move it to the project root.

### 2. Generating Training Data
Next, generate the training dataset using:
```sh
./gensfen depth 8 loop 100000000
```
Similar to the validation data, rename the generated file to `train.bin` and move it to the project root.

### 3. Training the NNUE Model
To start training, run:
```sh
python main.py
```
**Note:** Training an NNUE model is computationally expensive. It is recommended to use cloud-based services like AWS or Google Colab instead of a local machine.

After training is complete, results will be saved in:
```
/logs/lightning_logs/version_x/
```
Look for a checkpoint (`.ckpt`) file corresponding to the last trained epoch. For example, if you trained for 120 epochs, locate the file `epoch=120.ckpt`.

### 4. Quantizing the Model
To quantize the trained model, move the `.ckpt` file to the project root (next to `main.py`) and run:
```sh
python main.py quantize
```
This will convert the checkpoint into a `.jnn` file, optimized for inference.

## NNUE Probes
NNUE probes are available in two implementations: **Rust** and **Python**.
- **Python NNUE Probe**: Easy to use but has slower inference times.
- **Rust NNUE Probe**: Faster inference (~200kN/s), but requires Rust or an external `.whl` download.

### Installing the NNUE Probe
#### Python Probe
To install the Python-based NNUE probe, navigate to the folder containing `setup.py` (included with the NNUE probe) and run:
```sh
python setup.py install
```

#### Rust Probe
You can install the Rust probe by:
1. Downloading the `.whl` file from the [Releases](https://github.com/FireFather/sf-nnue-aio/releases/tag/08-01-2022-AIO) and installing it:
   ```sh
   pip install <downloaded_whl_file>
   ```
2. Building it manually using `maturin`:
   ```sh
   maturin build
   pip install target/wheel/*.whl
   ```

### Using the NNUE Probe
Refer to `example.py` for an example of how to integrate the NNUE probe into your project.

## Pre-Trained NNUE Models
Training an NNUE model requires significant computational resources. To save time, a pre-trained NNUE model is available for download in the [Releases](https://github.com/FireFather/sf-nnue-aio/releases/tag/08-01-2022-AIO) section.

## Acknowledgments
Special thanks to:
- [DanielUranga/TensorFlowNNUE](https://github.com/DanielUranga/TensorFlowNNUE) for contributing to the model development.

This guide provides a streamlined approach to training and integrating NNUE into chess engines. If you have any issues, please check the provided examples and documentation for further assistance.
