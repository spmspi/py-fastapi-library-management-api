from sqlalchemy import select
from sqlalchemy.orm import Session
from models import Author, Book
from schemas import AuthorCreate, BookCreate


def get_all_authors(db: Session):
    return db.scalars(select(Author)).all()

def get_author_name(db: Session, name: str = None):
    return db.scalar(select(Author).where(Author.name == name))

def get_author(db: Session, author_id: int):
    return db.scalar(select(Author).where(Author.id == author_id))

def create_author(db: Session, author: AuthorCreate):
    db_author = Author(
        name=author.name,
        bio=author.bio)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

def get_all_books(
        db: Session,
        title: str = None,
        author_name: str = None,
        ):
    queryset = db.query(Book)
    if title is not None:
        queryset = queryset.where(Book.title == title)

    if author_name is not None:
        queryset = queryset.join(Author).where(Author.name == author_name)

    return db.scalars(queryset).all()

def get_book(db: Session, book_id: int):
    return db.scalar(select(Book).where(Book.id == book_id))

def create_book(db: Session, book: BookCreate):
    db_book = Book(
        title=book.title,
        summary=book.summary,
        publication_date=book.publication_date,
        author_id=book.author_id
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book
