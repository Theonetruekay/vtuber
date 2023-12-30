# Vtuber Object Detection

This project implements object detection using TensorFlow for Vtuber images. The code includes scripts for creating TF records, downloading pre-trained models, and configuring the training process for transfer learning.

## Setup Paths

Make sure to set up the paths in the code to match your workspace structure.

```python
# Setup Paths
WORKSPACE_PATH = 'Tensorflow/workspace'
SCRIPTS_PATH = 'Tensorflow/scripts'
# ... (other paths)

Getting Started

    Set up the paths in the code according to your workspace structure.
    Create a label map in the annotations folder.
    Generate TF records for the training and testing datasets.
    Download pre-trained models from the TensorFlow Model Zoo.
    Copy the model config to the training folder.
    Update the config for transfer learning.

Training the Model

Train the model using the following command:

bash

python Tensorflow/research/object_detection/model_main_tf2.py --model_dir=Tensorflow/workspace/models/my_ssd_mobnet --pipeline_config_path=Tensorflow/workspace/models/my_ssd_mobnet/pipeline.config --num_train_steps=5000

Real-Time Object Detection

Run the script for real-time object detection using a webcam. The script displays live video feed with bounding boxes around detected objects.

bash

python path/to/your/script.py

Replace path/to/your/script.py with the actual path to your script.
Dependencies

Ensure you have the required dependencies installed. You can install them using:

bash

pip install -r requirements.txt

License

This project is licensed under the MIT License.