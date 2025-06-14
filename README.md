
# Gemini Chatbot Console App

A simple Python chatbot powered by Google's Gemini 1.5 Flash model using the `google.generativeai` API.

## Features

- Interactive console-based chat
- Supports session history
- Graceful error handling and exit

---

## Setup Instructions (Windows)

### 1. Clone or Download the Project

```bash
git clone git@github.com:JaaJPlayz/ai-simple.git
cd ai-simple
```

### 2. Set Up Virtual Environment

Create a new virtual environment in the project folder:

```bash
python -m venv .venv
```

Activate the virtual environment:

```bash
.venv\Scripts\activate
```

### 3. Install Dependencies

Ensure you have pip upgraded, then install required packages:

```bash
pip install --upgrade pip
pip install google-generativeai
```

### 4. Configure Your API Key

Uncomment and replace the following line in the Python script with your actual API key:

```python
# genai.configure(api_key="your_api_key_here")
```

Alternatively, you can securely load your key using environment variables:

```python
import os
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
```

Set the environment variable in PowerShell or CMD:

```powershell
$env:GOOGLE_API_KEY="your_api_key_here"
```

---

## Run the Application

Activate the virtual environment (if not already active):

```bash
.venv\Scripts\activate
```

## Install the dependencies:

```bash
pip install -r dev-requirements.txt
```

Run the chatbot:

```bash
python chat.py
```

Replace `chat.py` with the filename of your Python script if it's different.

---

## Example Usage

```
Give your statement: Hello!
AI response: Hi there! How can I help you today?
quit? [y/n]: n
```

---

## Notes

* Requires Python 3.8 or later.
* This project uses Gemini 1.5 Flash (`gemini-1.5-flash-latest`) for fast and cost-effective responses.
* Make sure your API key has the necessary permissions enabled on Google Cloud Console.

---

## License

This project is open source under the [MIT License](LICENSE).

```
