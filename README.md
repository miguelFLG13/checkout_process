# checkout_process

Simple checkout process with discounts.

# Explaining the development:

I developed a simple API REST with Python + Django to create a simple checkout process.

How this is a exercise I selected SQLite to do this easier.

I used Docker to deploy easily in production.

In src, the structure has 3 apps:
  - Product: with the logic of products, requests and his data model
  - Discounts: with the logic of discounts and his data model.
  - CheckOut: with the logic of checkouts, requests and his data model.

Also, I developed some test to check the basics.

I have tryed to do all thinking It was easy to grow and easy to add new functionality.

Finally, remember that you can use this directly from the python terminal and do the same with the models.


# How to Use:

1) Install Docker

2) Export environment variable `DJANGO_SETTINGS_MODULE=checkout_process.settings.production`

3) Export environment variable `SECRET_KEY` with a random string

4) Execute `make build`

5) Execute `make up`