from flask import Flask, render_template
import requests


app = Flask(__name__)

response = requests.get("https://api.npoint.io/5abcca6f4e39b4955965")
all_blogs = response.json()


@app.route('/')
def home():
    return render_template("index.html", all_blogs=all_blogs)


@app.route("/post/<blog_id>")
def get_blog(blog_id):
    request_post = None
    for blog in all_blogs:
        # print(type(blog_id))
        # print(type(blog["id"]))
        # print(blog)
        if blog["id"] == int(blog_id):
            request_post = blog
            # print(request_post)
    return render_template("post.html", request_post=request_post)


if __name__ == "__main__":
    app.run(debug=True)
