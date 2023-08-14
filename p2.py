import torch
import onnx
import onnx2keras
import torch2trt
import keras
import numpy as np

# Load your PyTorch model
pytorch_model = torch.load('your_model.pth')
pytorch_model.eval()

# Convert to ONNX format using torch2trt
dummy_input = torch.randn(1, 3, 224, 224).cuda()  # Adjust input shape
trt_model = torch2trt.pytorch_to_trt_model(pytorch_model, [dummy_input])

# Save the TRT model as ONNX
onnx_path = 'trt_model.onnx'
torch.onnx.export(trt_model, dummy_input, onnx_path, verbose=True)

# Load the ONNX model
onnx_model = onnx.load(onnx_path)

# Convert ONNX model to Keras using onnx2keras
keras_model = onnx2keras.onnx_to_keras(onnx_model, ['input_name'])  # Replace 'input_name' with the actual input name

# Print Keras model summary
keras_model.summary()

# Test the Keras model
input_data = np.random.random((1, 3, 224, 224))  # Adjust input shape
output = keras_model.predict(input_data)
print(output)
