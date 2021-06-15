import ldclient
from ldclient.config import Config
from dotenv import load_dotenv
import os

load_dotenv()

ldclient.set_config(Config(os.getenv("ENVIRONMENT-SPECIFIC-KEY")))


def get_test_user():
    return {
      "key": "UNIQUE IDENTIFIER",
      "firstName": "TestUser",
      "lastName": "user",
      "custom": {
        "groups": "beta_testers"
      }
    }


def get_auto_translate_flag():
    return ldclient.get().variation("auto-translate", get_test_user(), False)


def ldclient_close():
    ldclient.get().close()
