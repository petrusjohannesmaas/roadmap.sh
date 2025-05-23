
# URL Shortening Service

Flask is simple and flexible, perfect for building a RESTful service. Here's how you can implement it using Flask and Python's built-in SQLite library.

## Features

✅ **Create a new short URL** (`POST /shorten`)  
✅ **Retrieve an original URL** (`GET /shorten/<short_code>`)  
✅ **Update an existing short URL** (`PUT /shorten/<short_code>`)  
✅ **Delete an existing short URL** (`DELETE /shorten/<short_code>`)  
✅ **Get statistics on the short URL** (`GET /shorten/<short_code>/stats`)  

## Future Enhancements

- Containerized Deployment instructions
- Authentication  
- Rate Limiting  
- Advanced Analytics  
- gRPC API

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/roadmap.sh/url-shortener.git && cd url-shortener
```

### Install Flask

If you prefer using a virtual environment, install Flask like this:

```bash
python3 -m venv venv
source venv/bin/activate
pip install flask
```

Then run the application:

```bash
python3 main.py
```

## Running the application with **pipx**

`pipx` is great for managing Python applications in isolated environments. Here’s how to install and run the URL shortener using `pipx`:

### Install pipx

If you haven't installed `pipx` yet, check the [installation guide](https://pipx.pypa.io/stable/installation/).  
After installing, restart your terminal for the changes to take effect.

### Project Structure

```
url_shortener/
│── main.py        # (Your Flask app)
│── setup.py
│── pyproject.toml
│── __init__.py    # (Required for packaging)
```

### Install with pipx

Make sure you're in the project directory:

```bash
cd url-shortener
pipx install .
```

Now you can run it without virtual environment boilerplate:

```bash
url-shortener
```

Uninstall it with:

```bash
pipx uninstall url-shortener
```

Your API will be available at **http://127.0.0.1:5000/shorten** 🎉
