Create a new `task2/front-end` directory.

Inside your new `task2/front-end`, clone this repository: [https://github.com/atlas-school/softy-pinko-front-end](https://github.com/atlas-school/softy-pinko-front-end).

With the `softy-pinko-front-end` directory and files in place, create a new `Dockerfile` in your `task2/front-end` directory. To host and distribute our front-end content, we will use a static web server named Nginx. There are many others that can be used, but this one is simple to get started with and conveniently has a Docker image that we can use which is pre-installed.

In the new `task2/front-end/Dockerfile`, instead of using the latest Ubuntu version, use the latest version of Nginx.

Your `softy-pinko-front-end` files must be copied to `/var/www/html/softy-pinko-front-end` on the Docker image.

Create an Nginx config file named `softy-pinko-front-end.conf` inside the `task2/front-end` directory. This file must be copied to the Docker image at `/etc/nginx/conf.d/default.conf` and must include all of the configuration settings required to get your site to show up when visiting the URL.

When researching Nginx config files, the only section you’ll need in the `softy-pinko-front-end.conf` file is the “server” section. Pay attention to the syntax used to set up a port to listen to (recommendation: port 9000), the name of the server, the location, and the index file to use.