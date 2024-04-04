# Amazon Reviews Scraper

This Python script is designed to scrape Amazon product reviews from various domains (e.g., .com, .co.uk) using the provided product IDs. It downloads HTML pages containing reviews for specified products and saves them locally.

## Prerequisites

- Python 3.x
- Required Python packages:
  - argparse
  - os
  - sys
  - codecs
  - urllib (urllib.request, urllib.error)
  - socket
  - contextlib
  - time

## Usage

### Command Line Arguments

The script accepts the following command line arguments:

- `-d, --domain`: Domain from which to download the reviews (Default: com).
- `-f, --force`: Force download even if already successfully downloaded.
- `-r, --maxretries`: Max retries to download a file (Default: 3).
- `-t, --timeout`: Timeout in seconds for HTTP connections (Default: 180).
- `-p, --pause`: Seconds to wait between HTTP requests (Default: 5).
- `-m, --maxreviews`: Maximum number of reviews per item to download (Default: unlimited).
- `-o, --out`: Output base path for saving downloaded HTML files (Default: amazonreviews).
- `-c, --captcha`: Retry on captcha pages until captcha is not asked (Default: skip).
- `ids`: Product IDs for which to download reviews.

### Example Usage

```
python amazon_reviews_scraper.py -d com -o output_folder B00F9ZQQ8Q B00G5RDU5O
```

This command will download reviews for the products with IDs B00F9ZQQ8Q and B00G5RDU5O from the Amazon.com domain and save the HTML files in the `output_folder`.

## How It Works

The script iterates through each provided product ID and constructs URLs to fetch reviews from Amazon. It downloads HTML pages containing reviews, parses them, and saves them locally. The script handles cases such as retries on failure, timeouts, and captchas.

## Note

This script is for educational purposes only. Make sure to respect Amazon's terms of service and usage policies while scraping data.
