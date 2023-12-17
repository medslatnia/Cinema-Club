from PySide2 import QtWidgets
from movie import get_movies
from movie import Movie


class App(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ciné Club")
        self.setup_ui()
        self.populate_movies()
        self.set_connections()



    def setup_ui(self): 
        self.main_layout = QtWidgets.QVBoxLayout(self)

        self.le_movieTitle = QtWidgets.QLineEdit()
        self.btn_addMovie = QtWidgets.QPushButton("Add the movie")
        self.lw_movies = QtWidgets.QListWidget()
        self.lw_movies.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)
        self.btn_removeMovies = QtWidgets.QPushButton("Remove the movie(s)")

        self.main_layout.addWidget(self.le_movieTitle)
        self.main_layout.addWidget(self.btn_addMovie)
        self.main_layout.addWidget(self.lw_movies)
        self.main_layout.addWidget(self.btn_removeMovies)

    def populate_movies(self):
        movies = get_movies()

        for movie in movies:
            self.lw_movies.addItem(movie.title)

    def set_connections(self):
        self.btn_addMovie.clicked.connect(self.add_movie)
        self.btn_removeMovies.clicked.connect(self.removeMovies)
        self.le_movieTitle.returnPressed.connect(self.add_movie)


    def removeMovies(self):
        for selected_item in self.lw_movies.selectedItems():
            movie = Movie(selected_item.text())
            movie.remove_from_movies()
            self.lw_movies.takeItem(self.lw_movies.row(selected_item))
            


    def add_movie(self):
        movie_title = self.le_movieTitle.text()
        if not movie_title:
            return False

        movie = Movie(title=movie_title)
        resultat = movie.add_to_movies()
        if resultat:
            self.lw_movies.addItem(movie.title)

app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec_()
