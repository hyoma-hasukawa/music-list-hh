import multiprocessing

bind = "localhost:8080"
daemon = True
workders = multiprocessing.cpu_count() * 2 + 1 
