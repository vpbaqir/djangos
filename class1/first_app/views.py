from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def print_hello(request):
    movie_list={
        'movies' : [
    {
        "title": "The Social Network",
        "year": 2010,
        "genre": ["Biography", "Drama"],
        "plot": "The story of how Mark Zuckerberg created Facebook.",
        "relevance": "Shows the intersection of coding, business, and ambition."
    },
    {
        "title": "The Imitation Game",
        "year": 2014,
        "genre": ["Biography", "Drama", "Thriller"],
        "plot": "The life of Alan Turing and cracking the Nazi Enigma code.",
        "relevance": "Depicts cryptography and computing fundamentals."
    },
    {
        "title": "Tron: Legacy",
        "year": 2010,
        "genre": ["Action", "Adventure", "Sci-Fi"],
        "plot": "A young man is pulled into a digital world of living programs.",
        "relevance": "Visual metaphor for programming and virtual worlds."
    },
    {
        "title": "WarGames",
        "year": 1983,
        "genre": ["Sci-Fi", "Thriller"],
        "plot": "A young hacker accesses a military supercomputer thinking it’s a game.",
        "relevance": "Explores hacking and computer security."
    },
    {
        "title": "Hackers",
        "year": 1995,
        "genre": ["Crime", "Drama", "Thriller"],
        "plot": "Teen hackers uncover a conspiracy and are chased by authorities.",
        "relevance": "Showcases early hacker culture."
    },
    {
        "title": "The Matrix",
        "year": 1999,
        "genre": ["Action", "Sci-Fi"],
        "plot": "A hacker discovers the world is an illusion created by machines.",
        "relevance": "Offers philosophical ideas about virtual worlds and systems."
    },
    {
        "title": "Ex Machina",
        "year": 2015,
        "genre": ["Drama", "Sci-Fi", "Thriller"],
        "plot": "A programmer evaluates the human-like qualities of a robot.",
        "relevance": "Explores AI and machine learning."
    },
    {
        "title": "Pirates of Silicon Valley",
        "year": 1999,
        "genre": ["Biography", "Drama"],
        "plot": "The rise of Apple and Microsoft through Jobs and Gates' rivalry.",
        "relevance": "Gives insight into the tech industry's beginnings."
    },
    {
        "title": "The Internship",
        "year": 2013,
        "genre": ["Comedy"],
        "plot": "Two salesmen get internships at Google.",
        "relevance": "Offers a glimpse into tech culture."
    },
    {
        "title": "Source Code",
        "year": 2011,
        "genre": ["Action", "Drama", "Sci-Fi"],
        "plot": "A soldier enters a simulated reality to stop a terrorist attack.",
        "relevance": "Explores simulation and alternate realities."
    }
]}


    
    return render(request,'hello.html',movie_list)
    