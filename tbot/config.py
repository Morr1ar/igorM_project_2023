import os

TOKEN = "5656961547:AAExj9w2GS0CHetqfIwzf0XN_HPbSdMKHB8"
# db_data = "postgresql://hello_flask:hello_flask@db:5432/hello_flask_dev"
db_data = 'sqlite:///' + os.path.join("../flaskapp", 'app.db')