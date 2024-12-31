# CIFAR-10 Classification

This project focuses on implementing machine learning models for data classification using Python. The repository is structured to provide clear organization and functionality, enabling users to understand the workflow and explore the codebase.

## Features

### Data Preparation
The project includes scripts for preparing the CIFAR-10 dataset:
- **`CreateDataFolders.py`**: Handles the creation of necessary data directories.
- **`DownloadData.py`**: Downloads the CIFAR-10 dataset.
- **`ProcessData.py`**: Preprocesses the dataset into a usable format.

### Machine Learning Models
Jupyter notebooks are provided for implementing various machine learning models:
- **Bayesian Learning**: [`Bayesian_Learning.ipynb`](./src/Bayesian_Learning.ipynb)
- **Decision Tree**: [`Decision_Tree.ipynb`](./src/Decision_Tree.ipynb)
- **Multi-Layer Perceptron**: [`MultiLayerPerceptron.ipynb`](./src/MultiLayerPerceptron.ipynb)
- **Convolutional Neural Network**: [`CNN.ipynb`](./src/CNN.ipynb)

### Environment and Dependencies
The project is built using Python, with required dependencies listed in the `requirements.txt` file. Some of the core libraries include:
- `numpy`
- `pandas`
- `scikit-learn`
- `torch`

## Getting Started

1. Clone the repository to your local machine:
   ```bash
   git clone <repository-url>
   ```
2. (Optional) Create a virtual environment:
   ```bash
    python -m venv env
    source env/bin/activate  # On Windows: .\env\Scripts\activate
   ```
3. Install dependencies:
   ```bash
     pip install -r requirements.txt
   ```

## File Structure

The repository is designed for ease of navigation:
- **`src/`**: Contains core scripts and Jupyter notebooks.
- **Supporting files**: Includes `.gitignore`, `requirements.txt`, and this `README.md`.

## Project Scope

This version of the project does not include pre-trained weights, focusing instead on code exploration rather than model training or testing. Users can review the implementation of each model to understand the techniques and workflows applied.

### Highlights
- A **Convolutional Neural Network (CNN)** model is included, allowing users to explore a deep learning approach to classification.
- Complements traditional machine learning models such as Bayesian Learning, Decision Tree, and Multi-Layer Perceptron.

## Purpose

This project is ideal for:
- Gaining insights into Python-based machine learning and deep learning methodologies.
- Building a foundation for further development or adaptation to specific use cases.
