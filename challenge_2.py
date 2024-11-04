import requests
import re

# API endpoints
passage_url = "https://quest.squadcast.tech/api/RA2111032010006/worded_ip"
submission_url = "https://quest.squadcast.tech/api/RA2111032010006/submit/worded_ip"

# Mapping for word-to-digit conversion
word_to_digit = {
    "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
    "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9",
    "point": "."
}

# Step 1: Get the passage
response = requests.get(passage_url)
if response.status_code == 200:
    passage = response.text
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
    exit()

# Step 2: Extract the IP address in worded format
words = passage.split()
ip_segments = []
ip_address = ""
for word in words:
    if word in word_to_digit:
        ip_segments.append(word_to_digit[word])
    elif ip_segments:
        # If we hit a non-IP word after starting, reset if not valid
        ip_address = ''.join(ip_segments)
        octets = ip_address.split('.')
        if len(octets) == 4 and all(o.isdigit() and 0 <= int(o) <= 255 for o in octets):
            # Valid IP found
            break
        else:
            # Reset if invalid sequence
            ip_segments = []

# Format IP address if valid
ip_address = '.'.join(octets) if len(octets) == 4 else None
if not ip_address:
    print("Error: Unable to extract a valid IP address from passage.")
    exit()

# Print the validated IP address
print("Validated IP Address:", ip_address)

# Step 3: Prepare the submission
answer = ip_address
extension_used = "py"
submission_url_with_params = f"{submission_url}?answer={answer}&extension={extension_used}"

# Code for submission
code = """
import requests
import re

word_to_digit = {
    "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
    "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9",
    "point": "."
}

response = requests.get("https://quest.squadcast.tech/api/RA2111032010006/worded_ip")
words = response.text.split()
ip_segments = []
ip_address = ""
for word in words:
    if word in word_to_digit:
        ip_segments.append(word_to_digit[word])
    elif ip_segments:
        ip_address = ''.join(ip_segments)
        octets = ip_address.split('.')
        if len(octets) == 4 and all(o.isdigit() and 0 <= int(o) <= 255 for o in octets):
            break
        else:
            ip_segments = []
"""

headers = {
    "Content-Type": "text/plain"
}

# Step 4: Submit the answer
submission_response = requests.post(submission_url_with_params, headers=headers, data=code)

# Print submission response
if submission_response.status_code == 200:
    print("Submission successful:", submission_response.json())
else:
    print(f"Submission failed. Status code: {submission_response.status_code}")
    print("Response text:", submission_response.text)
