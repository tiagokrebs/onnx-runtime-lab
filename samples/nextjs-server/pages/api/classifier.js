const onnxruntime = require("onnxruntime-node")

module.exports = async (req, res) => {
  const { r, g, b } = req.query

  // Load the ONNX model
  const session = await onnxruntime.InferenceSession.create("./classifier.onnx")

  // Create an input tensor
  const data = Float32Array.from([parseInt(r), parseInt(g), parseInt(b)])
  const inputTensor = new onnxruntime.Tensor("float32", data, [1, 3])

  // Run the model on the input tensor
  const outputTensor = await session.run({ input: inputTensor }, ["output"])

  // Get the output of the model as a probability
  const probability = outputTensor.output.data

  // Return the result as a JSON response
  res.status(200).json({
    isOrange: probability > 0.5
  })
}

export {}

