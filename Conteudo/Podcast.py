import Conteudo


class Podcast(Conteudo):
    def __init__ (self, iscrPodcast, generoPodcast):
        self.__iscrPodcast = iscrPodcast
        self.__generoPodcast = generoPodcast