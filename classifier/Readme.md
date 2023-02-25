# Classifier model

This path contains a simple Neural Network used to classify if a sequence of RGB colors is orange-ish or not. The method is far from ideal and so is the accuracy of the model.  

The purpose here is not the quality of the classifier itself but to show how an ONNX can be created to be used by other applications.

To create the ONNX model use one of the methods below.  
You probably will need to create many versions of the model in order for the tests at the end to respond correctly (or just use the onnx already available).  
- The .ipybn file can be used as a Jupyper Notebook
- There is also a Google Colab notebook on [this link](https://colab.research.google.com/drive/1n96fSzKV3Siu7gXT4ia2UFVBAi-3VTmE?usp=sharing)
- Or use the `classifier.py` file
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python classifier.py
```
