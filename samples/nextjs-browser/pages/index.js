import { useState } from 'react';
import { InferenceSession, Tensor } from 'onnxruntime-web';

export default function Home() {
  const [r, setR] = useState('');
  const [g, setG] = useState('');
  const [b, setB] = useState('');
  const [isOrange, setIsOrange] = useState(null);

  async function classifyColor() {
      // Load the ONNX model
      const session = await InferenceSession.create('./_next/static/chunks/pages/classifier.onnx', { executionProviders: ['webgl'], graphOptimizationLevel: 'all' });

      // Create an input tensor
      const data = Float32Array.from([parseInt(r), parseInt(g), parseInt(b)]);
      const inputTensor = new Tensor('float32', data, [1, 3]);

      // Run the model on the input tensor
      const output = await session.run({ input: inputTensor }, ['output']);

      // Get the output of the model as a probability
      const probability = output.output.data;
      setIsOrange(probability > 0.5);
  }

  return (
    <div>
      <h1>Color Classifier</h1>
      <label>
        R: <input type="number" value={r} onChange={(e) => setR(e.target.value)} />
      </label>
      <br />
      <label>
        G: <input type="number" value={g} onChange={(e) => setG(e.target.value)} />
      </label>
      <br />
      <label>
        B: <input type="number" value={b} onChange={(e) => setB(e.target.value)} />
      </label>
      <br />
      <button onClick={classifyColor}>Classify Color</button>
      {isOrange !== null && (
        <div>The input color is {isOrange ? 'orange' : 'not orange'}.</div>
      )}
    </div>
      );
}
