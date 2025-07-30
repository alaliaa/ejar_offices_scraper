# Ejar Web Scraper and WhatsApp Notifier

This project contains a Python script that scrapes real estate brokerage office information from the Ejar website (ejar.sa) and can send notifications and data via WhatsApp.



## Installation

1.  Clone this repository or download the source code.
2.  Install the required Python packages using pip:

    ```bash
    pip install -r requirements.txt
    ```

## How to Run the Script

1.  **Important:** For the WhatsApp functionality to work, you must be logged into WhatsApp Web on Chrome. `pywhatkit` will open a new tab and use your existing session to send the message.

2.  Open the `main.py` file and configure the parameters within the `if __name__ == "__main__":` block at the bottom of the file:
    - `number_of_pages`: Set the number of pages you want to scrape.
    - `my_number`: Enter your full phone number in international format (e.g., `+9665...`) to receive the detailed report.
    - `send_me`: 
        - Set to `True` if you want to send the formatted list of offices to `my_number`.
        - Set to `False` if you want to send a premade message to all the scraped office numbers.
    - `target_url`: The URL from `ejar.sa` to scrape. The default is for offices in Riyadh.
    - `save_to_csv` (in the `scrape_ejar` function call): Set to `True` if you want to save the scraped data to `ejar_offices.csv`.
    - `desired_number_of_offices`: Limit the number of offices to be processed for sending messages.
    - `premade_message`: If `send_me` is `False`, this is the message that will be sent to the offices.

3.  Run the script from your terminal:

    ```bash
    python main.py
    ```

## Project Structure

The project is organized into three main Python files:

### `main.py`
- This is the main entry point of the application.
- It handles the overall workflow:
  1.  Sets the configuration parameters (URL, number of pages, etc.).
  2.  Calls the scraping function from `scraper.py`.
  3.  Based on the `send_me` flag, it either:
      - Formats and sends a detailed report to your number using functions from `whatsapp_utils.py`.
      - Sends a premade message to all scraped offices using functions from `whatsapp_utils.py`.

### `scraper.py`
- Contains all the web scraping logic.
- `scrape_ejar(url, number_of_pages, save_to_csv=False)`:
  -   Takes an Ejar URL and the number of pages to scrape.
  -   Returns a list of dictionaries, where each dictionary represents a brokerage office.
  -   If `save_to_csv` is `True`, it creates `ejar_offices.csv`.

### `whatsapp_utils.py`
- Contains all the functions related to sending WhatsApp messages.
- `send_whatsapp_message(recipient_number, message)`:
  -   Sends a given `message` to the `recipient_number` via WhatsApp.
- `send_premade_messages_to_offices(offices, message)`:
  -   Iterates through the list of `offices`, extracts unique phone numbers, and sends them a `message`.
- `format_offices_for_whatsapp(offices)`:
  -   Takes the list of `offices` and formats it into a clean, readable string for a WhatsApp message.

