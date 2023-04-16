import meteorite
from llama_cpp import Llama

app = meteorite.Meteorite()


@app.predict
def predict(input_bytes):
    input_string = input_bytes.decode("utf-8")
    llm = Llama(model_path="./model/7B/ggml-model-q4_0.bin")
    output = llm(input_string, max_tokens=32, echo=True)
    output_text = output["choices"][0]["text"]
    return output_text


app.start()
