import requests
from bs4 import BeautifulSoup

# API endpoints
base_url = "https://quest.squadcast.tech/api/RA2111032010006"
weather_url = f"{base_url}/weather"
weather_city_url = f"{base_url}/weather/get?q="
submission_url = f"{base_url}/submit/weather"

# Step 1: Get city names and condition
response = requests.get(weather_url)

# Check if the response was successful
if response.status_code == 200:
    try:
        # Parse the HTML response
        soup = BeautifulSoup(response.text, "html.parser")
        city1 = soup.find("code", string=lambda x: x and "City 1" in x).text.split(": ")[1]
        city2 = soup.find("code", string=lambda x: x and "City 2" in x).text.split(": ")[1]
        condition = soup.find("code", string=lambda x: x and "Condition" in x).text.split(": ")[1]
    except Exception as e:
        print("Error: Failed to parse HTML response.")
        print("Exception:", e)
        exit()
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
    print("Response text:", response.text)
    exit()

# Step 2: Get weather data for each city
city1_weather_response = requests.get(f"{weather_city_url}{city1}")
city2_weather_response = requests.get(f"{weather_city_url}{city2}")

# Check if weather data requests were successful
if city1_weather_response.status_code == 200:
    try:
        city1_weather = city1_weather_response.json()
    except requests.exceptions.JSONDecodeError:
        print(f"Error: Failed to decode JSON for {city1} weather data.")
        print("Response text:", city1_weather_response.text)
        exit()
else:
    print(f"Failed to retrieve weather data for {city1}. Status code: {city1_weather_response.status_code}")
    print("Response text:", city1_weather_response.text)
    exit()

if city2_weather_response.status_code == 200:
    try:
        city2_weather = city2_weather_response.json()
    except requests.exceptions.JSONDecodeError:
        print(f"Error: Failed to decode JSON for {city2} weather data.")
        print("Response text:", city2_weather_response.text)
        exit()
else:
    print(f"Failed to retrieve weather data for {city2}. Status code: {city2_weather_response.status_code}")
    print("Response text:", city2_weather_response.text)
    exit()

# Step 3: Determine the better location based on the condition
better_location = None

# Use get() with a default value to prevent KeyError
if condition == "hot":
    better_location = city1 if city1_weather.get("temperature", float('-inf')) > city2_weather.get("temperature", float('-inf')) else city2
elif condition == "cold":
    better_location = city1 if city1_weather.get("temperature", float('inf')) < city2_weather.get("temperature", float('inf')) else city2
elif condition == "windy":
    better_location = city1 if city1_weather.get("wind", float('-inf')) > city2_weather.get("wind", float('-inf')) else city2
elif condition == "rainy":
    better_location = city1 if city1_weather.get("rain", float('-inf')) > city2_weather.get("rain", float('-inf')) else city2
elif condition == "sunny":
    better_location = city1 if city1_weather.get("cloud", float('inf')) < city2_weather.get("cloud", float('inf')) else city2
elif condition == "cloudy":
    better_location = city1 if city1_weather.get("cloud", float('-inf')) > city2_weather.get("cloud", float('-inf')) else city2

if not better_location:
    print("Error: Unable to determine better location based on condition.")
    exit()

# Step 4: Prepare the submission
answer = better_location
extension_used = "py"
submission_url_with_params = f"{submission_url}?answer={answer}&extension={extension_used}"

# Code to submit
code = """
import requests
from bs4 import BeautifulSoup

# API endpoints
base_url = "https://quest.squadcast.tech/api/RA2111032010006"
weather_url = f"{base_url}/weather"
weather_city_url = f"{base_url}/weather/get?q="
submission_url = f"{base_url}/submit/weather"

response = requests.get(weather_url)
soup = BeautifulSoup(response.text, "html.parser")
city1 = soup.find("code", string=lambda x: x and "City 1" in x).text.split(": ")[1]
city2 = soup.find("code", string=lambda x: x and "City 2" in x).text.split(": ")[1]
condition = soup.find("code", string=lambda x: x and "Condition" in x).text.split(": ")[1]

# Logic for fetching weather data and determining better location
"""

headers = {
    "Content-Type": "text/plain"
}

# Step 5: Submit the result with the code
submission_response = requests.post(submission_url_with_params, headers=headers, data=code)

# Print submission response
if submission_response.status_code == 200:
    print("Submission successful:", submission_response.json())
else:
    print(f"Submission failed. Status code: {submission_response.status_code}")
    print("Response text:", submission_response.text)
