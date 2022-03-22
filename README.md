# Scraping-rendu
Scraping du site https://leagueoflegends.fandom.com/

## Bibliothèques utilisées
* [requests](https://pypi.org/project/requests/)
* [BeautifulSoup](https://pypi.org/project/beautiful/)
* [requests_cache](https://pypi.org/project/requests-cache/)
* [yaml](https://pyyaml.org/wiki/PyYAMLDocumentation)


## Commandes utiles
afficher la page totale :
<pre>print(yaml.dump(solution, sort_keys=False, default_flow_style=False))</pre>
afficher le titre :
<pre>print(yaml.dump(solution, sort_keys=False, default_flow_style=False))</pre>
afficher la table de sommaire :
<pre>print(yaml.dump(solution['Table content'], sort_keys=False, default_flow_style=False))</pre>
afficher la table de correspondance des couleurs :
<pre>print(yaml.dump(solution['Colors definition'], sort_keys=False, default_flow_style=False))</pre>
afficher les champions :
<pre>print(yaml.dump(solution['Champions'], sort_keys=False, default_flow_style=False))</pre>
afficher les champions récemment scraped :
<pre>print(yaml.dump(solution['Scraped champions'], sort_keys=False, default_flow_style=False))</pre>

## Tentative d'ajout de couleur en console pour bien visualiser les différentes parties scraped
* [colorama](https://pypi.org/project/colorama/)
* [colored](https://pypi.org/project/colored/)
* ...

## Auteur
* Lucas DAVAL alias [@LucasDaval](https://github.com/LucasDaval)
