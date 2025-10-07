import Conteudo

class Podcast(Conteudo):
    def __init__ (self, iscrPodcast, generoPodcast, titulo, duracao, data, Artista):
        super().__init__(self, titulo, duracao, data, Artista)
        self.__iscrPodcast = iscrPodcast
        self.__generoPodcast = generoPodcast