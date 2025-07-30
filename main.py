from scraper import scrape_ejar
from whatsapp_utils import send_premade_messages_to_offices, format_offices_for_whatsapp, send_whatsapp_message




if __name__ == "__main__":
    # This link search for all the offices in Riyadh city 

    # The number of pages to scrape (each page contains 10 offices)
    number_of_pages = 1        
    # The number of offices to scrape
    desired_number_of_offices = 5
    # The number of the phone number to send the message to
    my_number = "+9660000000000"
    # Whether to send the message to your own number or to the offices
    send_me = True 
    # A premade message to send to the offices (only used if send_me is False)
    premade_message = "سلام عليكم ورحمة الله "
    # The url to scrape the offices from Riyadh
    target_url = "https://www.ejar.sa/ar/brokerage-offices?region=169&city=196&district=All&name=&field_bo_rating_value=All"


    scraped_offices = scrape_ejar(target_url, number_of_pages,save_to_csv=False)
    number_of_offices = len(scraped_offices)
    print(f"Total number of offices: {number_of_offices}")
    scraped_offices = scraped_offices[:desired_number_of_offices]
    
    if send_me:
        # Send the detailed report to your own number
        whatsapp_message = format_offices_for_whatsapp(scraped_offices)
        send_whatsapp_message(my_number, whatsapp_message) 


    else:
        #  Send a premade message to all scraped offices
        print("\n--- Now sending a premade message to all scraped offices ---")
        send_premade_messages_to_offices(scraped_offices, premade_message)