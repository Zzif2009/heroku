from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "yandexlyceum_secret_key"


def main():
    table = input()
    global_init(table)
    session = create_session()
    for user in session.query(User).filter(User.age < 18):
        print(user, user.age, "years")


if __name__ == "__main__":
    main()
