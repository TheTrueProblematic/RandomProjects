from openai import OpenAI
import base64
client = OpenAI(api_key='key',)

imagePath = "test.png"

with open(imagePath, "rb") as image_file:
  encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

response = client.chat.completions.create(
  model="gpt-4-vision-preview",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "answer the question in this image. At the bottom of your response simply put answer: (whatever goes in the blank)"},
        {
          "type": "image_url",
          "image_url": {
            "url": "data:image/png;base64," + encoded_string,
            "detail": "high"
          },
        },
      ],
    }
  ],
  max_tokens=1000,
)

firstResp = response.choices[0].message.content


response = client.chat.completions.create(
  model="gpt-4-vision-preview",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "Take this answer and reduce it down to the smallest shortest version necessary to answer the question. For example if it's multiple choice simply output the letter associated with the answer, or if its a numberical response only ouput the number to put in the answer box. "},
        {"type": "text", "text": firstResp},
      ],
    }
  ],
  max_tokens=1000,
)

secondResp = response.choices[0].message.content

print(firstResp+"\n ------------------------- \n"+secondResp)


file_path = 'output.txt'
new_content = secondResp

with open(file_path, 'w') as file:
    file.write(new_content)
