import os
import app.constants as constants
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SECRET_KEY = os.environ['SECRET_KEY']
    MIN_YEAR = 2016
    MAX_YEAR = 2100
    PASSWORD_SALT = "something random and full of non-standard characters"
    LOCALE = "fr_FR.UTF-8"

    TIMEZONE = "Europe/Paris"

    WEEK_STARTING_DAY = constants.WEEK_START_DAY_MONDAY

    MONTHS_TO_EXPORT = 6  # currently only used for ICS export

    FEATURE_FLAG_ICAL_EXPORT = False

    # If true, will automatically decorate hyperlinks with <a> tags upon rendering them
    AUTO_DECORATE_TASK_DETAILS_HYPERLINK = True

    SHOW_VIEW_PAST_BUTTON = True

    # Of use if SHOW_VIEW_PAST_BUTTON is False
    HIDE_PAST_TASKS = False

    # days past to keep hidden tasks (future ones always kept) counting all months as 31 days long
    DAYS_PAST_TO_KEEP_HIDDEN_TASKS = 62

    # If to render emoji buttons at the task create/edit page
    EMOJIS_ENABLED = True

    # Colors for new task buttons
    BUTTON_CUSTOM_COLOR_VALUE = "#3EB34F"
    BUTTONS_COLORS_LIST = (
        ("#FF4848", "Red"),
        ("#3EB34F", "Green"),
        ("#2966B8", "Blue"),
        ("#808080", "Grey"),
        ("#B05F3C", "Brown"),
        ("#9588EC", "Purple"),
        ("#F2981A", "Orange"),
        ("#3D3D3D", "Black"),
    )
    # Emojis for new task buttons
    BUTTONS_EMOJIS_LIST = (
        "💬",
        "📞",
        "🍔",
        "🍺",
        "📽️",
        "🎂",
        "🏖️",
        "💻",
        "📔",
        "✂️",
        "🚂",
        "🏡",
        "🐶",
        "🐱",
    )


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


