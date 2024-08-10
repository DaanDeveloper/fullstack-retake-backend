get_release_date = "SELECT * FROM midnightecho.release_dates WHERE movie_name = %s;"

get_latest_news = "SELECT * FROM midnightecho.latest_news ORDER BY published_at DESC;"

insert_contact_message = ("INSERT INTO midnightecho.contact_messages (name, email, subject, message, submitted_at) VALUES (%s, %s, %s, %s, %s);")