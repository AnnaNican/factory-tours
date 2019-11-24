


# Manufactory Tours

Factories are these magical buildings that produce things, a lot of the things that satisfy our cravings, keep the economy running and are often the pride of nations. Over the years they have been transitioning from symbols of industrial revolutions to scapegoats of climate change.  They do not always have the prettiest architecture, yet some have been the nucleus of innovation in construction. Lot&apos;s of things changed in the factories - including the fact that there are fewer and fewer humans working there. This project maps the factories that are open for visits to spur on visits to the places that make our "stuff". 

The app is [hosted on Heroku](https://manufactory-app.herokuapp.com/)


### Styling
    * font: Indie Flower https://fonts.google.com/specimen/Indie+Flower?selection.family=Indie+Flower
    * charts:[Chart.xkcd | xkcd styled chart lib](https://timqian.com/chart.xkcd/#getting_started)
    * illustration: https://dribbble.com/shots/5077105-Conveyor-Belt-Insurance?utm_source=Clipboard_Shot&utm_campaign=agrib&utm_content=Conveyor%20Belt%20Insurance&utm_medium=Social_Share

### Run the app:

The app is build with node.js.
```
node server.js
```

### Scraping

Original data was scraped from :https://www.factorytoursusa.com/ 
```
# run scraper code as
python src/get_factory_data.py
python src/make_json.py
```

