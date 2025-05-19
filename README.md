# 🎬 Movie Recommendation System using SVD

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-3.2%2B-green)](https://www.djangoproject.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0%2B-orange)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A content-based movie recommendation system that uses Singular Value Decomposition (SVD) to provide personalized movie suggestions. This project demonstrates how matrix factorization techniques can be applied in recommendation systems.

## ✨ Features

- **SVD-based Recommendations**: Utilizes Singular Value Decomposition for dimensionality reduction and latent factor modeling
- **Web Interface**: Built with Django for easy interaction
- **Scalable**: Can be extended with more users and movies
- **Performance Metrics**: Includes Frobenius norm and Mean Squared Error calculations
- **Top-N Recommendations**: Provides personalized movie suggestions for each user

## 🛠️ Tech Stack

- **Backend**: Python, Django
- **Data Processing**: NumPy, Pandas
- **Machine Learning**: SciPy, scikit-learn
- **Frontend**: Basic HTML/CSS (can be extended)

## 📊 Dataset

The system uses a custom dataset (`movie_ratings_dataset.csv`) containing:
- User IDs
- Movie Names
- Ratings (on a scale of 1-5)

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- pip (Python package manager)
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Movie-recommendation-using-SVD.git
   cd Movie-recommendation-using-SVD
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   If requirements.txt doesn't exist, install the following packages:
   ```bash
   pip install django numpy pandas scipy scikit-learn
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the application**
   Open your browser and go to `http://127.0.0.1:8000/`

## 🎯 Usage

### Getting Recommendations

To get movie recommendations for a specific user, make a GET request to:
```
http://127.0.0.1:8000/recommendations/?user_id=<user_id>
```

### Example

```bash
curl "http://127.0.0.1:8000/recommendations/?user_id=1"
```

### Expected Output
```
Recommended movies for user 1: Movie1, Movie2, Movie3, Movie4, Movie5
```

## 📈 How It Works

1. **Data Preparation**: The system loads the movie ratings data and creates a user-item matrix.
2. **Matrix Factorization**: Applies SVD to decompose the user-item matrix into three matrices (U, Σ, V^T).
3. **Dimensionality Reduction**: Uses a reduced number of latent factors (k=2) to approximate the original matrix.
4. **Prediction**: Reconstructs the rating matrix and generates recommendations based on predicted ratings.

## 📂 Project Structure

```
Movie-recommendation-using-SVD/
├── manage.py            # Django management script
├── movie_ratings_dataset.csv  # Sample dataset
├── Movie recommender system.py  # Core recommendation logic
├── README.md            # This file
├── requirements.txt     # Project dependencies
└── movie_recommender/   # Django app
    ├── __init__.py
    ├── admin.py        # Admin interface configuration
    ├── apps.py         # App configuration
    ├── models.py       # Database models
    ├── tests.py        # Test cases
    ├── urls.py         # URL routing
    └── views.py        # Request handlers
```

## 🤝 Contributing

Contributions are welcome! Here's how you can contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by collaborative filtering and matrix factorization techniques
- Built with the help of Django and scientific Python stack
- Dataset created for demonstration purposes

## 📧 Contact

For any questions or feedback, please contact Sai Harshith at saiharshithvenkata3@gmail.com
