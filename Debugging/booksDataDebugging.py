# -*- coding: utf-8 -*-
##### DO NOT MODIFY THESE LINES #####
# set up data
booksData = [{"title":"The Arabian Nights (New Deluxe Edition)","author_array":["Muhsin Mahdi", "Husain Haddawy"],"num_chapters":35,"num_pages":560},{"title":"Things Fall Apart","author_array":["Chinua Achebe"],"num_chapters":25,"num_pages":209},{"title":"Pride and Prejudice","author_array":["Jane Austen"],"num_chapters":61,"num_pages":353}]
# initializes 5 variables to be filled in
totalBooks = 0
totalPages = 0
avgPagesPerBook = 0.0
avgChaptersPerBook = 0.0
avgAuthorsPerBook = 0.0
titleOfLongestBook = ""
#####################################


# Edit this section:
# Currently finds two of the five values

totalBooks = len(booksData)
for book in booksData:
    totalPages += book["num_pages"]


##### DO NOT MODIFY THESE LINES #####
# prints final value of the five variables
print("Total number of books: " + str(totalBooks))
print("Total number of pages: " + str(totalPages))
print("Average number of pages per book: " + str(avgPagesPerBook))
print("Average number of chapters per book: " + str(avgChaptersPerBook))
print("Average number of authors per book: " + str(avgAuthorsPerBook))
print("Title of longest book (by pages): " + titleOfLongestBook)
#####################################


### SOLUTION:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
booksData = [{"title":"The Arabian Nights (New Deluxe Edition)","author_array":["Muhsin Mahdi", "Husain Haddawy"],"num_chapters":35,"num_pages":560},{"title":"Things Fall Apart","author_array":["Chinua Achebe"],"num_chapters":25,"num_pages":209},{"title":"Pride and Prejudice","author_array":["Jane Austen"],"num_chapters":61,"num_pages":353}]
# initializes 5 variables to be filled in
totalBooks = 0
totalPages = 0
totalChapters = 0
avgPagesPerBook = 0.0
avgChaptersPerBook = 0.0
avgAuthorsPerBook = 0.0
titleOfLongestBook = ""
#####################################


# Edit this section:
# Currently finds two of the five values

totalBooks = len(booksData)
total_authors = 0
longest_book = 0
for i in range(len(booksData)):
    totalPages += booksData[i]["num_pages"]
    totalChapters += booksData[i]["num_chapters"]
    total_authors += len(booksData[i]["author_array"])
    if booksData[i]["num_pages"] > longest_book:
        longest_book =  booksData[i]["num_pages"]
        titleOfLongestBook = booksData[i]["title"]


avgPagesPerBook = totalPages / totalBooks
avgChaptersPerBook = totalChapters / totalBooks
avgAuthorsPerBook = total_authors / totalBooks

##### DO NOT MODIFY THESE LINES #####
# prints final value of the five variables
print("Total number of books: " + str(totalBooks))
print("Total number of pages: " + str(totalPages))
print("Average number of pages per book: " + str(avgPagesPerBook))
print("Average number of chapters per book: " + str(avgChaptersPerBook))
print("Average number of authors per book: " + str(avgAuthorsPerBook))
print("Title of longest book (by pages): " + titleOfLongestBook)
#####################################
