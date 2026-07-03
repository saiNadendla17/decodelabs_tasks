# ==========================================
# DecodeLabs AI Project 3
# AI Recommendation System
# Developed by: Nadendla Sai Vyshnavi
# ==========================================

import random

# ANSI Color codes for better output formatting
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

print(Colors.BOLD + Colors.CYAN + "=" * 60)
print("      DECODE AI RECOMMENDATION SYSTEM")
print("=" * 60 + Colors.END)

movies = {
    "action": ["Avengers: Endgame", "John Wick", "The Dark Knight", "Mission Impossible"],
    "comedy": ["3 Idiots", "Free Guy", "Jumanji", "The Mask"],
    "horror": ["The Conjuring", "Insidious", "Smile", "Annabelle"],
    "romance": ["Titanic", "La La Land", "The Notebook", "Me Before You"],
    "science fiction": ["Interstellar", "Inception", "Avatar", "The Martian"]
}

books = {
    "action": ["The Hunger Games", "The Maze Runner", "Alex Rider"],
    "comedy": ["Diary of a Wimpy Kid", "Good Omens", "Bossypants"],
    "horror": ["Dracula", "It", "Frankenstein"],
    "romance": ["Pride and Prejudice", "Twilight", "The Fault in Our Stars"],
    "science fiction": ["Dune", "The Time Machine", "Ready Player One"]
}

songs = {
    "action": ["Believer", "Legends Never Die", "Warriors"],
    "comedy": ["Happy", "Can't Stop The Feeling", "Uptown Funk"],
    "horror": ["Thriller", "Somebody's Watching Me", "Monster"],
    "romance": ["Perfect", "All of Me", "Until I Found You"],
    "science fiction": ["Starboy", "Blinding Lights", "Space Song"]
}

while True:

    print(Colors.BOLD + Colors.BLUE + "\nChoose Recommendation Type" + Colors.END)
    print(Colors.GREEN + "1. Movies")
    print("2. Books")
    print("3. Songs" + Colors.END)

    choice = input(Colors.YELLOW + "\nEnter your choice (1-3): " + Colors.END)

    if choice == "1":
        data = movies
        title = "Movies"

    elif choice == "2":
        data = books
        title = "Books"

    elif choice == "3":
        data = songs
        title = "Songs"

    else:
        print(Colors.RED + "❌ Invalid Choice! Please select 1, 2, or 3." + Colors.END)
        continue

    print(Colors.BOLD + Colors.CYAN + "\nAvailable Genres" + Colors.END)
    print(Colors.CYAN + "-" * 35 + Colors.END)

    for genre in data:
        print(Colors.GREEN + "  ✓ " + genre.title() + Colors.END)

    genre = input(Colors.YELLOW + "\nEnter Genre: " + Colors.END).lower()

    if genre in data:

        print(Colors.BOLD + Colors.GREEN + f"\n✨ Recommended {title} ✨" + Colors.END)
        print(Colors.GREEN + "-" * 40 + Colors.END)

        recommendations = random.sample(data[genre], 3)

        for i, item in enumerate(recommendations, 1):
            print(Colors.YELLOW + f"  ⭐ {i}. {item}" + Colors.END)

        print(Colors.BOLD + Colors.RED + "\n🏆 Today's Best Pick 🏆" + Colors.END)
        print(Colors.RED + f"  ➜ {random.choice(data[genre])}" + Colors.END)

    else:
        print(Colors.RED + f"\n❌ Genre '{genre}' not available. Please choose from the list above." + Colors.END)

    rating = input(Colors.YELLOW + "\nRate this recommendation (1-5): " + Colors.END)
    print(Colors.GREEN + "✓ Thank you for your feedback!" + Colors.END)

    again = input(Colors.YELLOW + "\nWould you like another recommendation? (yes/no): " + Colors.END).lower()

    if again != "yes":
        print(Colors.BOLD + Colors.CYAN + "\n" + "=" * 60)
        print("Thank you for using Decode AI Recommendation System!")
        print("=" * 60 + Colors.END)
        break