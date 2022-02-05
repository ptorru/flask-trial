# flask-trial
This is my first trial of flask and jinja templating

## Running the app
For this you will need a NASA API key. Get it from [here]()

Use python to run the `run.py`script, passing as arguments your key and the number of extra images to display in the page:

```bash
# This will generate a page with 2 extra images
python run.py <your-api-key> 2
```

## Talking through the code
In this function we build the data we will use to puplate the Jinja template with:

```python
def template_test():
    # API call to get the picture of the day
    # API call to get other random pictures
    return render_template('template.html', ...some parameters...)
```

This function has the call to `render_template` which is the one that builds the actual page based on the template.

In the template we then catch those paremters. These behave just like python objects. For example we can pass a dictionary and access its internals directly, no decompossing is necessary up-front. Here we have passed a list called `others`. This list contains dictionaries with data:
```html
      {% for n in others %}
      <p>Date: {{n["date"]}} / {{n["title"]}}</p>
```
