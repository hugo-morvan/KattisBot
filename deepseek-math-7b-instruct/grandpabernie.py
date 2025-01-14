 def find_year(country):
    return years[countries == country].argsort()[-1] + 1
# Generator time: 3.0590 seconds