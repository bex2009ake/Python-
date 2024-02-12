# import requests
# from bs4 import BeautifulSoup


# num = 1
# url = 'https://leetcode.com/problems/two-sum/'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
# a = soup.find_all('div',class_='flex h-full w-full overflow-y-auto rounded-b')


# print(a)


import openai
openai.api_key = "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"
def chat_with_gpt (prompt):
 response = openai.ChatCompletion.create(
 model="gpt-3.5-turbo",
 messages=[{"role": "user", "content": prompt}]
 )
 return response.choices[0].message.content.strip()
if __name__  == "__main__":
 while True:
   user_input = input ("You: ")
   if user_input.lower() in ["quit", "exit", "bye"]:
     break
   response = chat_with_gpt (user_input)
   print("Chatbot: ", response)