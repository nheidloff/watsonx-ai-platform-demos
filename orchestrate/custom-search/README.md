# Custom Search Extension for watsonx Orchestrate

```bash
python3.11 -m venv --upgrade-deps venv
source venv/bin/activate
pip install -r requirements.txt
fastapi dev main.py --port 8080
```

```bash
open http://127.0.0.1:8080/docs
```

```bash
Mac:
podman build -t custom-search .
Linux:
podman build --platform linux/amd64 -t custom-search-linux-amd64 .

export CONTENT_1_KEYWORD="Wi-Fi"
export CONTENT_1_RESULT="Potential cause:\nThere could be a specific problem with the equipment or connection.\n\nAction:\nAsk client to check if all cables are properly connected and if there are any obstructions to the router."
export CONTENT_2_KEYWORD="didn't solve"
export CONTENT_2_RESULT="Potential cause:\nOld unsupported router software version.\n\nAction:\nPerform a remote diagnostic check on the router."

podman run -d -p 8080:8080 --name custom-search \
    -e CONTENT_1_KEYWORD=${CONTENT_1_KEYWORD} \
    -e CONTENT_1_RESULT=${CONTENT_1_RESULT} \
    -e CONTENT_2_KEYWORD=${CONTENT_2_KEYWORD} \
    -e CONTENT_2_RESULT=${CONTENT_2_RESULT} \
    custom-search
```

```bash
export CONTENT_1="What are potential route causes for 'Wi-Fi problems and the TV service quality'?"
export CONTENT_2="That didn't solve the issue. Which other route causes are there?"
curl -X 'POST' \
  'http://127.0.0.1:8080/search' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "query": "'"$CONTENT_1"'"
}'
curl -X 'POST' \
  'http://127.0.0.1:808/search' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "query": "'"$CONTENT_2"'"
}'
```

## Push Container

```bash
open https://cloud.ibm.com/docs/cli?topic=cli-getting-started

ibmcloud plugin install container-registry
ibmcloud plugin install ce
ibmcloud login --sso -r eu-de
ibmcloud target -g niklas
ibmcloud cr login 

// create namespace

podman tag custom-search-linux-amd64 icr.io/niklas/custom-search-linux-amd64:1
podman push icr.io/niklas/custom-search-linux-amd64:1
```

## Deploy to Code Engine

```bash
// create project niklas-watson-demo

// create application niklas-custom-search

// create secret for private.icr.io

// define CONTENT_1_KEYWORD, CONTENT_1_RESULT, CONTENT_2_KEYWORD and CONTENT_2_RESULT

// get URL
```