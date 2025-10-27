import csv
import sqlite3

from Models.Conteudo.Musica import Musica
from Models.Conteudo.Podcast import Podcast
from Models.Conteudo.AudioLivro import AudioLivro
from Models.Conteudo.SomAmbiente import SomAmbiente

class ConteudoServices:
    def __init__(self):
        self.__musicas = []
        self.__podcasts = []
        self.__audiolivros = []
        self.__sons_ambiente = []
        self.__erros = []

    @property
    def musicas(self):
        return self.__musicas
    
    @property
    def podcasts(self):
        return self.__podcasts
    
    @property
    def audiolivros(self):
        return self.__audiolivros
    
    @property
    def sons_ambiente(self):
        return self.__sons_ambiente

    @property
    def erros(self):
        return self.__erros

    def carregar_csv(self, nome_arquivo):
        with open(nome_arquivo, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")

            for i, row in enumerate(reader, start=1):
                tipo = row["content_type"].lower()

                try:
                    if tipo == "musica":
                        if not row["identifier/ISRC"]:
                            raise ValueError("Música sem ISRC não pode ser cadastrada")
                        musica = Musica(
                            row["title"], row["artist_id"], row["release_date"],
                            int(row["duration_sec"]), row["genre"],
                            row["identifier/ISRC"], row["album"],
                            row["Faixa"], row["selo"], row["explicit"]
                        )
                        self.musicas.append(musica)

                    elif tipo == "podcast":
                        if not row["rss_feed"]:
                            raise ValueError("Podcast sem RSS Feed")
                        podcast = Podcast(
                            row["title"], row["artist_id"], row["release_date"],
                            int(row["duration_sec"]), row["genre"],
                            row["season"], row["episode"],
                            row["rss_feed"], row["identifier/ISRC"]
                        )
                        self.podcasts.append(podcast)

                    elif tipo == "audiolivro":
                        if not row["narrator"] or not row["editora"]:
                            raise ValueError("Audiolivro sem narrador ou editora")
                        audiobook = AudioLivro(
                            row["title"], row["artist_id"], row["release_date"],
                            int(row["duration_sec"]), row["genre"],
                            row["narrator"], row["editora"], row["capítulo"]
                        )
                        self.audiolivros.append(audiobook)

                    elif tipo == "som_ambiente":
                        som = SomAmbiente(
                            row["title"], row["artist_id"], row["release_date"],
                            int(row["duration_sec"]), row["genre"],
                            row["is_loopable"], row["noise_level"]
                        )
                        self.sons_ambiente.append(som)

                    else:
                        raise ValueError(f"Tipo desconhecido: {tipo}")

                except ValueError as e:
                    self.erros.append({"linha": i, "erro": str(e), "conteudo": row})

    def salvar_no_banco(self):
        try:
            con = sqlite3.connect("streaming.db")
            cur = con.cursor()

            ConteudoDB.create_tables(cur)

            for m in self.musicas:
                ConteudoDB.insert_musica(cur, m)
            for p in self.podcasts:
                ConteudoDB.insert_podcast(cur, p)
            for a in self.audiolivros:
                ConteudoDB.insert_audiolivro(cur, a)
            for s in self.sons_ambiente:
                ConteudoDB.insert_som(cur, s)

            con.commit()
            print("Catálogo salvo com sucesso.")

        except Exception as e:
            print("Erro:", e)
            con.rollback()
        finally:
            cur.close()
            con.close()


class ConteudoDB:
    def create_tables(cur):
        cur.execute("""
        CREATE TABLE IF NOT EXISTS musica(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            artista TEXT NOT NULL,
            data_lancamento TEXT NOT NULL,
            duracao INT NOT NULL,
            genero TEXT,
            isrc TEXT NOT NULL UNIQUE,
            album TEXT,
            faixa INT,
            selo TEXT,
            explicito TEXT NOT NULL
        );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS podcast(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            artista TEXT NOT NULL,
            data_lancamento TEXT NOT NULL,
            duracao INT NOT NULL,
            genero TEXT,
            season INT,
            episode INT,
            rss_feed TEXT NOT NULL,
            isrc TEXT
        );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS audiolivro(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            artista TEXT NOT NULL,
            data_lancamento TEXT NOT NULL,
            duracao INT NOT NULL,
            genero TEXT,
            narrador TEXT NOT NULL,
            editora TEXT NOT NULL,
            capitulos INT
        );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS som_ambiente(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            artista TEXT NOT NULL,
            data_lancamento TEXT NOT NULL,
            duracao INT NOT NULL,
            genero TEXT,
            loopable TEXT,
            faixaRuido TEXT
        );
        """)

    def insert_musica(cur, m):
        cur.execute("""INSERT INTO musica
        (titulo, artista, data_lancamento, duracao, genero, isrc, album, faixa, selo, explicito)
        VALUES (?,?,?,?,?,?,?,?,?,?)""",
        (m.titulo, m.artista, m.data, m.duracao, m.genero, m.isrc, m.album, m.faixa, m.selo, m.explicito))

    def insert_podcast(cur, p):
        cur.execute("""INSERT INTO podcast
        (titulo, artista, data_lancamento, duracao, genero, season, episode, rss_feed, isrc)
        VALUES (?,?,?,?,?,?,?,?,?)""",
        (p.titulo, p.artista, p.data, p.duracao, p.genero, p.season, p.episode, p.rss, p.isrc))

    def insert_audiolivro(cur, a):
        cur.execute("""INSERT INTO audiolivro
        (titulo, artista, data_lancamento, duracao, genero, narrador, editora, capitulos)
        VALUES (?,?,?,?,?,?,?,?)""",
        (a.titulo, a.artista, a.data, a.duracao, a.genero, a.narrador, a.editora, a.capitulos))

    def insert_som(cur, s):
        cur.execute("""INSERT INTO som_ambiente
        (titulo, artista, data_lancamento, duracao, genero, loopable, faixaRuido)
        VALUES (?,?,?,?,?,?,?)""",
        (s.titulo, s.artista, s.data, s.duracao, s.genero, s.loopable, s.faixaRuido))
