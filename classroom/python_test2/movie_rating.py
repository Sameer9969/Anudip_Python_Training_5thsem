"""Problem 10: Movie Rating Analysis System 
Problem Statement 
Ratings given by users for movies are stored below. 
Sample Data 
ratings = { 
    "Inception": 4.8, 
    "Avatar": 4.3, 
    "Titanic": 4.5, 
    "Joker": 4.7, 
    "Frozen": 3.8, 
    "Interstellar": 4.9, 
    "Dune": 4.6, 
    "Up": 4.1, 
    "Coco": 4.4, 
    "Cars": 3.9 
} 
Tasks 
1. Display movies rated above 4.5.  
2. Find the highest-rated movie.  
3. Find the lowest-rated movie.  
4. Calculate average rating.  
5. Create a recommendation list (rating ≥ 4.5).  
Sample Output 
Movies Rated Above 4.5: 
Inception 
Joker 
Interstellar 
Dune 
 
Highest Rated Movie: 
Interstellar (4.9) 
 
Lowest Rated Movie: 
Frozen (3.8) 
 
Average Rating: 4.4 
 
Recommended Movies: 
['Inception', 'Titanic', 'Joker', 'Interstellar', 'Dune']"""

#===================================================
ratings = { 
    "Inception": 4.8, 
    "Avatar": 4.3, 
    "Titanic": 4.5, 
    "Joker": 4.7, 
    "Frozen": 3.8, 
    "Interstellar": 4.9, 
    "Dune": 4.6, 
    "Up": 4.1, 
    "Coco": 4.4, 
    "Cars": 3.9 
}

#===================================
# 1. Display movies rated above 4.5.
#===================================
print("Movies Rated Above 4.5:")
for movie in ratings:
    if ratings[movie] > 4.5:
        print(movie)
#===================================
# 2. Find the highest-rated movie.
#===================================
highest = 0
for movie in ratings:
    if ratings[movie] > highest:
        highest = ratings[movie]
        highest_movie = movie
print("\nHighest Rated Movie:")
print(highest_movie, "(", highest, ")")
#===================================
# 3. Find the lowest-rated movie.
#===================================
lowest = float('inf')
for movie in ratings:
    if ratings[movie] < lowest:
        lowest = ratings[movie]
        lowest_movie = movie
print("\nLowest Rated Movie:")
print(lowest_movie, "(", lowest, ")")
#===================================
# 4. Calculate average rating.
#===================================
total = 0
for movie in ratings:
    total += ratings[movie]
average = total / len(ratings)
print("\nAverage Rating:", average)
#===================================
# 5. Create a recommendation list (rating ≥ 4.5).
#===================================
print("\nRecommended Movies:")
for movie in ratings:
    if ratings[movie] >= 4.5:
        print(movie)
#===================================

