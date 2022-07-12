from core import *

if __name__ == "__main__":
    try:
        APP.run(host="0.0.0.0", port=80)
    except:
        APP.run(host="0.0.0.0", port=8080)