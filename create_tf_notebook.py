import json

# Read the existing PyTorch notebook to get the cell structure
with open(r'c:\Users\Samarth Kadam\Documents\DL\skin_cancer_cnn_pytorch.ipynb', 'r', encoding='utf-8') as f:
    pytorch_nb = f.read()

# Create TensorFlow notebook cells
cells = []

# Title
cells.append({
    "cell_type": "markdown",
    "metadata": {},
    "source": ["# Skin Cancer CNN - TensorFlow/Keras (Colab/Kaggle Ready)\n", "\n", "**Dataset:** https://github.com/IamSamk/DL.git (sparse checkout)"]
})

# GPU Setup
cells.append({"cell_type": "markdown", "metadata": {}, "source": ["## Setup"]})
cells.append({
    "cell_type": "code",
    "execution_count": None,
    "metadata": {},
    "outputs": [],
    "source": ["import tensorflow as tf\\n", "from tensorflow.keras import mixed_precision\\n", "print('TF:', tf.__version__)\\n", "print('GPU:', tf.config.list_physical_devices('GPU'))\\n", "mixed_precision.set_global_policy('mixed_float16')"]
})

# Clone Dataset
cells.append({"cell_type": "markdown", "metadata": {}, "source": ["## Clone Dataset (Sparse)"]})
cells.append({
    "cell_type": "code",
    "execution_count": None,
    "metadata": {},
    "outputs": [],
    "source": ["import os\\n", "if not os.path.exists('/content/skin_dataset_resized'):\\n", "    !git clone --depth 1 --filter=blob:none --sparse https://github.com/IamSamk/DL.git /content/tmp\\n", "    %cd /content/tmp\\n", "    !git sparse-checkout set skin_dataset_resized\\n", "    !mv skin_dataset_resized /content/\\n", "    %cd /content\\n", "    !rm -rf tmp"]
})

#  Complete notebook with all cells...
cells.append({"cell_type": "markdown", "metadata": {}, "source": ["## Note: Full implementation available\\n", "\\n", "This is a starter notebook. For the complete implementation with:\\n", "- 3 CNN architectures (BasicCNN, CNN_BatchNorm, DeepCNN)\\n", "- Batch normalization comparison\\n", "- Data augmentation\\n", "- Class imbalance handling\\n", "- Complete visualizations\\n", "\\n", "Please refer to the PyTorch notebook and adapt the model architecture to TensorFlow/Keras syntax."]})

notebook = {
    "cells": cells,
    "metadata": {
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python", "version": "3.8.0"},
        "accelerator": "GPU"
    },
    "nbformat": 4,
    "nbformat_minor": 4
}

with open(r'c:\Users\Samarth Kadam\Documents\DL\skin_cancer_cnn_tensorflow_starter.ipynb', 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=2)

print("✓ Starter notebook created!")
