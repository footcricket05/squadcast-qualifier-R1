# Squadcast Challenge Solutions

This repository contains solutions to the Squadcast coding challenges. The solutions are implemented in Python, but you can use any programming language as specified. Each solution includes API calls, data processing, and submission of results as per the requirements.

## Table of Contents
1. [Instructions](#instructions)
2. [Questions and Solutions](#questions-and-solutions)
   - [Question 1: Find the Better Location](#question-1-find-the-better-location)
   - [Question 2: Find the IP Address Written in Words](#question-2-find-the-ip-address-written-in-words)
   - [Question 3: Decrypt the Encrypted Message](#question-3-decrypt-the-encrypted-message)
3. [Setup and Execution](#setup-and-execution)
4. [Additional Resources](#additional-resources)

---

## Instructions

- You have **75 minutes** to solve all questions.
- Questions can be solved in **any order**.
- Each question has the **same weight**.
- Solutions can be implemented in **any language**. (Squadcast recommends Golang).
- Use **internet resources** for assistance, if needed.
- Code for each solution should be submitted in the request body of the submission request.
- Make sure to **pass the extension** of the programming language in the submission URL (e.g., `extension=py` for Python).
- Join the Squadcast [Discord server](https://discord.gg/YKecYphK) for updates or announcements.

---

## Questions and Solutions

### Question 1: Find the Better Location

**Objective:** Determine which of two cities is a better location based on a specified weather condition.

**API Endpoints:**
- Get city names and condition: `https://quest.squadcast.tech/api/RA2111032010006/weather`
- Get weather details for a city: `https://quest.squadcast.tech/api/RA2111032010006/weather/get?q=city_name`

**Conditions:**
- `hot`: Higher temperature
- `cold`: Lower temperature
- `windy`: Higher wind value
- `rainy`: Higher rain value
- `sunny`: Lower cloud cover
- `cloudy`: Higher cloud cover

**Submission URL:** `https://quest.squadcast.tech/api/RA2111032010006/submit/weather?answer={your_answer}&extension={extension_used}`

**Example Code:**
```python
# import requests and other necessary libraries here
# define and implement the solution code for this question
# and submit as per the instructions provided above
```

---

### Question 2: Find the IP Address Written in Words

**Objective:** Extract and parse an IP address written in words from a passage, then submit it in standard IPv4 format.

**API Endpoints:**
- Get passage: `https://quest.squadcast.tech/api/RA2111032010006/worded_ip`

**Submission URL:** `https://quest.squadcast.tech/api/RA2111032010006/submit/worded_ip?answer={your_answer}&extension={extension_used}`

**Example Code:**
```python
# import requests, re, and other necessary libraries
# define and implement the solution to extract and format IP address
# and submit as per the instructions provided above
```

---

### Question 3: Decrypt the Encrypted Message

**Objective:** Decrypt a message encrypted with the Fernet method, replace Unicode representations of emojis with actual emojis, and submit the result.

**API Endpoints:**
- Get payload and decryption key: `https://quest.squadcast.tech/api/RA2111032010006/emoji`

**Submission URL:** `https://quest.squadcast.tech/api/RA2111032010006/submit/emoji?answer={your_answer}&extension={extension_used}`

**Example Code:**
```python
# import requests, cryptography, re, and other necessary libraries
# define and implement the solution to decrypt and convert emoji codes
# and submit as per the instructions provided above
```

---

## Setup and Execution

### Prerequisites
- Python 3.x
- `requests`, `re`, `cryptography`, and `beautifulsoup4` libraries (for Python). Install them via pip if necessary:
  ```bash
  pip install requests cryptography beautifulsoup4
  ```

### Running the Solutions
1. Clone the repository.
2. Replace the code in each question’s solution template as per instructions.
3. Run each script in your command line to check if it fetches, processes, and submits correctly.
4. Verify the submission responses for successful execution.

---

## Additional Resources

- [Fernet Encryption](https://cryptography.io/en/latest/fernet/) for understanding the decryption process.
- [IPv4 Address Validation](https://en.wikipedia.org/wiki/IPv4#Address_representations) for IP address formatting.
- Join the Squadcast [Discord server](https://discord.gg/YKecYphK) for support and announcements.

---

**Note:** Ensure all code submitted is complete and well-commented for clarity.
