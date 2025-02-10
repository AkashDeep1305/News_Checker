# News Checker

## Overview
News Checker is a web application that helps users verify whether a news headline is real or fake. The project consists of a **backend** for scraping and training a machine learning model and a **frontend** built with React for user interaction.

## Project Structure
```
news-checker/
│-- backend/
│   │-- app.py          # Backend API for news verification
│   │-- scrapper.py     # Scrapes news headlines and saves them as a CSV file
│   │-- trainmodel.py   # Trains a model using the CSV data
│   │-- model.h5        # Trained deep learning model
│   │-- vectorizer.pkl  # TF-IDF vectorizer
│
│-- frontend/
│   │-- public/
│   │-- src/
│   │-- package.json    # React dependencies
│     
│-- requirements.txt    # Python dependencies
```

## Backend Setup
The backend is built with Flask and uses machine learning to classify news as real or fake.

### Install Dependencies
1. Navigate to the `backend` directory:
   ```bash
   cd backend
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Backend
Start the backend server:
```bash
python app.py
```

## Training the Model
To train the model using scraped news data:
```bash
python scrapper.py  # Scrapes news headlines and saves them as CSV
python trainmodel.py  # Trains the model and saves it as model.h5
```

## Frontend Setup
The frontend is built using React.

### Install Dependencies
1. Navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```
2. Install the required dependencies:
   ```bash
   npm install
   ```
   **Note:** The `node_modules` folder is not included in the repository. Running `npm install` will download the necessary packages.

### Running the Frontend
Start the frontend React development server:
```bash
npm start
```

## Running the Full Application
To use the News Checker system:
1. Start the backend: `python backend/app.py`
2. Start the frontend: `npm start` inside the `frontend` directory.
3. Open `http://localhost:3000` in a web browser.

