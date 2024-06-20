seconds = int(input())
hrs = seconds//3600
seconds = seconds%3600
mins = seconds//60
seconds = seconds%60
print(hrs,'Hrs',mins,'mins',seconds,'secs')