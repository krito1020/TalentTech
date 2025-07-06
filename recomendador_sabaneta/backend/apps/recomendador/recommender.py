import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class RecomendadorEmpresas:
    def __init__(self, path_excel):
        self.df = pd.read_excel(path_excel, sheet_name='BBDD')
   #     self.df.fillna('', inplace=True)
        for col in self.df.columns:
            if self.df[col].dtype == 'object':
                self.df[col] = self.df[col].fillna('')
            else:
                self.df[col] = self.df[col].fillna(0)
        self.vectorizador = TfidfVectorizer(stop_words=None)
        self.tfidf = self.vectorizador.fit_transform(self.df['ARTICULOS'])

    def recomendar(self, texto_usuario, top_n=5, min_similitud=0.2):
        consulta = self.vectorizador.transform([texto_usuario])
        similitudes = cosine_similarity(consulta, self.tfidf).flatten()
        indices = [i for i in similitudes.argsort()[::-1] if similitudes[i] >= min_similitud][:top_n]
        return self.df.iloc[indices]