# InfoCrwaler

## Overview

This project is developed for the **Information Management Group** at **IIT Roorkee (IITR)**. It aims to build a robust information management system for retrieving and processing data from multiple product websites. This system enables enhanced decision-making and improved operational efficiency for the team. The project leverages cutting-edge technologies, including AI-driven crawlers, scraping tools, and ethical data collection practices.

---

## Features

- **Web Crawling**: Efficient crawling of product websites for structured data using multiple fetchers (BeautifulSoup, Selenium, Crawl4AI, and ScrapeGraphAI).
- **Data Cleaning**: Automatic cleaning and normalization of the data to ensure consistency and reliability.
- **Proxy & User-Agent Rotation**: To prevent getting blocked while scraping, the system uses proxy rotation and random user-agent generation.
- **Ethics Check**: Ethical guidelines are implemented to ensure only permitted websites are crawled.
- **Scalable Architecture**: Designed to handle large-scale web scraping and data processing efficiently.

---

## Architecture

The architecture consists of several core components that work together to retrieve, clean, and process data:

1. **Crawler Fetchers**:
   - **BeautifulSoup Fetcher**: Simple HTML scraping using requests with user-agent and proxy rotation.
   - **Selenium Fetcher**: Scrapes JavaScript-heavy pages using Selenium.
   - **Crawl4AI Fetcher**: Uses an AI-powered crawler for handling modern web applications with heavy JavaScript.
   - **ScrapeGraphAI Fetcher**: Fetches highly structured data using AI-driven scraping techniques.

2. **Data Processing**:
   - **Cleaners**: Clean and normalize the scraped data for further processing and analysis.
   - **Proxy Management**: Manages the list of proxies to ensure that scraping operations are performed anonymously and efficiently.
   
3. **Ethics and Filtering**:
   - **Ethics Check**: Filters out URLs that do not adhere to ethical scraping practices.
   
4. **Data Storage**:
   - **Output Storage**: Crawled and cleaned data is stored in JSON format, allowing easy access and future analysis.

---

## Technologies Used

- **Python**: Core language for development.
- **BeautifulSoup**: HTML parsing for simple websites.
- **Selenium**: For scraping JavaScript-heavy websites.
- **Crawl4AI**: AI-powered crawling for modern applications.
- **ScrapeGraphAI**: Extracts highly structured data with AI models.
- **Asyncio**: For concurrent execution of crawlers.
- **Requests**: For HTTP requests and web scraping.
- **Tenacity**: Retry logic to ensure reliability during scraping.
- **Pydantic**: For data modeling and validation.
- **Logging**: For detailed logs to track crawler performance and errors.
- **Proxies and User-Agent Rotation**: For anti-blocking mechanisms.

---

## Setup Instructions

### Prerequisites

1. **Python 3.8+**: Ensure Python is installed.
2. **Environment Variables**: Set up your environment variables (`SGAI_API_KEY` for ScrapeGraphAI).
3. **Required Libraries**: Install the required dependencies using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

4. **Proxies File**: Ensure the `proxy.json` file is available in the correct directory. This file contains a list of proxies used for web scraping.

---

## Running the Project

1. **Setup the Seed URLs**: Create or update your `urls.json` file with the base URLs of the product websites to be crawled.

    Example format:

    ```json
    {
        "example_product": {
            "base_url": "https://www.amazon.com/product"
        }
    }
    ```

2. **Run the Crawlers**:

   To start crawling, run the `main.py` script which will initialize the crawling process and save the crawled URLs and data.

   ```bash
   python main.py
