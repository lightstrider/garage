rt = False #do you want to see the rotten tomatoes as well?
import webbrowser
movies = []
go = True
count = 0
while go:
  movie_name = raw_input("What movie? Say 'stop' to stop")
  if ((count == 5)|(movie_name == "stop")):
    go = False
  else:
    movies.append(movie_name)
    count+=1
for i in movies:
  adjusted_name=i.replace(" ","%20")
  parents_link = 'http://www.google.com/search?safe=strict&hl=en&q=imdb%20parents%20guide%20{}&btnI'.format(adjusted_name)
  webbrowser.open(parents_link)
  if rt:
    rotten_link = 'http://www.google.com/search?safe=strict&hl=en&q=rotten%20tomatoes%20{}&btnI'.format(adjusted_name)
    webbrowser.open(rotten_link)
