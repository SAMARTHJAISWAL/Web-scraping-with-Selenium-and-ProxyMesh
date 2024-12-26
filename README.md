# Web Scraping Twitter Trends with Selenium, ProxyMesh, and MongoDB

This project scrapes the top 5 trending topics from Twitter's homepage using Selenium with ProxyMesh for IP rotation. Results are stored in MongoDB and displayed on a simple web page.

## Setup
1. Install Python dependencies: `pip install selenium pymongo flask`
2. Set up Twitter account for scraping 
3. Configure ProxyMesh credentials
4. Start MongoDB server
5. Update `config.py` with Twitter, ProxyMesh, and MongoDB details

## Usage
1. Run the Flask app: `python app.py`
2. Navigate to `http://localhost:5000` in browser
3. Click button to scrape trends and view results

## Project Structure
- `config/`: Configuration settings 
- `src/`: Selenium scraper and MongoDB operations
- `app/`: Flask routes and frontend template
- `run.py`: Application entry point

## Key Features
- Selenium automation with ProxyMesh for IP rotation
- MongoDB for data storage 
- Flask web interface to trigger scraping and display trends
