import json
from flask import jsonify
from db.mysql import ConnectionDB

class Joke:

    def __init__(self, joke_text=None, _id=None):
        if joke_text:
            self.joke_text = joke_text
        if _id:
            self.id = _id

    @classmethod
    def get_by_id(cls, _id):
        try:
            select_by_id_sentence = "SELECT id, joke_text FROM joke WHERE id={0};"
            conn, cursor = ConnectionDB.get_cursor()
            cursor.execute(select_by_id_sentence.format(_id))
            joke = cursor.fetchone()
            json_joke = json.loads(joke)
            return json_joke
        except Exception as e:
            return jsonify({"msg": f"{e}"})
        # TODO: create and return object Joke

    def save(self):
        try:
            insert_sentence = "INSERT INTO joke(joke_text) VALUES('{0}');"
            conn, cursor = ConnectionDB.get_cursor()
            cursor.execute(insert_sentence.format(self.joke_text))
            conn.commit()
            self.id = cursor.lastrowid
            return jsonify({"msg": f"1 record inserted, ID: {cursor.lastrowid}"})
        except:
            return jsonify({"msg": "Error in save joke"})

    def update(self):
        update_sentence = "UPDATE joke SET joke_text='{0}' WHERE id={1};"
        conn, cursor = ConnectionDB.get_cursor()
        cursor.execute(update_sentence.format(self.joke_text, self.id))
        conn.commit()
        return jsonify({"msg": f"{cursor.rowcount} record updated, ID: {self.id}"})

    def delete(self):
        delete_sentence = "DELETE FROM joke WHERE id={0};"
        conn, cursor = ConnectionDB.get_cursor()
        cursor.execute(delete_sentence.format(self.id))
        conn.commit()
        return jsonify({"msg": f"{cursor.rowcount} record deleted, ID: {self.id}"})
