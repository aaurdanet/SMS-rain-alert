# SMS-rain-alert

This Python script retrieves weather forecast data from OpenWeatherMap and sends a daily SMS alert using Twilio if rain is expected at your location.
Getting Started

To use this script, follow these steps:

Sign Up for OpenWeatherMap API: Obtain an API key from OpenWeatherMap and replace API_KEY in the script with your key.

Set Your Location: Specify your latitude (MY_LAT) and longitude (MY_LONG) in the script to get accurate weather data for your location.

Sign Up for Twilio: Create an account on Twilio and obtain your Account SID (account_sid) and Auth Token (auth_token).

Verify Your Phone Numbers: Verify your phone numbers with Twilio and replace the placeholders in the script (from_ and to) with your Twilio phone numbers.

Run the Script: Execute the script, and it will retrieve the weather forecast for your location. If rain is expected, it will send an SMS alert using Twilio.

Automation

You can host this script on platforms like PythonAnywhere and schedule it to run automatically every day in the morning using the task scheduler feature.
Dependencies

Python 3.x
requests library (install using pip install requests)
Twilio Python SDK (twilio package) (install using pip install twilio)

Disclaimer

Please note that this script requires internet access to retrieve weather data and Twilio credits to send SMS alerts. Charges may apply for using Twilio services.
