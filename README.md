# Amazon Laptop Scraper

This project scrapes laptop listings from Amazon India using Selenium and stores the extracted data in a CSV file.

## Features

* Extracts product image URL
* Extracts product title
* Extracts product rating
* Extracts product price
* Identifies whether the listing is an advertisement or an organic result
* Saves the output with a timestamped CSV filename

## Technologies Used

* Python
* Selenium
* Pandas

## Installation

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Scraper

```bash
python amazon_scraper.py
```

A CSV file will be generated automatically with the current timestamp.

## Output Fields

* Image
* Title
* Rating
* Price
* Ad_Organic_Result
