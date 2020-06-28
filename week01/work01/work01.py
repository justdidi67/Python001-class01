import requests
from bs4 import BeautifulSoup as bs
import pandas


def get_page(url):
    movies_list = []
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "cookie": "rewardsn=; wxtokenkey=777; wxuin=2624901963; devicetype=Windows10x64; version=62090070; lang=zh_CN; pass_ticket=TbNqF6zgmcLvbpMKA3pwn8f/6WXMi4C/l6ic0bBPeo9UR1JLNUbEThx0lyCJBm2T; __guid=166713058.138131931348501380.1593316983737.2498; wap_sid2=CMum0+MJElx4SEV6OEJLX2RyLWsxQ1J3eDVqdE0zR1JSZFAwWDdFMmY0TEJlQ2NIRlNzVTMwVURnZ1R5VnlZbV9VaDFPSXA5VXFKcE9TenlRXzk3clRCbHNoUFl5aXNFQUFBfjDBseD3BTgNQAE=; monitor_count=2"
    }
    res = requests.get(url, headers=header)
    bs_info = bs(res.text, "html.parser")
    for movie in bs_info.find_all('div', class_='movie-hover-info', limit=10):
        movie_info = movie.find_all(class_='movie-hover-title')
        movie_name = movie_info[0].find(class_='name').text.strip()
        movie_type = movie_info[1].text.strip()
        time = movie_info[3].text.strip()
        movie = {'movie_name': movie_name, 'movie_type': movie_type, 'time': time}
        movies_list.append(movie)
    return movies_list

url = 'https://maoyan.com/films?showType=3'
movie_list = get_page(url)
print(movie_list)

movies = pandas.DataFrame(movie_list)
movies.to_csv('./work01.csv',encoding='utf_8_sig',index=False)