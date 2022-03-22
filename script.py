import yaml
import requests
from bs4 import BeautifulSoup
import requests_cache

requests_cache.install_cache('invocateur_cache')


class LOLScraper(object):

    def __init__(self, url):
        self. url = url
        self.data = []

    def get_request(self):
        return requests.get(self.url).text.strip()

    def get_soup(self):
        return BeautifulSoup(self.get_request(), 'html.parser')
    
    @staticmethod
    def clean(dirty_item):
        return dirty_item.get_text().strip().replace('\n', '')
        
    def get_title(self, page):
        title = self.clean(page.h1)
        return title

    def get_table_content_link(self, page):
        link_table = []
        ul = page.find(id="toc").ul.find_all(class_="toctext")
        for link in ul:
            link_table.append(link.text)
            # print(link)
        return link_table
    
    def get_color_def(self, page):
        color_table = {}
        colors_tr = page.find(class_='wikitable champions-list-legend').tbody.find_all('tr')
        for item in colors_tr[1:]:
            color = list(map(self.clean, item))
            color_table[color[1]] = color[3]
        return color_table
        
    def get_champions(self, page):
        champ_table = {}
        champs_tr = page.find(class_='article-table').tbody.find_all('tr')
        for item in champs_tr[1:]:
            champ = list(map(self.clean, item))
            champ_table[champ[1]] = {
                'classes': champ[3],
                'release date': champ[5],
                'last changed': champ[7],
                'bue essence': champ[9],
                'rp': champ[11],
            }
        return champ_table

    def get_list_scrapped_champions(self, content):
        data = []
        ul = content.find(class_="columntemplate").ul.find_all("li")
        for li in ul:
            data.append(li.text)
        return(data)
    
    def get_all_page(self):
        page = self.get_soup().find(class_='page__main')
        self.data = {
            'title': self.get_title(page),
            'table content': self.get_table_content_link(page),
            'colors definition': self.get_color_def(page),
            'champions': self.get_champions(page),
            'Scraped champions': self.get_list_scrapped_champions(page)
        }
        
        return self.data
        

        


if __name__ == "__main__":

    solution = LOLScraper(r'https://leagueoflegends.fandom.com/wiki/List_of_champions').get_all_page()
    # for key, value in solution.items():
    #     pprint(key, ": ", value)
    print(yaml.dump(solution, sort_keys=False, default_flow_style=False))
    
