"""3. Movie Review Sentiment Analyzer 
Problem Statement 
Movie reviews are stored as follows: 
reviews = [ 
    "excellent movie", 
    "average story", 
    "excellent acting", 
    "poor direction", 
    "excellent visuals", 
    "poor screenplay", 
    "good music", 
    "excellent climax", 
    "average performance", 
    "good cinematography" 
] 
Requirements 
Create the following functions: 
1. count_sentiments(reviews) 
Counts: 
• Excellent  
• Good  
• Average  
• Poor reviews  
2. most_common_word(reviews) 
Returns the most frequently occurring word. 
3. longest_review(reviews) 
Returns the review containing the maximum number of characters. 
4. reviews_with_keyword(reviews, keyword) 
Displays all reviews containing a given keyword. 
Sample Output 
Excellent Reviews: 4 
Good Reviews: 2 
Average Reviews: 2 
Poor Reviews: 2 
 
Most Common Word: 
excellent 
 
Longest Review: 
good cinematography 
 
Reviews containing 'excellent': 
excellent movie 
excellent acting 
excellent visuals 
excellent climax"""

reviews = [ 
    "excellent movie", 
    "average story", 
    "excellent acting", 
    "poor direction", 
    "excellent visuals", 
    "poor screenplay", 
    "good music", 
    "excellent climax", 
    "average performance", 
    "good cinematography" 
]

#========================================
# 1.count_sentiments(reviews) 
#Counts: 
#• Excellent  
#• Good  
#• Average  
#• Poor reviews  
#========================================
def count_sentiments(reviews):
    excellent_count = 0
    good_count = 0
    average_count = 0
    poor_count = 0
    for review in reviews:
        if "excellent" in review:
            excellent_count += 1
        elif "good" in review :
            good_count += 1
        elif "average" in review:
            average_count += 1
        else:
            poor_count += 1
    return {
        "excellent": excellent_count,
        "good": good_count,
        "average": average_count,
        "poor": poor_count
    }
#=============================================
# 2.  most_common_word(reviews) 
# Returns the most frequently occurring word.
# ============================================
def most_common_word(reviews):
    word_count = {}
    for review in reviews:
        words = review.split()
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    return max(word_count, key=word_count.get)
#=============================================
#3. longest_review(reviews) 
# Returns the review containing the maximum number of characters. 
#==============================================
def longest_review(reviews):
    longest = reviews[0]
    for review in reviews:
        if len(review) > len(longest):
            longest = review
    return longest
#================================================
# 4. reviews_with_keyword(reviews, keyword)
# Displays all reviews containing a given keyword.
#================================================
def reviews_with_keyword(reviews, keyword):
    print("Reviews containing '" + keyword + "':")
    for review in reviews:
        if keyword in review:
            print(review)
#================================================   
# function call
#================================================
result = count_sentiments(reviews)

print("Excellent Reviews:", result["excellent"])
print("Good Reviews:", result["good"])
print("Average Reviews:", result["average"])
print("Poor Reviews:", result["poor"])

print("\nMost Common Word:")
print(most_common_word(reviews))

print("\nLongest Review:")
print(longest_review(reviews))

print("\n")
reviews_with_keyword(reviews, "excellent")