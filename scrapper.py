import logging
from linkedin_jobs_scraper import LinkedinScraper
from linkedin_jobs_scraper.events import Events, EventData
from linkedin_jobs_scraper.query import Query, QueryOptions

# Change root logger level (default is WARN)
logging.basicConfig(level = logging.INFO)

# Definir un array vacío
def on_data(data: EventData):
    # Llenar el array con cada instancia de data
    print('[ON_DATA]', data.title, data.company, data.date, data.link, len(data.description))


def on_error(error):
    print('[ON_ERROR]', error)


def on_end():
    print('[ON_END]')


scraper = LinkedinScraper(
    chrome_options=None,  # You can pass your custom Chrome options here
    headless=True,  # Overrides headless mode only if chrome_options is None
    max_workers=1,  # How many threads will be spawned to run queries concurrently (one Chrome driver for each thread)
    slow_mo=0.4,  # Slow down the scraper to avoid 'Too many requests (429)' errors
)

# Add event listeners

# Evento que para detectar cada oferta
scraper.on(Events.DATA, on_data)

scraper.on(Events.ERROR, on_error)
scraper.on(Events.END, on_end)

queries = [
    Query(
        # Categoria que estás buscando
        query='Engineer',
        options=QueryOptions(
            # Pais donde quieres buscar
            locations=['United States'],
            # En caso sean imágenes o css
            optimize=False,
            # Defines la cantidad
            limit=5
        )
    ),
]

scraper.run(queries)
