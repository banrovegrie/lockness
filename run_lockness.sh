#!/bin/bash

echo "Welcome to Lockness - Your ML Model Training Assistant"
echo "Please follow the prompts to train your model."
read -p "Enter your dataset's ID as shown in the website: " data_path
read -p "Enter path to your PyTorch model file: " model_path
read -p "Enter path for saving the output model file: " output_path
read -p "Enter number of epochs for training: " epochs
read -p "Enter learning rate: " learning_rate

echo "Starting model training..."
python train_model.py --data_path "$data_path" --model_path "$model_path" --output_path "$output_path" --epochs "$epochs" --learning_rate "$learning_rate"

echo "Model training completed and saved to $output_path."
echo "Thank you for using Lockness!"
