from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests
from googlesearch import search  # Additional import for google search

# Initialize Flask app
app = Flask(__name__)

# Define bot response logic
@app.route("/bot", methods=['POST'])
def bot():
    # Get user message
    user_msg = request.values.get('Body', '').lower()

    # Create Twilio Messaging Response
    response = MessagingResponse()

    # Check for user query and respond
    if 'help' in user_msg:
        msg = response.message("This is a WhatsApp bot to provide quick answers! Please type your query to get started.")
    else:
        # Perform a Google search for the user's query
        result = []
        for i in search(user_msg, num=5, stop=5, pause=2):
            result.append(i)

        # Send the search results back to the user
        msg = response.message("\n".join(result))

    return str(response)

# Run Flask app
if __name__ == "__main__":
    app.run(port=5000, debug=True)