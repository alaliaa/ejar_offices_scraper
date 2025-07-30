import time 
import pywhatkit



def send_whatsapp_message(recipient_number, message):
    """
    Schedules a WhatsApp message using pywhatkit.
    """
    now = time.time()
    current_time = time.localtime(now)
    hour_now = current_time.tm_hour 
    minute_now = current_time.tm_min 

    # 1 minute after the current time 
    minute_now += 1 
    pywhatkit.sendwhatmsg(recipient_number, message, hour_now, minute_now, 10, True, 2)


def send_premade_messages_to_offices(offices, message):
    """
    Schedules a WhatsApp message to a list of phone numbers from the scraped offices.
    """
    if not offices:
        print("No offices to send messages to.")
        return

    phone_numbers = [office['Phone'] for office in offices if 'Phone' in office and office['Phone'] != 'N/A']
    unique_phone_numbers = list(set(phone_numbers))
    
    now = time.localtime()
    hour = now.tm_hour
    minute = now.tm_min + 1  # Start scheduling in 1 minute to be safe (increase it if you want to send the message later)

    for number in unique_phone_numbers:
        # Format the number for pywhatkit
        number_str = str(number).strip().replace(" ", "")
        if number_str.startswith('966'):
            full_number = '+' + number_str
        elif number_str.startswith('05'):
            full_number = '+966' + number_str[1:]
        elif number_str.startswith('+'):
            full_number = number_str
        else:
            print(f"Skipping invalid number format: {number}")
            continue

        # Handle time overflow for scheduling
        if minute >= 60:
            hour += minute // 60
            minute %= 60
        if hour >= 24:
            hour %= 24

        print(f"Scheduling premade message to {full_number} at {hour:02d}:{minute:02d}")
        pywhatkit.sendwhatmsg(full_number, message, hour, minute, 15, True, 5)
        
        minute += 1  # Schedule the next message one minute later


def format_offices_for_whatsapp(offices):
    """
    Formats the list of offices into a single string for WhatsApp.
    """
    if not offices:
        return "No offices found."

    message = "*Brokerage Offices Report*\n\n"
    for office in offices:
        message += f"*Name:* {office['Name']}\n"
        message += f"*District:* {office['District']}\n"
        message += f"*Phone:* {office['Phone']}\n"
        message += f"*Rating:* {office['Rating']}\n"
        message += "--------------------\n"
    return message
