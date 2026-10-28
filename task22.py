<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CineWorld | Movie Explorer</title>

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    font-family: Arial, sans-serif;
    background: #101018;
    color: #fff;
}

header {
    background: #191923;
    padding: 20px 7%;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 20px;
    flex-wrap: wrap;
    border-bottom: 1px solid #30303c;
}

.logo {
    color: #ffbd39;
    font-size: 28px;
    font-weight: bold;
}

nav {
    display: flex;
    gap: 20px;
    flex-wrap: wrap;
}

nav a {
    color: white;
    text-decoration: none;
    transition: .3s;
}

nav a:hover {
    color: #ffbd39;
}

.hero {
    min-height: 350px;
    padding: 65px 20px;
    text-align: center;
    display: flex;
    justify-content: center;
    align-items: center;
    background: linear-gradient(135deg, #35154e, #17172c, #651d29);
}

.hero h1 {
    font-size: clamp(35px, 5vw, 58px);
    margin-bottom: 15px;
    animation: fadeIn 1s ease;
}

.hero h1 span {
    color: #ffbd39;
}

.hero p {
    color: #ddd;
    margin-bottom: 25px;
}

.search {
    width: min(90%, 450px);
    padding: 14px;
    border: none;
    border-radius: 8px;
    font-size: 16px;
    outline: none;
}

.container {
    max-width: 1250px;
    margin: auto;
    padding: 45px 22px;
}

.heading {
    font-size: 30px;
    margin-bottom: 25px;
}

.heading span {
    color: #ffbd39;
}

.filters {
    display: flex;
    gap: 12px;
    flex-wrap: wrap;
    margin-bottom: 28px;
}

.filters button {
    background: #242432;
    color: white;
    padding: 10px 18px;
    border: 1px solid #414151;
    border-radius: 25px;
    cursor: pointer;
    transition: .3s;
}

.filters button:hover,
.filters button.active {
    background: #ffbd39;
    color: #171717;
    border-color: #ffbd39;
}

.movie-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
    gap: 25px;
}

.movie-card {
    background: #1d1d29;
    border-radius: 13px;
    overflow: hidden;
    border: 1px solid #30303c;
    transition: transform .3s, box-shadow .3s;
    animation: fadeIn .6s ease;
}

.movie-card:hover {
    transform: translateY(-7px);
    box-shadow: 0 12px 28px #0008;
}

.poster {
    height: 290px;
    position: relative;
    overflow: hidden;
    background: #29293a;
}

.poster img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform .4s;
}

.movie-card:hover .poster img {
    transform: scale(1.06);
}

.rating {
    position: absolute;
    top: 12px;
    right: 12px;
    background: #ffbd39;
    color: #171717;
    padding: 7px 10px;
    border-radius: 6px;
    font-weight: bold;
}

.movie-info {
    padding: 18px;
}

.movie-info h3 {
    font-size: 20px;
    margin-bottom: 10px;
}

.meta {
    color: #b9b9c8;
    font-size: 13px;
    line-height: 1.8;
}

.genre {
    display: inline-block;
    background: #373044;
    color: #e5caff;
    padding: 5px 9px;
    margin: 10px 0;
    border-radius: 5px;
    font-size: 12px;
}

.synopsis {
    color: #d0d0dc;
    font-size: 14px;
    line-height: 1.6;
    margin: 10px 0;
}

.btn {
    border: none;
    background: #ffbd39;
    color: #151515;
    padding: 11px 16px;
    border-radius: 6px;
    font-weight: bold;
    cursor: pointer;
    transition: .3s;
}

.btn:hover {
    background: #ffcf70;
    transform: translateY(-2px);
}

.details-section {
    background: #1a1a26;
    border-radius: 12px;
    padding: 25px;
    margin-top: 35px;
    line-height: 1.9;
    scroll-margin-top: 20px;
}

.details-section p {
    color: #d0d0dc;
    margin: 8px 0;
}

.details-section h3 {
    color: #ffbd39;
    margin-bottom: 12px;
}

.reviews {
    margin-top: 15px;
    padding: 15px;
    background: #252533;
    border-left: 3px solid #ffbd39;
    border-radius: 5px;
}

#emptyMessage {
    display: none;
    color: #ccc;
    margin-top: 20px;
}

