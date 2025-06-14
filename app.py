import google.generativeai as genai

# Uncomment this line and put your api key here:
# genai.configure(api_key="")

model = genai.GenerativeModel('gemini-1.5-flash-latest') 

# Initialize a chat session
chat = model.start_chat(history=[])

# Send messages and get responses
try:
	while True:
		user_msg = str(input("Give your statement: "))
		ai_response = chat.send_message(user_msg)

		print(f"AI response: {ai_response.text}")

		quit_input = str(input("quit? [y/n]: "))
		if quit_input == "y":
			break

except Exception as e:
    print(f"An error occurred during chat: {e}")