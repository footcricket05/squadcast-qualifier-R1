import requests
from cryptography.fernet import Fernet
from bs4 import BeautifulSoup
import re

# API endpoint to get the encrypted payload and key
payload_url = "https://quest.squadcast.tech/api/RA2111032010006/emoji"
submission_url = "https://quest.squadcast.tech/api/RA2111032010006/submit/emoji"

# Step 1: Retrieve the encrypted data and decryption key
response = requests.get(payload_url)

# Parse HTML to extract Key and EncryptedText using BeautifulSoup
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find all <code> tags and extract the one with 'Key:' and 'EncryptedText:'
    code_tags = soup.find_all("code")
    
    key = None
    encrypted_text = None
    for tag in code_tags:
        text = tag.get_text()
        if "Key:" in text:
            key = text.split("Key:")[1].strip()
        elif "EncryptedText:" in text:
            encrypted_text = text.split("EncryptedText:")[1].strip()
    
    # Check if both key and encrypted text were found
    if not key or not encrypted_text:
        print("Error: Could not find key or encrypted text in the response.")
        exit()
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
    exit()

# Step 2: Decrypt the encrypted text using the Fernet key
fernet = Fernet(key.encode())
decrypted_text = fernet.decrypt(encrypted_text.encode()).decode()

# Step 3: Replace unicode representations with actual emojis
def replace_unicode_with_emoji(text):
    # Regex to match U+ emoji patterns
    unicode_pattern = re.compile(r"U\+([0-9A-Fa-f]{4,5})")
    return unicode_pattern.sub(lambda match: chr(int(match.group(1), 16)), text)

# Apply the replacement function
decrypted_with_emojis = replace_unicode_with_emoji(decrypted_text)
print("Decrypted Text with Emojis:", decrypted_with_emojis)

# Step 4: URL encode the answer
from urllib.parse import quote
answer = quote(decrypted_with_emojis)

# Step 5: Prepare the submission URL with the answer
submission_url_with_params = f"{submission_url}?answer={answer}&extension=py"

# Code to submit
code = """
import requests
from cryptography.fernet import Fernet
import re
from bs4 import BeautifulSoup

payload_url = "https://quest.squadcast.tech/api/RA2111032010006/emoji"
response = requests.get(payload_url)
soup = BeautifulSoup(response.text, "html.parser")

code_tags = soup.find_all("code")
key = None
encrypted_text = None
for tag in code_tags:
    text = tag.get_text()
    if "Key:" in text:
        key = text.split("Key:")[1].strip()
    elif "EncryptedText:" in text:
        encrypted_text = text.split("EncryptedText:")[1].strip()

fernet = Fernet(key.encode())
decrypted_text = fernet.decrypt(encrypted_text.encode()).decode()

def replace_unicode_with_emoji(text):
    unicode_pattern = re.compile(r"U\\+([0-9A-Fa-f]{4,5})")
    return unicode_pattern.sub(lambda match: chr(int(match.group(1), 16)), text)

decrypted_with_emojis = replace_unicode_with_emoji(decrypted_text)
"""

headers = {
    "Content-Type": "text/plain"
}

# Step 6: Make the POST request to submit the answer
submission_response = requests.post(submission_url_with_params, headers=headers, data=code)

# Print submission response
if submission_response.status_code == 200:
    print("Submission successful:", submission_response.json())
else:
    print(f"Submission failed. Status code: {submission_response.status_code}")
    print("Response text:", submission_response.text)
