##################################################################################
#   Author:           Victoria Heredia
#   Email:            vdheredia1128@my.msutexas.edu
#   Label:            A04
#   Title:            Program 4: Movie Ratings
#   Course:           CMPS 4143 
#   Semester:         Fall 2025
#  
#   Description:
#       This program reads movie titles and ratings from a file, stores the ratings 
#       in a dictionary of lists, and calculates each movie’s average rating. It 
#       then writes a formatted report to report.txt, including all movies and the 
#       top-rated one.        
###################################################################################

with open("Ratings.txt", encoding = "utf-8") as fin:
    movRatings = {}
    for line in fin:

        # This line of code was the first try, it did not work with lines in the text like this: 
        # "Three Billboards Outside Ebbing, Missouri,9" because it has two commas

        # Line of code: section = line.strip().split(',')

        # New version of the line:
        sections = line.strip().rsplit(',', 1)
        movTitle = sections[0]
        movRatingNum = int(sections[1])
        # print(f"Title: {movTitle}, Rating: {movRating}")

        if movTitle not in movRatings:
            movRatings[movTitle] = [] # This line creates a new key for the movie
        movRatings[movTitle].append(movRatingNum) #Then, this line will add the movie's rating to the list

        # Test to ensure movies and ratings were stored correctly in 'movRatings'  
        # print(movRatings)


with open("report.txt","w", encoding="utf-8") as fout:
    
    # write lines to the file using fout.write()
    fout.write("Author: Victoria Heredia\nTitle: Program 4 - Movie Ratings\nCourse: CMPS 4143\nDescription:This program reads movie titles and ratings from a file,\nstores the ratings in a dictionary of lists, and calculates each movie’s\naverage rating. It then writes a formatted report to 'report.txt',\nincluding all movies and the top-rated one.\n")
    fout.write("\nMovie Ratings Report\n")
    fout.write("---------------------------------------------------------------------\n")

    topMovie = ""
    topAverage = 0


    for title, ratings in movRatings.items(): # This line of the for loop sees the 1st element of the tuple go into 'title' 
                                              # and the 2nd element go into 'rating'
        totalRating = 0 
        count = 0

        # This for loop adds each rating to 'totalRating' and 'count' variables
        for r in ratings:
            totalRating += r
            count +=1 

        average = totalRating/count

        # this if statement goes through every movie one at a time
        # if a movie's average rating is better than the current best, then
        # this movie is the new best
        if average > topAverage or (average == topAverage and title < topMovie): #Python automatically knows which letter come first
                                                                                 # and also know how to compare whole words
                                                                                 # title < topMovie is used a tie-breaker: the alphabetically earlier title wins
            topAverage = average
            # print(f"Top Movie is currently: {topMovie}")
            topMovie = title
            # print(f"Title updated to {title}")

        line = f"{title} | Ratings: {ratings} | Average: {average:.2f}\n"
        fout.write(line)
    fout.write(f"\nTop Rated Movie: {topMovie} ({topAverage:.2f})\n")