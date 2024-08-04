## Setup

1. Clone the repository and navigate to the project directory.

   ```sh
   git clone https://github.com/Roshan070298/GenAI.git
   cd GenAI

2. Download and install ollama framework into the OS.
3. Run the following commands to download the models

   ollama install llama2
   ollama install mistral

4. create a virtual environment and run the below command
   pip install requirements.txt

5. run the below command to start the app
   python app.py


## API 
 URL: http://127.0.0.1:5000/genAI
body : {
   "endpoint_name": "llama2",  # add the model name (llama2 or mistral)
    "prompt": "What is machine learning",  # add the prompt that you need an answer to
    "new": true     # optional parameter, if you want a new converation else the previous conversation continues
} 
