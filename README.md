```markdown
# Web Scraping with Selenium and ProxyMesh

This project demonstrates web scraping of Twitter's "What's Happening" section using Selenium and ProxyMesh. The scraped data is stored in MongoDB and displayed on a simple HTML page.

---

## Overview

### Project Components
1. **Web Scraping with Selenium:** Automates the process of logging into Twitter and fetching the top 5 trending topics under the "What's Happening" section.
2. **ProxyMesh Integration:** Ensures that each scraping request is routed through a different IP address to prevent rate limiting and improve anonymity.
3. **MongoDB Storage:** Stores the scraped data with a unique ID for each run, including:
   - Top 5 trending topics
   - Date and time of the script run
   - The IP address used for the request
4. **HTML Interface:** Displays the results on a webpage with a button to trigger the Selenium script. The webpage also shows a JSON extract of the stored record.

---

## Setup Instructions

### Prerequisites
1. Python 3.x installed on your system.
2. MongoDB installed and running locally or on a remote server.
3. Google Chrome installed with the corresponding version of [ChromeDriver](https://chromedriver.chromium.org/downloads).
4. Twitter account credentials for login (required for accessing "What's Happening").
5. A ProxyMesh account with access to rotating IP proxies.

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/SAMARTHJAISWAL/Web-scraping-with-Selenium-and-ProxyMesh.git
   cd Web-scraping-with-Selenium-and-ProxyMesh
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure ProxyMesh credentials:
   - Update the ProxyMesh credentials in the Selenium script (`src/scraper.py`).

4. Configure MongoDB:
   - Ensure your MongoDB instance is running.
   - Update the MongoDB connection string in the script.

---

## Usage

### 1. Run the Selenium Script
The script fetches Twitter's "What's Happening" section, stores the data in MongoDB, and outputs the results. 

- Run the scraper script:
  ```bash
  python src/scraper.py
  ```

### 2. Launch the Web Interface
The HTML page provides an interface to trigger the Selenium script and display the results.

- Start the Flask server:
  ```bash
  python run.py
  ```

- Open your browser and navigate to `http://127.0.0.1:5000`.

### 3. Using the Web Page
- Click the **"Click here to run the script"** button to run the Selenium script.
- View the results in the following format:
  ```
  These are the most happening topics as on {Date and Time of end of Selenium Script}
  - Name of trend1
  - Name of trend2
  - Name of trend3
  - Name of trend4
  - Name of trend5
  The IP address used for this query was XXX.XXX.XXX.XXX.
  ```

- JSON extract from MongoDB is displayed below the results.

---

## Project Structure

```
Web-scraping-with-Selenium-and-ProxyMesh/
│
├── app/                     # Contains HTML templates and static files
│   ├── templates/
│   │   └── index.html       # HTML page for the web interface
│
├── src/
│   ├── scraper.py           # Selenium script for scraping Twitter
│
├── requirements.txt         # Python dependencies
├── run.py                   # Flask server for the web interface
├── README.md                # Project documentation
```

---

## Important Notes
1. **Twitter Login Required:** Ensure the Selenium script includes your Twitter login credentials for accessing the "What's Happening" section.
2. **ProxyMesh Configuration:** Verify that your ProxyMesh account is active and credentials are correctly configured.
3. **Error Handling:** The script includes basic error handling for login and scraping failures but may require adjustments based on Twitter's dynamic elements or ProxyMesh connectivity issues.

---

## Example Output

### HTML Page
```
These are the most happening topics as on 2024-12-26 10:00:00
- Topic 1
- Topic 2
- Topic 3
- Topic 4
- Topic 5
The IP address used for this query was 123.45.67.89.

JSON Extract:
[
    {
        "_id": { "unique_id": "abc123" },
        "nameoftrend1": "Topic 1",
        "nameoftrend2": "Topic 2",
        ...
    }
]
```

---

## Author
Developed by **Samarth Jaiswal** as part of the Stir Tech Internship application assignment.

For any queries, please reach out via [samarthjaiswal@example.com](mailto:samarthjaiswal@example.com).
```
