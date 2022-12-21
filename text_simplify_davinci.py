import openai

def simplify_sentence(sentence):
  # Set OpenAi API key
  openai.api_key = "Api-Key"

  # Set the model and prompt
  model_engine = "text-davinci-002"
  prompt = f"Take this string of text and simplify it as much as possible: {sentence}"

  # Use the OpenAI API to generate a response
  completion = openai.Completion.create(
      engine=model_engine,
      prompt=prompt,
      max_tokens=1024,
      temperature=0.5,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
  )

  # Get the response from the API
  response = completion.choices[0].text

  # Print the response
  return response

# Test the function by letting the user input a sentence

sentence = input("Enter a sentence: ")
simplified_sentence = simplify_sentence(sentence)
print(simplified_sentence)
