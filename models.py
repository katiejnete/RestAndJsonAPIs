"""Models for Cupcake app."""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


def connect_db(app):
    with app.app_context():
        db.app = app
        db.init_app(app)


class Cupcake(db.Model):
    """Cupcake model."""

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    flavor: Mapped[str] = mapped_column(nullable=False)
    size: Mapped[str] = mapped_column(nullable=False)
    rating: Mapped[float] = mapped_column(nullable=False)
    image: Mapped[str] = mapped_column(
        nullable=False, default="https://tinyurl.com/demo-cupcake"
    )

    def serialize(cupcake):
        """Serialize a cupcake SQLAlchemy object instance to dictionary."""

        return {
            "id": cupcake.id,
            "flavor": cupcake.flavor,
            "size": cupcake.size,
            "rating": cupcake.rating,
            "image": cupcake.image,
        }
