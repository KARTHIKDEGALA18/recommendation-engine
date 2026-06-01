# Context-Aware Movie Recommendation Engine 🎬

## Overview

This project is a Movie Recommendation Backend developed using FastAPI.

The system provides movie recommendations based on user preferences and supports genre filtering, movie analytics, similarity-based recommendations, and caching.

## Features

* Personalized Movie Recommendations
* Genre-Based Filtering
* Similar Movie Retrieval
* Movie Analytics Dashboard
* Recommendation Caching
* REST API Architecture

## APIs

### Get Movie Recommendations

/recommend/{user_id}

### Genre Filtering

/recommend/{user_id}?genre=Sci-Fi

### Analytics

/analytics

### Similar Movies

/similar/{movie_id}

## Tech Stack

* Python
* FastAPI
* JSON
* Git & GitHub

## Project Structure

api/

services/

data/

README.md

## Future Improvements

* TensorFlow Recommenders
* MovieLens Dataset Integration
* User Embeddings
* ANN Search
* Redis Caching
* Real-Time Recommendations
