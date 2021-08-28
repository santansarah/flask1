from flask import Flask, render_template, abort
app = Flask(__name__)

PRODUCTS = {
    'nestcam': {
        'name': 'Nest Cam',
        'img': 'https://lh3.googleusercontent.com/EHsTpZJpybZxlLYT3rlOkcHkQCU6rturZ-XmaieWwDZVDsDRRO_3seIx_JzqLQ3Qz7cnBc0zvueNb4q-mmv2GY0XGhpg84gQ4A=w120',
        'desc': 'The battery-powered security camera with smarts.'
    },
    'nestaudio': {
        'name': 'Nest Audio',
        'img': 'https://lh3.googleusercontent.com/B_HPzK396bh0jV8TZddsfU7J2xICkD7HlWfeUJNkth6AK86KllqnU04sztQiKXh0fu4EmIh03_MsbtGjdJNqGGGwXvGGVIQ-Qg=w120',
        'desc': 'Meet Nest Audio, the helpful speaker that’s all about sound.' 
    },
    'chromecast': {
        'name': 'Chromecast',
        'img': 'https://lh3.googleusercontent.com/NX2UbwSeZBrH7WaaLaWvlfR3j5etfmLBnsmKoK0NrnrzOUjUZtX96M94dlMnREg4ev42mkKx6R24M5Y2Avl2RtJPytkno2W13Z8=w120',
        'desc': 'Chromecast streams your entertainment in up to 4K HDR.'
    }
}
 
@app.route('/')
def home():
    return render_template('home.html', products=PRODUCTS)

@app.route('/product/<key>')
def product(key):
    product = PRODUCTS.get(key)
    if not product:
        abort(404)
    return render_template('product.html', product=product)
