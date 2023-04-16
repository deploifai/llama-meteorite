# Running Llama on Meteorite
This example uses Meteorite to create an HTTP API for hosting models.

This example hosts [llama.cpp](https://github.com/ggerganov/llama.cpp) using the [llama-cpp-python](https://github.com/abetlen/llama-cpp-python).

## The model

The LLaMA model can be obtained from [here](https://ai.facebook.com/blog/large-language-model-llama-meta-ai/).

    .
    ├── ...
    ├── model                   
    │   ├── 7B
    │   │   ├── ggml-model-q4_0.bin
    │   │   ├── ggml-model-f16.bin
    │   │   ├── params.json
    │   │   ├── consolidated.00.pth
    │   │   └── checklist.chk
    │   ├── ggml-vocab.bin
    │   ├── tokenizer.model
    │   └── tokenizer_checklist.chk
    └── ...


## Run the Meteorite application

The example was developed with `Python 3.8`.


### Install requirements
```shell
pip install -r requirements.txt
```

### Run the application

The Meteorite application is written in [main.py](./main.py)
```shell
python main.py
```

Once the application is started:
```shell
➜ python main.py
[2023-04-16T15:43:36Z INFO  actix_server::builder] starting 1 workers
[2023-04-16T15:43:36Z INFO  actix_server::server] Actix runtime found; starting in Actix runtime
```

## Acknowledgements
This example is not possible without the following projects:

1. [llama.cpp](https://github.com/ggerganov/llama.cpp) - Inference of LLaMA model in pure C/C++
2. [llama-cpp-python](https://github.com/abetlen/llama-cpp-python) - Simple Python bindings for @ggerganov's llama.cpp library.
