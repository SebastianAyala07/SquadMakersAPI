from db.mysql import ConnectionDB

class Joke:

    def __init__(self, joke_text):
        self.joke_text = joke_text

    @classmethod
    def get_by_id(cls, _id):
        select_by_id_sentence = "SELECT * FROM joke WHERE id={0};"
        conn, cursor = cursor = ConnectionDB.get_cursor()
        cursor.execute(select_by_id_sentence.format(_id))
        joke = cursor.fetchone()
        # TODO: create and return object Joke

    def save(self):
        insert_sentence = "INSERT INTO joke (joke_text) VALUES ({0});"
        conn, cursor = ConnectionDB.get_cursor()
        cursor.execute(insert_sentence.format(self.joke_text))
        conn.commit()

    def update(self):
        update_sentence = "UPDATE joke SET joke_text={0} WHERE id={2};"
        conn, cursor = ConnectionDB.get_cursor()
        cursor.execute(update_sentence.format(self.joke_text, self.id))
        conn.commit()

    def delete(self):
        delete_sentence = "DELETE FROM joke WHERE id={0};"
        conn, cursor = ConnectionDB.get_cursor()
        cursor.execute(delete_sentence.format(self.id))
        conn.commit()
