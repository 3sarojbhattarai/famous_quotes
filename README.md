# famous_quotes
Famous quote  a Django-based web application and REST API. That will show you some famous quote.

# Features:


# Installation

1. Install git,python3, pip3, virtualenv in your operating system
2. Create a development environment ready by using these commands
    git clone https://github.com/3sarojbhattarai/famous_quotes
    cd famous_quotes		
    python3 -m venv .venv
    source .venv/bin/activate		
    pip install -r requirements.txt		
    python manage.py makemigrations		
    python manage.py migrate		
    python manage.py collectstatic		
    python manage.py runserver		
    
 3. Go to http://127.0.0.1:8000/ to use project
 4. For RestAPI# JSON objects of persons
    http://127.0.0.1:8000/api/categories/		
    http://127.0.0.1:8000/api/quotes/		
    http://127.0.0.1:8000/api/quotes_random/	
    http://127.0.0.1:8000/api/qbp/pk/		
    http://127.0.0.1:8000/api/qbc/pk/		
