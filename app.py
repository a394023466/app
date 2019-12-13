from flask import Flask
import redis
import os
app= Flask(__name__)
r = redis.Redis(host=os.environ.get("REDIS_HOST"), port=os.environ.get("REDIS_PORT"))
@app.route("/")
def hello():
	r.incr('hits')
	return "hello container %s" % r.get('hits')

if __name__ == "__main__":
	app.run(host="0.0.0.0",port=5000,debug=True)
