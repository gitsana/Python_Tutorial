''' '''

import requests
import smtplib

''' Get the emails from the file '''
def get_emails():

    emails = {}
    try:
        email_file = open('emails2.txt', 'r')

        for line in email_file:     # assume there's an email address, name on each line
            (customer_name, customer_email) = line.split(',')
            emails[customer_name] = customer_email.strip()

    except FileNotFoundError as err:
        print("*** Here is your friendly error message", err)

    return emails


''' Get the schedule from the file '''
def get_schedule():
    try:
        schedule_file = open('schedule.txt', 'r')
        schedule_contents = schedule_file.read()

    except FileNotFoundError as err:
        print("*** Here is your friendly error message", err)

    return schedule_contents


''' getting the weather forecast from API, use requests module '''
def get_weather_forecast():
    url = 'http://api.openweathermap.org/data/2.5/weather?q=London&units=imperial&APPID=c71eda8c578cd86f48d4deb98d3462a6'
    weather_request = requests.get(url)
    weather_json = weather_request.json()

    weather_description = weather_json['weather'][0]['description']
    temp_min = weather_json['main']['temp_min']
    temp_max = weather_json['main']['temp_max']
    weather_forecast = 'The weather forecast for tomorrow is ' + weather_description + ' with a high of ' + str(int(temp_max)) + ' and a low of ' + str(int(temp_min)) + '.'
    return weather_forecast


def send_emails(emails, schedule, forecast):
    server = smtplib.SMTP('smtp.gmail.com', '587') # connect to SMPTO server with server and port 587 for TLS encryption

    # start TLS encryption (versus SSL encryption)
    server.starttls()

    from_address = 'sana.experimental@gmail.com'
    # to_address = 'ismail.sana@gmail.com'

    # login
    password = input("What's your password? ")    # instead of saving it
    server.login(from_address, password)

    for to_address, name in emails.items():
        message = "Subject: Welcome to the Circus Group\n"
        message += "Hi, " + name + "\n\n" + forecast
        message += "\n\nThe schedule is:\n\n" + schedule
        message += "\n\nBest,\nThe Circus Team"
        server.sendmail(from_address, to_address, message)

    server.quit()

''' main program '''
def main():
    emails = get_emails()
    print(emails)

    schedule = get_schedule()
    print(schedule)

    forecast = get_weather_forecast()
    print (forecast)

    print('Sending email now')
    send_emails(emails, schedule, forecast)
    print('Email sent')

''' run main part of program '''
main()