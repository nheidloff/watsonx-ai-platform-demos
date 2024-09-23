# Fine-tuning of the Transcript Summarization Model with InstructLab

Install [InstructLab](https://github.com/instructlab), for example for MacBooks with Apple silicon:

```bash
cd instructlab
python3.11 -m venv --upgrade-deps venv  
source venv/bin/activate
pip cache remove llama_cpp_python
pip install 'instructlab[mps]'
```

Initialize iLab:

```bash
rm -rf "/Users/niklasheidloff/Library/Application Support/instructlab"
ilab config init --taxonomy-path ./taxonomy --model-path ./models --config ./profiles/config.yaml
Welcome to InstructLab CLI. This guide will help you to setup your environment.
Please provide the following values to initiate the environment [press Enter for defaults]:
Path to taxonomy repo [./taxonomy]: 
`./taxonomy` seems to not exist or is empty. Should I clone https://github.com/instructlab/taxonomy.git for you? [Y/n]: Y
Cloning https://github.com/instructlab/taxonomy.git...
Path to your model [./models]: 
Generating `/Users/niklasheidloff/Library/Application Support/instructlab/config.yaml` and `/Users/niklasheidloff/Library/Application Support/instructlab/internal/train_configuration/profiles`...
Please choose a train profile to use:
[0] No profile (CPU-only)
[1] A100_H100_x2.yaml
[2] A100_H100_x4.yaml
[3] A100_H100_x8.yaml
[4] L40_x4.yaml
[5] L40_x8.yaml
[6] L4_x8.yaml
Enter the number of your choice [hit enter for the default CPU-only profile] [0]: 
Using default CPU-only train profile.
Initialization completed successfully, you're ready to start using `ilab`. Enjoy!
rm -rf ./taxonomy/.git
```

Download Model:

```bash
ilab download
export HF_TOKEN=xxx
git lfs install
mkdir models/ibm
cd models/ibm
git clone https://huggingface.co/ibm/merlinite-7b
cd ../../
ls -la models/ibm/merlinite-7b                                             
total 28293360
drwxr-xr-x  19 niklasheidloff  staff         608 Sep 17 13:06 .
drwxr-xr-x   3 niklasheidloff  staff          96 Sep 17 12:52 ..
-rw-r--r--@  1 niklasheidloff  staff        6148 Sep 17 13:06 .DS_Store
drwxr-xr-x   3 niklasheidloff  staff          96 Aug 20 17:28 .cache
-rw-r--r--   1 niklasheidloff  staff        1519 Aug 20 17:28 .gitattributes
drwxr-xr-x   8 niklasheidloff  staff         256 Aug 20 17:28 Model Card for Merlinite 7b 28cc0b72cf574a4a828140d3539ede4a
-rw-r--r--   1 niklasheidloff  staff        8076 Aug 20 17:28 README.md
-rw-r--r--   1 niklasheidloff  staff         119 Aug 20 17:28 added_tokens.json
-rw-r--r--   1 niklasheidloff  staff         735 Aug 20 17:28 config.json
-rw-r--r--   1 niklasheidloff  staff         136 Aug 20 17:28 generation_config.json
-rw-r--r--   1 niklasheidloff  staff  4943227872 Aug 20 17:38 model-00001-of-00003.safetensors
-rw-r--r--   1 niklasheidloff  staff  4999819336 Aug 20 17:37 model-00002-of-00003.safetensors
-rw-r--r--   1 niklasheidloff  staff  4540581880 Aug 20 17:41 model-00003-of-00003.safetensors
-rw-r--r--   1 niklasheidloff  staff       23950 Aug 20 17:28 model.safetensors.index.json
-rw-r--r--   1 niklasheidloff  staff      201367 Aug 20 17:28 paper.pdf
-rw-r--r--   1 niklasheidloff  staff         670 Aug 20 17:28 special_tokens_map.json
-rw-r--r--   1 niklasheidloff  staff     1795802 Aug 20 17:28 tokenizer.json
-rw-r--r--   1 niklasheidloff  staff      493443 Aug 20 17:28 tokenizer.model
-rw-r--r--   1 niklasheidloff  staff        1961 Aug 20 17:28 tokenizer_config.json
```

Fine-tune Model:

```bash
ilab model train --local --model-path models/ibm/merlinite-7b
ls -la ./checkpoints/models-ibm-merlinite-7b-mlx-q
total 8508472
drwxr-xr-x  20 niklasheidloff  staff         640 Sep 17 13:19 .
drwxr-xr-x   3 niklasheidloff  staff          96 Sep 17 13:08 ..
-rw-r--r--   1 niklasheidloff  staff     6832790 Sep 17 13:10 adapters-010.npz
-rw-r--r--   1 niklasheidloff  staff     6832790 Sep 17 13:11 adapters-020.npz
-rw-r--r--   1 niklasheidloff  staff     6832790 Sep 17 13:12 adapters-030.npz
-rw-r--r--   1 niklasheidloff  staff     6832790 Sep 17 13:13 adapters-040.npz
-rw-r--r--   1 niklasheidloff  staff     6832790 Sep 17 13:14 adapters-050.npz
-rw-r--r--   1 niklasheidloff  staff     6832790 Sep 17 13:15 adapters-060.npz
-rw-r--r--   1 niklasheidloff  staff     6832790 Sep 17 13:16 adapters-070.npz
-rw-r--r--   1 niklasheidloff  staff     6832790 Sep 17 13:17 adapters-080.npz
-rw-r--r--   1 niklasheidloff  staff     6832790 Sep 17 13:18 adapters-090.npz
-rw-r--r--   1 niklasheidloff  staff     6832790 Sep 17 13:19 adapters-100.npz
-rw-r--r--   1 niklasheidloff  staff     6832790 Sep 17 13:19 adapters.npz
-rw-r--r--   1 niklasheidloff  staff         119 Sep 17 13:08 added_tokens.json
-rw-r--r--   1 niklasheidloff  staff        2293 Sep 17 13:08 config.json
-rw-r--r--   1 niklasheidloff  staff  4262441012 Sep 17 13:08 model.safetensors
-rw-r--r--   1 niklasheidloff  staff         670 Sep 17 13:08 special_tokens_map.json
-rw-r--r--   1 niklasheidloff  staff     1795830 Sep 17 13:08 tokenizer.json
-rw-r--r--   1 niklasheidloff  staff      493443 Sep 17 13:08 tokenizer.model
-rw-r--r--   1 niklasheidloff  staff        1989 Sep 17 13:08 tokenizer_config.json
mkdir ./checkpoints-prevent-deletions
mkdir ./checkpoints-prevent-deletions/models-ibm-merlinite-7b-mlx-q
cp ./checkpoints/models-ibm-merlinite-7b-mlx-q/* ./checkpoints-prevent-deletions/models-ibm-merlinite-7b-mlx-q
```

Quantize Model:

```bash
ilab model convert --model-dir ./checkpoints/models-ibm-merlinite-7b-mlx-q
ls -la models-ibm-merlinite-7b-trained
total 8543896
drwxr-xr-x   9 niklasheidloff  staff         288 Sep 17 17:20 .
drwxr-xr-x  12 niklasheidloff  staff         384 Sep 17 17:19 ..
-rw-r--r--   1 niklasheidloff  staff         119 Sep 17 17:19 added_tokens.json
-rw-r--r--   1 niklasheidloff  staff        2246 Sep 17 17:19 config.json
-rw-r--r--   1 niklasheidloff  staff  4368484544 Sep 17 17:20 models-ibm-merlinite-7b-Q4_K_M.gguf
-rw-r--r--   1 niklasheidloff  staff         670 Sep 17 17:19 special_tokens_map.json
-rw-r--r--   1 niklasheidloff  staff     1795830 Sep 17 17:19 tokenizer.json
-rw-r--r--   1 niklasheidloff  staff      493443 Sep 17 17:19 tokenizer.model
-rw-r--r--   1 niklasheidloff  staff        1989 Sep 17 17:19 tokenizer_config.json
```

Serve Model with iLab:

```bash
ilab model serve --model-path models-ibm-merlinite-7b-trained/models-ibm-merlinite-7b-Q4_K_M.gguf
```

Invoke model running in iLab:

```bash
curl -X 'POST' \
  'http://localhost:8000/v1/completions' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "model": "models-ibm-merlinite-7b-trained/models-ibm-merlinite-7b-Q4_K_M.gguf",
  "max_tokens": 400,
  "temperature": 0,
  "prompt": "<|system|>\nI am, Red Hat\u00ae Instruct Model based on Granite 7B, an AI language model developed by Red Hat and IBM Research, based on the Granite-7b-base language model. My primary function is to be a chat assistant.\n<|user|>\nSummarize the transcript of the call. Identify the agent and the subscriber. Add any specific issues mentioned by the subscriber. Add any corrective actions taken as directed by the agent. Please mention if the issue is resolved. Mention any follow-up actions and timelines. And list the phone number of the subscriber at the end.\n\nTranscript:\n\nJohn (Teltop Customer Care Agent): Hello, this is John from Teltop customer care. How can I assist you today?\n\nMary (Disappointed Subscriber): Hi John, it is Mary again. I have been having a nightmare with your service. My home Wi-Fi is acting up, and the TV service over fiber is terrible.\n\nJohn: I am sorry to hear about the troubles you are facing at home, Mary. Let us address these issues. Can you please provide me with your account number or the phone number associated with your account?\n\nMary: Sure, it is 123-555-1234.\n\nJohn: Thank you. Can you provide me with more details about the Wi-Fi problems and the TV service quality?\n\nMary: The Wi-Fi keeps dropping, and the TV service over fiber is pixelated and glitchy. It is making it impossible to enjoy any show or movie.\n\nJohn: I understand how frustrating that can be, Mary. Let me check our system to see if there are any reported issues in your area.\n\nJohn checks the system and finds no reported issues in Mary area.\n\nJohn: Mary, it seems there are no reported issues in your area. It could be a specific problem with your equipment or connection. Can you check if all cables are properly connected and if there are any obstructions to the router?\n\nMary: I have checked, and everything seems fine. This is so frustrating!\n\nJohn: I am sorry to hear that, Mary. It might be best to perform a remote diagnostic check on your router. I can guide you through the process.\n\nJohn guides Mary through the diagnostic check, and it reveals some issues with the router.\n\nJohn: Mary, it appears there are some issues with your router. We need to update the router software. Additionally, I will address the TV service quality. There might be a signal issue or equipment malfunction.\n\nMary: Finally some answers! When will the router be updated, and how soon can you fix the TV service?\n\nJohn: We will start the router update immediately. As for the TV service, our team will work on it directly, and you should see improvements within the next 24 hours.\n\nMary: Well, it is about time! I hope this gets sorted out.\n\nJohn: I appreciate your patience, Mary. To make up for the inconvenience, I would like to offer you three months of free TV service once everything is resolved. Does that sound fair?\n\nMary: That is more like it, John. I appreciate the offer. Let us hope the technician and your team can fix these issues once and for all.\n\nJohn: Thank you for understanding, Mary. We are committed to providing you with a seamless experience. If you have any other concerns or questions, feel free to reach out.\n\nMary: Thanks, John. I will take the offer for the free TV service, and let us hope things get better soon.\n\nJohn: Absolutely, Mary. We appreciate your loyalty, and we are here to make things right. If there is anything else, do not hesitate to contact us. Have a great day!\n<|assistant|>\n",
  "stop": [
    "<|endoftext|>"
  ]
}'
```

iLab chat: 

```bash
cd instructlab
source venv/bin/activate
ilab chat -m models-ibm-merlinite-7b-trained/models-ibm-merlinite-7b-Q4_K_M.gguf
```

Serve Model with Ollama:

```bash
cd ../application
ollama create transcript-summary -f Modelfile
ollama run transcript-summary
cd ../instructlab
```

Invoke model running in Ollama:

```bash
curl -X 'POST' \
  'http://localhost:11434/v1/completions' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "model": "transcript-summary",
  "max_tokens": 400,
  "temperature": 0,
  "prompt": "<|system|>\nI am, Red Hat\u00ae Instruct Model based on Granite 7B, an AI language model developed by Red Hat and IBM Research, based on the Granite-7b-base language model. My primary function is to be a chat assistant.\n<|user|>\nSummarize the transcript of the call. Identify the agent and the subscriber. Add any specific issues mentioned by the subscriber. Add any corrective actions taken as directed by the agent. Please mention if the issue is resolved. Mention any follow-up actions and timelines. And list the phone number of the subscriber at the end.\n\nTranscript:\n\nJohn (Teltop Customer Care Agent): Hello, this is John from Teltop customer care. How can I assist you today?\n\nMary (Disappointed Subscriber): Hi John, it is Mary again. I have been having a nightmare with your service. My home Wi-Fi is acting up, and the TV service over fiber is terrible.\n\nJohn: I am sorry to hear about the troubles you are facing at home, Mary. Let us address these issues. Can you please provide me with your account number or the phone number associated with your account?\n\nMary: Sure, it is 123-555-1234.\n\nJohn: Thank you. Can you provide me with more details about the Wi-Fi problems and the TV service quality?\n\nMary: The Wi-Fi keeps dropping, and the TV service over fiber is pixelated and glitchy. It is making it impossible to enjoy any show or movie.\n\nJohn: I understand how frustrating that can be, Mary. Let me check our system to see if there are any reported issues in your area.\n\nJohn checks the system and finds no reported issues in Mary area.\n\nJohn: Mary, it seems there are no reported issues in your area. It could be a specific problem with your equipment or connection. Can you check if all cables are properly connected and if there are any obstructions to the router?\n\nMary: I have checked, and everything seems fine. This is so frustrating!\n\nJohn: I am sorry to hear that, Mary. It might be best to perform a remote diagnostic check on your router. I can guide you through the process.\n\nJohn guides Mary through the diagnostic check, and it reveals some issues with the router.\n\nJohn: Mary, it appears there are some issues with your router. We need to update the router software. Additionally, I will address the TV service quality. There might be a signal issue or equipment malfunction.\n\nMary: Finally some answers! When will the router be updated, and how soon can you fix the TV service?\n\nJohn: We will start the router update immediately. As for the TV service, our team will work on it directly, and you should see improvements within the next 24 hours.\n\nMary: Well, it is about time! I hope this gets sorted out.\n\nJohn: I appreciate your patience, Mary. To make up for the inconvenience, I would like to offer you three months of free TV service once everything is resolved. Does that sound fair?\n\nMary: That is more like it, John. I appreciate the offer. Let us hope the technician and your team can fix these issues once and for all.\n\nJohn: Thank you for understanding, Mary. We are committed to providing you with a seamless experience. If you have any other concerns or questions, feel free to reach out.\n\nMary: Thanks, John. I will take the offer for the free TV service, and let us hope things get better soon.\n\nJohn: Absolutely, Mary. We appreciate your loyalty, and we are here to make things right. If there is anything else, do not hesitate to contact us. Have a great day!\n<|assistant|>\n",
  "stop": [
    "<|endoftext|>"
  ]
}'
```