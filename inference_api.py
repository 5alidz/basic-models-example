# example of how to use the inference API with the codegen-350M-multi model
# which is a small model that generates code from text
import requests

API_URL = "https://api-inference.huggingface.co/models/Salesforce/codegen-350M-multi"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "function add(a, b)"
})

print(output)
# if output is [{'generated_text': 'function add(m) {\r\n      var newXSSA = new XSSSA(g, m.group(0).length + 1);\r\n      newXSSA.start = m.pos;\r\n      new'}]

# to get the generated text, we need to access the first element of the list, then the value of the key 'generated_text'
print(output[0]['generated_text'])