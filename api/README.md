# The backend to chatbot application with the indexing form using ChatGpt

# Contents:

- [Requirements](#requirements)
- [Usage](#usage)
- [Storage](#storage)
- [Routes](#routes)
- [Chatbots](#chatbot-services)
- [Emix chatbot](#chatbot-emix-service)
- [Upload data file](#upload-data-file)

## requirements

```
langchain==0.0.167
llama_index==0.6.6
flask==2.3.2
flask_cors==3.0.10

```

```
Note:
    Requires-Python >=3.9,
```

# Usage

###### Create an environment using Python 3.9, install the required packages.

```
pip install -r requirements.txt
```

# Storage

## chatbot services

### 1- chatbot emix service:

```
data/chatbot_services/emix_service
```

# Routes

## chatbot services:

### chatbot emix service:

### Chat with emix:

```
 Url: /api/chat-emix
 Method : POST
 Payload: { 
           "question": (String)*
         }

```

###### success response

```
{
        "message": "Response completed successfully.",
        "success": True,
        "result": string
},200
```

###### error response

```
{
    "message": "A problem occurred during the chat process !!!",
    "success": False
},500
```

##### - Train emix chatbot service:

```
 Url: /api/train-chat-emix
 Method: POST
 Payload: { 
           "with_sitemap": (bool) default-false
         }
```

###### success response

```
{
    "message": "Training completed successfully",
    "success": True
},201

```

##### error response

```
{
    "message": "something went wrong, we're working to solve it",
    "success": False
},500
```

## Upload data file:

```
 Url: /api/upload-file
 Method : POST
 Payload/Multipart File: { 
           "file": (file)*
         }

```

###### success response

```
{
        "message": "File uploaded successfully.",
        "success": True,
        "result": string
},202
```

###### error response

```
{
    "message": "something went wrong, we're working to solve it",
    "success": False
},500
```
