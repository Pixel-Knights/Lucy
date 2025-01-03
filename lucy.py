from openai import OpenAI

# Initialize OpenAI client that points to the local LM Studio server
client = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio"
)

# Define the conversation with the AI
messages = [
    {"role": "system", "content": "Apenas responda em português."},
    {"role": "user", "content": "What do you like to do?"}
]

# Define the expected response structure
character_schema = {
    "type": "json_schema",
    "json_schema": {
        "name": "characters",
        "schema": {
            "type": "object",
            "properties": {
                "characters": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string"},
                            "occupation": {"type": "string"},
                            "personality": {"type": "string"},
                            "background": {"type": "string"}
                        },
                        "required": ["name", "occupation", "personality", "background"]
                    },
                    "minItems": 1,
                }
            },
            "required": ["characters"]
        },
    }
}

# Get response from AI
response = client.chat.completions.create(
    model="your-model",
    messages=messages,
    #response_format=character_schema,
)

# Parse and display the results
results = response.choices[0].message.content
print(results)