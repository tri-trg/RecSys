# RecSys

A self-built recommendation system for learning and experimentation.

## Dataset

This project uses the [MovieLens 32M Dataset](https://grouplens.org/datasets/movielens/32m/) provided by GroupLens Research.
> **Disclaimer:** No guarantees are made to the correctness of the data, its suitability for any particular purpose, or the validity of results based on the use of the data set. The dataset may not be used for any commercial or revenue-bearing purposes.

## Project Structure

```text
RecSys/
├── data/                   # Local dataset storage (ignored by git)
├── src/                    # Main source code directory
│   ├── __init__.py
│   └── dts_fetcher.py      # Automated dataset downloader, extractor, and cleanup
├── .gitignore              # Git ignore rules
├── main.py                 # Central execution pipeline
├── README.md               # Project documentation
└── requirements.txt        # Python dependencies
```

## Installation & Setup

**1. Clone the repository:**

   ```bash
   git clone https://github.com/your-username/RecSys.git
   cd RecSys
   ```

**2. Create and activate a virtual environment:**

   ```bash
   python -m venv .venv
   
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

**3. Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

**1. Fetching the Data**
To securely download and extract the MovieLens 32M dataset into the local `data/` directory, run the fetcher script. The script includes automated chunk streaming, HTTP error handling, and a dynamic progress bar:

```bash
python src/dts_fetcher.py
```

*(Note: The `ml-32m.zip` file is approximately 250MB, and the extracted files will require roughly 1.3GB of local storage.)*

## Roadmap

- [x] Establish secure, automated data ingestion pipeline (`dts_fetcher.py`)
- [ ] Perform Exploratory Data Analysis (EDA) on user/movie interactions
- [ ] Implement baseline recommendation algorithms (e.g., Collaborative Filtering)
- [ ] Evaluate model performance using standard RecSys metrics
