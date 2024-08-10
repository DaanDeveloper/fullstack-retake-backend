from fastapi import APIRouter
import database
from queries import r0986005_queries

app = APIRouter()

@app.get("/getReleaseDate")
def get_release_date(movie_name: str):
    query = r0986005_queries.get_release_date
    release_date = database.execute_sql_query(query, (movie_name,))
    if isinstance(release_date, Exception):
        return {"error": str(release_date)}, 500

    if not release_date:
        return {"error": "Movie not found"}, 404

    release_date_js_format = release_date[0][2].strftime("'%B %d, %Y'")

    return {"releaseDate": release_date_js_format}

@app.get("/getLatestNews")
def get_latest_news():
    query = r0986005_queries.get_latest_news
    latest_news = database.execute_sql_query(query, ())
    if isinstance(latest_news, Exception):
        return {"error": str(latest_news)}, 500

    news_items = []
    for news in latest_news:
        news_info = {
            "Title": news[1],
            "Content": news[2],
            "Published At": news[3].strftime("%Y-%m-%d %H:%M:%S")
        }
        news_items.append(news_info)

    return {"lastNews": news_items}
