import time

import numpy as np

import bottle


app = bottle.Bottle()


@app.route("/random")
def random():
    time.sleep(np.random.randint(0, 1) + np.random.rand())
    return str(np.random.rand())


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)