footer {
    text-align: center;
    background: #191923;
    padding: 25px;
    color: #aaa;
    line-height: 1.8;
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(15px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@media(max-width: 600px) {
    header {
        justify-content: center;
    }

    nav {
        justify-content: center;
        gap: 13px;
    }

    nav a {
        font-size: 14px;
    }

    .container {
        padding: 30px 16px;
    }

    .poster {
        height: 330px;
    }
}
</style>
</head>

<body>

<header>
    <div class="logo">🎬 CineWorld</div>
    <nav>
        <a href="#home">Home</a>
        <a href="#movies">Movies</a>
        <a href="#reviews">Reviews</a>
        <a href="#about">About</a>
    </nav>
</header>

<section class="hero" id="home">
    <div>
        <h1>Discover the World of <span>Cinema</span></h1>
        <p>Explore movies, meet the cast and discover your next favourite film.</p>
        <input type="text" class="search" id="search"
            placeholder="Search movie titles or genres...">
    </div>
</section>

<main class="container" id="movies">
    <h2 class="heading">Explore <span>Movies</span></h2>

    <div class="filters">
        <button class="active" data-genre="All">All Movies</button>
        <button data-genre="Action">Action</button>
        <button data-genre="Sci-Fi">Sci-Fi</button>
        <button data-genre="Drama">Drama</button>
        <button data-genre="Animation">Animation</button>
    </div>

    <div class="movie-grid" id="movieGrid"></div>

    <p id="emptyMessage">No movies found. Try another search.</p>

    <section class="details-section" id="movieDetails">
        <h3>Movie Details</h3>
        <p>Select a movie and click "View Details" to see its cast,
        synopsis, release date and critic review.</p>
    </section>
</main>

<section class="container" id="reviews">
    <h2 class="heading">Critics' <span>Corner</span></h2>
    <div class="details-section">
        <h3>About Movie Ratings</h3>
        <p>Explore the sample critic ratings and review summaries
        displayed for each film. These ratings are illustrative and
        are not live critic scores.</p>
        <p>Choose a movie card to read its sample review.</p>
    </div>
</section>

<section class="container" id="about">
    <h2 class="heading">About <span>CineWorld</span></h2>
    <div class="details-section">
        <p>CineWorld is a movie catalog website built with HTML,
        CSS and JavaScript. It helps users explore films by genre
        and discover their stories, casts, release dates and ratings.</p>
    </div>
</section>

<footer>
    <p>© <span id="year"></span> CineWorld | Movie Explorer</p>
    <p>Academic project developed using HTML, CSS and JavaScript.</p>
</footer>

<script>
const movies = [
    {
        id: 1,
        title: "The Dark Knight",
        genre: "Action",
        year: "2008",
        release: "18 July 2008",
        rating: "9.0/10",
        cast: "Christian Bale, Heath Ledger, Aaron Eckhart",
        director: "Christopher Nolan",
        image: "https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg",
        synopsis: "Batman faces the Joker, a criminal mastermind who brings chaos to Gotham City.",
        review: "A gripping superhero crime drama praised for its performances and storytelling."
    },
    {
        id: 2,
        title: "Interstellar",
        genre: "Sci-Fi",
        year: "2014",
        release: "7 November 2014",
        rating: "8.7/10",
        cast: "Matthew McConaughey, Anne Hathaway, Jessica Chastain",
        director: "Christopher Nolan",
        image: "https://image.tmdb.org/t/p/w500/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg",
        synopsis: "A group of explorers travels through space in search of a future for humanity.",
        review: "An ambitious science-fiction film known for its scale, emotion and music."
    },
    {
        id: 3,
        title: "Inception",
        genre: "Sci-Fi",
        year: "2010",
        release: "16 July 2010",
        rating: "8.8/10",
        cast: "Leonardo DiCaprio, Joseph Gordon-Levitt, Elliot Page",
        director: "Christopher Nolan",
        image: "https://image.tmdb.org/t/p/w500/oYuLEt3zVCKq57qu2F8dT7NIa6f.jpg",
        synopsis: "A skilled thief enters people's dreams to steal secrets and attempts an extraordinary mission.",
        review: "A mind-bending thriller with inventive visuals and layered storytelling."
    },
    {
        id: 4,
        title: "The Shawshank Redemption",
        genre: "Drama",
        year: "1994",
        release: "23 September 1994",
        rating: "9.3/10",
        cast: "Tim Robbins, Morgan Freeman, Bob Gunton",
        director: "Frank Darabont",
        image: "https://image.tmdb.org/t/p/w500/9cqNxx0GxF0bflZmeSMuL5tnGzr.jpg",
        synopsis: "Two prisoners develop a lasting friendship while navigating life inside prison.",
        review: "A moving story of friendship, hope and perseverance."
    },
    {
        id: 5,
        title: "Spider-Man: Into the Spider-Verse",
        genre: "Animation",
        year: "2018",
        release: "14 December 2018",
        rating: "8.4/10",
        cast: "Shameik Moore, Jake Johnson, Hailee Steinfeld",
        director: "Bob Persichetti, Peter Ramsey, Rodney Rothman",
        image: "https://image.tmdb.org/t/p/w500/iiZZdoQBEYBv6id8su7ImL0oCbD.jpg",
        synopsis: "Miles Morales discovers his powers and encounters Spider-heroes from other dimensions.",
        review: "A visually inventive animated adventure with humour and heart."
    },
    {
        id: 6,
        title: "Gladiator",
        genre: "Action",
        year: "2000",
        release: "5 May 2000",
        rating: "8.5/10",
        cast: "Russell Crowe, Joaquin Phoenix, Connie Nielsen",
        director: "Ridley Scott",
        image: "https://image.tmdb.org/t/p/w500/ty8TGRuvJLPUmAR1H1nRIsgwvim.jpg",
        synopsis: "A betrayed Roman general seeks justice in the arena as a gladiator.",
        review: "An epic historical drama noted for its scale and lead performance."
    }
];

let selectedGenre = "All";

const grid = document.getElementById("movieGrid");
const search = document.getElementById("search");

function renderMovies() {
    const query = search.value.toLowerCase();

    const results = movies.filter(movie => {
        const genreMatch =
            selectedGenre === "All" || movie.genre === selectedGenre;

        const searchMatch =
            movie.title.toLowerCase().includes(query) ||
            movie.genre.toLowerCase().includes(query) ||
            movie.cast.toLowerCase().includes(query);

        return genreMatch && searchMatch;
    });

    grid.innerHTML = results.map(movie => `
        <article class="movie-card">
            <div class="poster">
                <img src="${movie.image}"
                     alt="${movie.title} movie poster"
                     loading="lazy"
                     onerror="this.style.display='none';">
                <span class="rating">⭐ ${movie.rating}</span>
            </div>

            <div class="movie-info">
                <h3>${movie.title}</h3>
                <p class="meta">📅 ${movie.year}</p>
                <span class="genre">${movie.genre}</span>
                <p class="synopsis">${movie.synopsis}</p>
                <button class="btn" onclick="showDetails(${movie.id})">
                    View Details
                </button>
            </div>
        </article>
    `).join("");

    document.getElementById("emptyMessage").style.display =
        results.length ? "none" : "block";
}

document.querySelectorAll(".filters button").forEach(button => {
    button.addEventListener("click", () => {
        document.querySelectorAll(".filters button")
            .forEach(item => item.classList.remove("active"));

        button.classList.add("active");
        selectedGenre = button.dataset.genre;
        renderMovies();
    });
});

search.addEventListener("input", renderMovies);

function showDetails(id) {
    const movie = movies.find(item => item.id === id);

    document.getElementById("movieDetails").innerHTML = `
        <h3>${movie.title}</h3>
        <p><strong>Genre:</strong> ${movie.genre}</p>
        <p><strong>Release Date:</strong> ${movie.release}</p>
        <p><strong>Rating:</strong> ⭐ ${movie.rating}</p>
        <p><strong>Director:</strong> ${movie.director}</p>
        <p><strong>Cast:</strong> ${movie.cast}</p>
        <p><strong>Synopsis:</strong> ${movie.synopsis}</p>
        <div class="reviews">
            <strong>Critic Review:</strong>
            <p>${movie.review}</p>
        </div>
    `;

    document.getElementById("movieDetails")
        .scrollIntoView({ behavior: "smooth" });
}

document.getElementById("year").textContent =
    new Date().getFullYear();

renderMovies();
</script>

</body>
</html>
