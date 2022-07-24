#!/usr/bin/env python
# coding: utf-8

# In[1]:

from flask import request, Flask, render_template
import joblib


# In[2]:


app = Flask(__name__)


# In[3]:


@app.route("/", methods = ["GET", "POST"])


def index():
    if request.method == "POST":
        rates = float(request.form.get("rates"))
        print(rates)
        model_1 = joblib.load("regression")
        r1 = model_1.predict([[rates]])
        model_2 = joblib.load("tree")
        r2 = model_2.predict([[rates]])
        return(render_template("index.html", result_1 = r1, result_2 = r2))
    else:
        return(render_template("index.html", result_1 = "WAITING", result_2 = "WAITING"))


# In[ ]:


if __name__ == "__main__":
    app.run()
