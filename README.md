# 🕵️ Fake News Detector

A web-based fake news detection tool that uses machine learning and pattern recognition to analyze and identify potentially misleading or false news content.

## 🚀 Features

- Paste any news article or headline and get an instant verdict
- Pattern recognition model trained on real and fake news datasets
- Google Search integration to cross-reference news sources
- Clean, simple web interface

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **ML:** scikit-learn (TF-IDF + Passive Aggressive Classifier)
- **Search:** Google Custom Search API
- **Frontend:** HTML, CSS, JavaScript

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/Pprog-png/fake-news-detector-website-implementation.git
cd fake-news-detector-website-implementation
```

### 2. Install Git LFS (for the dataset)

This project uses [Git Large File Storage](https://git-lfs.com) to store the training dataset.

```bash
git lfs install
git lfs pull
```

> This will download `FakeNewsTrainingSetUpdated.csv` (~110MB) automatically after cloning.

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up API credentials

This project uses the **Google Custom Search API** to cross-reference news articles.

You need two credential files in the root of the project:

- `api_key` — Your Google API key
- `search_engine_id` — Your Custom Search Engine ID

**To get these:**
1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Create a project → Enable **Custom Search API**
3. Go to **Credentials** → Create an **API Key**
4. Go to [Programmable Search Engine](https://programmablesearchengine.google.com) → Create a search engine → copy the ID

Create the files like this:
```bash
echo "YOUR_API_KEY_HERE" > api_key
echo "YOUR_SEARCH_ENGINE_ID_HERE" > search_engine_id
```

> ⚠️ **Never share or commit these files.** They are listed in `.gitignore` for your protection.

### 5. Run the app

```bash
python app.py
```

Then open your browser and go to: `http://localhost:5000`

## 📁 Project Structure

```
├── app.py                        # Main Flask application
├── search.py                     # Google Search integration
├── credits                       # Credits and attributions
├── FakeNewsTrainingSetUpdated.csv # Training dataset (stored via Git LFS)
├── api_key                       # Google API key (not in repo)
├── search_engine_id              # Search engine ID (not in repo)
├── requirements.txt              # Python dependencies
├── static/
│   ├── css/                      # Stylesheets
│   ├── scripts/                  # JavaScript
│   └── background1.jpeg          # Background image
└── templates/
    ├── index.html                # Main page
    └── credits.html              # Credits page
```

## 👥 Credits

See `credits` file for full attribution.

## ⚠️ Disclaimer

This tool is for educational purposes. It is not 100% accurate and should not be used as the sole source of truth for determining whether news is real or fake.
