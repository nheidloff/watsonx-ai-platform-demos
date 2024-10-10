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
export CONTENT_1_RESULT_TITLE="Potential route cause for Wi-Fi issue C01"
export CONTENT_1_RESULT_BODY="There could be a specific problem with the equipment or connection. Ask client to check if all cables are properly connected and if there are any obstructions to the router."
export CONTENT_2_KEYWORD="didn't solve"
export CONTENT_2_RESULT_TITLE="Potential route cause for Wi-Fi issue C02"
export CONTENT_2_RESULT_BODY="A reason why Wi-Fi doesn't work could be an old unsupported router software version. Perform a remote diagnostic check on the router."
export CONTENT_NOT_RELEVANT_TITLE="Great weather"
export CONTENT_NOT_RELEVANT_BODY="The grass is always greener on the other side of the fence"

podman run -d -p 8080:8080 --name custom-search \
    -e CONTENT_1_KEYWORD=${CONTENT_1_KEYWORD} \
    -e CONTENT_1_RESULT_TITLE=${CONTENT_1_RESULT_TITLE} \
    -e CONTENT_1_RESULT_BODY=${CONTENT_1_RESULT_BODY} \
    -e CONTENT_2_KEYWORD=${CONTENT_2_KEYWORD} \
    -e CONTENT_2_RESULT_TITLE=${CONTENT_2_RESULT_TITLE} \
    -e CONTENT_2_RESULT_BODY=${CONTENT_2_RESULT_BODY} \
    -e CONTENT_NOT_RELEVANT_TITLE=${CONTENT_NOT_RELEVANT_TITLE} \
    -e CONTENT_NOT_RELEVANT_BODY=${CONTENT_NOT_RELEVANT_BODY} \
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
}' | jq
curl -X 'POST' \
  'http://127.0.0.1:8080/search' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "query": "'"$CONTENT_2"'"
}' | jq
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

podman tag custom-search-linux-amd64 icr.io/niklas/custom-search-linux-amd64:2
podman push icr.io/niklas/custom-search-linux-amd64:2
```

## Deploy to Code Engine

```bash
// create project niklas-watson-demo

// create application niklas-custom-search

// create secret for private.icr.io

// define CONTENT_1_KEYWORD, CONTENT_1_RESULT_TITLE, CONTENT_1_RESULT_BODY, CONTENT_2_KEYWORD, CONTENT_2_RESULT_TITLE, CONTENT_2_RESULT_BODY, CONTENT_NOT_RELEVANT_TITLE, CONTENT_NOT_RELEVANT_BODY

// get URL
```

## Example Conversation

**Step 1**

User input: "What are potential route causes for 'Wi-Fi problems and the TV service quality'?"

```bash
curl -X POST  \
   'https://niklas-custom-search.xxx.eu-de.codeengine.appdomain.cloud/search' \
   -H 'content-type: application/json' \
   -H 'content-type: application/json' \
   -H 'accept: application/json' \
   -d '"{
   \"query\":\"What are potential route causes for 'Wi-Fi problems and the TV service quality'?\",
   \"filter\":\"\"
}"' 
```

```json
{
  "status":200,
  "body":[
    {
      "title":"Potential route cause for Wi-Fi issue C01",
      "body":"There could be a specific problem with the equipment or connection. Ask client to check if all cables are properly connected and if there are any obstructions to the router.",
      "result_metadata":{"document_retrieval_source":"server_side_search"}
    },
    {
      "title":"Great weather",
      "body":"The grass is always greener on the other side of the fence",
      "result_metadata":{"document_retrieval_source":"server_side_search"}
    }
  ]
}
```

Assistant: "There could be a specific problem with the equipment or connection. Check if all cables are properly connected and if there are any obstructions to the router."

**Step 2**

User input: "That didn't solve the issue. What else could be the route cause?"

```bash
curl -X POST  \
   'https://niklas-custom-search.xxx.eu-de.codeengine.appdomain.cloud/search' \
   -H 'content-type: application/json' \
   -H 'content-type: application/json' \
   -H 'accept: application/json' \
   -d '"{
   \"query\":\"The solution provided in the previous answer didn't solve the issue. What are other potential route causes for 'Wi-Fi problems and the TV service quality'?\",
   \"original_query\":\"That didn't solve the issue. What else could be the route cause?\",
   \"filter\":\"\"
}"' 
```

```json
{
  "status":200,
  "body":[
    {
      "title":"Potential route cause for Wi-Fi issue C02",
      "body":"A reason why Wi-Fi doesn't work could be an old unsupported router software version. Perform a remote diagnostic check on the router.",
      "result_metadata":{"document_retrieval_source":"server_side_search"}
    },
    {
      "title":"Great weather",
      "body":"The grass is always greener on the other side of the fence",
      "result_metadata":{"document_retrieval_source":"server_side_search"}
    }
  ]
}
```

Assistant: "The only potential route cause I'm aware of is an old unsupported router software version, which would require a remote diagnostic check on the router."