try:
    import gunicorn
    print("Gunicorn is installed.")
except ImportError:
    print("Gunicorn is not installed.")
