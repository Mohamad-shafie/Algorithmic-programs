# Question Link: https://quera.org/problemset/275506?tab=description
import math


numbers_of_chapter = int(input())
chapters = input()
chapters = list(map(int, chapters.split(" ")))
pages = 0

for chapter in chapters:
    pages += math.ceil(chapter / 2)

print(pages)