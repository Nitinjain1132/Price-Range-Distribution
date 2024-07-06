import pandas as pd
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv(r"C:\Users\HP\Desktop\kartik\Dataset .csv")

# Determine the top three most common cuisines
top_cuisines = data['Cuisines'].str.split(', ').explode().value_counts().head(3)

# Calculate the percentage of restaurants that serve each of the top cuisines
total_restaurants = len(data)
cuisine_percentages = (top_cuisines / total_restaurants) * 100

# Identify the city with the highest number of restaurants
city_counts = data['City'].value_counts()
top_city = city_counts.idxmax()
top_city_count = city_counts.max()

# Calculate the average rating for restaurants in each city
average_ratings = data.groupby('City')['Aggregate rating'].mean()

# Determine the city with the highest average rating
top_avg_rating_city = average_ratings.idxmax()
highest_avg_rating = average_ratings.max()

# Calculate the percentage of restaurants in each price range category
price_range_counts = data['Price range'].value_counts()
percentage_per_price_range = (price_range_counts / total_restaurants) * 100

# Function to create a window for top cuisines and their percentages
def top_cuisines_window():
    window = tk.Tk()
    window.title("Top 3 Cuisines and Their Percentages")

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(top_cuisines.index, cuisine_percentages, color=sns.color_palette("husl", len(top_cuisines)))
    ax.set_xlabel('Cuisines')
    ax.set_ylabel('Percentage of Restaurants')
    ax.set_title('Top 3 Cuisines and Their Percentages')
    
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    window.mainloop()

# Function to create a window for average ratings for top 10 cities by number of restaurants
def top_cities_ratings_window():
    window = tk.Tk()
    window.title("Average Ratings for Top 10 Cities by Number of Restaurants")

    fig, ax = plt.subplots(figsize=(8, 6))
    top_cities = city_counts.head(10)
    top_cities_ratings = average_ratings[top_cities.index]
    ax.bar(top_cities_ratings.index, top_cities_ratings, color=sns.color_palette("husl", len(top_cities_ratings)))
    ax.set_xlabel('Cities')
    ax.set_ylabel('Average Rating')
    ax.set_title('Average Ratings for Top 10 Cities by Number of Restaurants')
    
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    window.mainloop()

# Function to create a window for the distribution of price ranges
def price_range_distribution_window():
    window = tk.Tk()
    window.title("Distribution of Price Ranges Among Restaurants")

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(percentage_per_price_range.index, percentage_per_price_range.values, color=sns.color_palette("husl", len(percentage_per_price_range)))
    ax.set_xlabel('Price Range')
    ax.set_ylabel('Percentage of Restaurants')
    ax.set_title('Distribution of Price Ranges Among Restaurants')
    ax.set_xticks(percentage_per_price_range.index)
    
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    window.mainloop()

# Create the main window with buttons to open each graph window
root = tk.Tk()
root.title("Restaurant Data Analysis")

frame = ttk.Frame(root, padding="10")
frame.pack(fill=tk.BOTH, expand=True)

# Create buttons to open each graph window
ttk.Button(frame, text="Top 3 Cuisines and Their Percentages", command=top_cuisines_window).pack(padx=10, pady=10)
ttk.Button(frame, text="Average Ratings for Top 10 Cities by Number of Restaurants", command=top_cities_ratings_window).pack(padx=10, pady=10)
ttk.Button(frame, text="Distribution of Price Ranges Among Restaurants", command=price_range_distribution_window).pack(padx=10, pady=10)

# Start the main event loop
root.mainloop()
