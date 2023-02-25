import onnxruntime as ort
import numpy as np

def predict_onnx(model_file, input_data):
    # Load the ONNX model
    session = ort.InferenceSession(model_file)

    # Get the names of the input and output tensors
    input_name = session.get_inputs()[0].name
    output_name = session.get_outputs()[0].name

    # Run the model on the input data
    output_data = session.run([output_name], {input_name: input_data})[0]

    # Return the output of the model
    if output_data > 0.5:
        return "Some tone of orange"
    else:
        return "Not some tone of orange"

input_data = np.array([[255, 128, 0]], dtype=np.float32)
output = predict_onnx("classifier.onnx", input_data)
print(output)

