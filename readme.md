# Jinja Demo with Flask/Python

This repository includes a Flask site that uses Jinja templates to render a collection of Google Nest products. The home page displays a list of products and a link to a single product page.

## How it Works

Products are defined in **app.py** and passed to the **home.html** template using the `render_template` function. The home template loops through all of the products and creates a bootstrap card for each product, along with a dynamic product detail link. 

**home.html** dynamically generates a product detail link using the product's key (e.g. http://localhost:5000/product/nestcam). **app.py** includes a dynamic route to the **product.html** template, where the product `<key>` is used to pass a single product to the **product.html** template. 

## Run the Site Locally

This Jinja demo includes a Docker Compose file that creates a web service and `/app` volume mount, allowing you to easily run this app and make changes locally. 

> Note: If you'd like to run this site without using Docker, you'll need Python 3.8 and Flask version 2.0.1. Jinja2 is included with Flask.

To use Docker Compose and run this demo in your browser:

1. Clone the Git repository. This creates a new folder named **flask1**.

        git clone https://github.com/santansarah/flask1.git

2. Navigate to the project folder and start the Docker container.
   
        docker compose up

    The site launches in a development environment with debugging on.

         Attaching to web_1g objects: 31, done.
         web_1  |  * Serving Flask app 'app.py' (lazy loading)
         web_1  |  * Environment: development3/23), done.
         web_1  |  * Debug mode: on, reused 29 (delta 4), pack-reused 0
         web_1  |  * Running on all addresses.4 KiB | 578.00 KiB/s, done.
         web_1  |    WARNING: This is a development server. Do not use it in a production deployment.
         web_1  |  * Running on http://xxx.xx.x.x:5000/ (Press CTRL+C to quit)
         web_1  |  * Restarting with statgit$ cd flask1
         web_1  |  * Debugger is active!_git/flask1$ docker compose up
         web_1  |  * Debugger PIN: 140-832-486

3. From your browser, navigate to **localhost**.

        http://localhost:5000/

 You should now be able to view products and click Product Details. With debugging on, the terminal displays each request:

      web_1  | xxx.xx.x.x - - [29/Aug/2021 18:52:58] "GET /static/css/bootstrap.min.css HTTP/1.1" 200 -
      web_1  | xxx.xx.x.x - - [29/Aug/2021 18:52:58] "GET /static/css/main.css HTTP/1.1" 200 -
      web_1  | xxx.xx.x.x - - [29/Aug/2021 18:53:56] "GET /product/nestcam HTTP/1.1" 200 -
      web_1  | xxx.xx.x.x - - [29/Aug/2021 18:53:56] "GET /static/css/bootstrap.min.css HTTP/1.1" 304 -
      web_1  | xxx.xx.x.x- - [29/Aug/2021 18:53:56] "GET /static/css/main.css HTTP/1.1" 304 -   

To stop the site, press **ctrl+c**.      