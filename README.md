# Flipkart Product Review Scraper

This GitHub repository contains a Django web application that allows users to search for product reviews on Flipkart. By typing the name of a product and clicking the search button, users can obtain reviews displayed in a table format, including product name, rating, caption, and comments.

## Getting Started

To run the application and start scraping Flipkart product reviews, follow these steps:

### Prerequisites

- Python 3.x
- Django (installed via `pip`)

### Running the Application

1. Start the Django development server:

```bash
python manage.py runserver
```

2. Access the application by navigating to `http://localhost:8000/` in your web browser.

### Using the Search Page

1. On the home page, you'll find a search input field where you can type the name of the product you want to search for.

2. After entering the product name, click the "Search" button to initiate the review scraping process.

3. The application will handle any errors during the scraping process using try-except blocks, ensuring a smooth user experience.

4. Once the scraping process is complete, the application will display the product reviews in a table format. The table includes the product name, rating, caption, and comments.

## Note

- The application logs the scraping activities, allowing you to monitor the scraping process and view any errors or exceptions that might occur during runtime.

## Contributing

We welcome contributions to this project! Feel free to open issues for bug reports or feature requests. If you'd like to make code changes, please fork the repository, create a new branch, and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code as per the terms of the license.

## Acknowledgments

Special thanks to the Flipkart website for providing the product reviews and inspiring this project.
