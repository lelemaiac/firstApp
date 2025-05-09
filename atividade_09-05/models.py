from sqlalchemy import create_engine, Integer,select, Column, String
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session

engine = create_engine('sqlite:///banco.sqlite3')
db_session = scoped_session(sessionmaker(bind=engine))
# db_session = sessionmaker(bind=engine)

Base = declarative_base()
#Base.query = db_session.query_property()

class Livro(Base):
    __tablename__ = 'Livros'
    id = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False, index=True, unique=True)
    autor = Column(String, nullable=False, index=True)
    descricao = Column(String, nullable=False, index=True)
    categoria = Column(String, nullable=False, index=True)

    def __repr__(self):
        return '<Livro {}>'.format(self.titulo)

    def save(self):
        try:
            db_session.add(self)
            db_session.commit()
        except SQLAlchemyError:
            db_session.rollback()
            raise

    def delete(self):
        try:
            db_session.delete(self)
            db_session.commit()
        except SQLAlchemyError:
            db_session.rollback()
            raise

    def serialize_user(self):
        dados_livro = {
            'id': self.id,
            'titulo': self.titulo,
            'autor': self.autor,
            'categoria': self.categoria,
            'descricao': self.descricao,

        }
        return dados_livro


class Usuario(Base):
    __tablename__ = 'Usuarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False, index=True, unique=True)
    salario = Column(String, nullable=False, index=True)
    profissao = Column(String, nullable=False, index=True)

    def __repr__(self):
        return '<Usuário {}>'.format(self.nome)

    def save(self):
        try:
            db_session.add(self)
            db_session.commit()
        except SQLAlchemyError:
            db_session.rollback()
            raise

    def delete(self):
        try:
            db_session.delete(self)
            db_session.commit()
        except SQLAlchemyError:
            db_session.rollback()
            raise

    def serialize_user(self):
        dados_usuario = {
            'id': self.id,
            'nome': self.nome,
            'profissao': self.profissao,
            'salario': self.salario,

        }
        return dados_usuario

def init_db():
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    init_db()