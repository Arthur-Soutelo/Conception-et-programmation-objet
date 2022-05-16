import sqlite3
if __name__ == '__main__':
	try:
		conn = sqlite3.connect('hotellerie.db')
		curseur = conn.cursor()
		curseur.execute("SELECT nom, ville FROM hotel;")
		print(curseur.fetchall())
        
	except Exception as err:                                # interception d'une exception quelconque
		print('err:', str(err))
		print('type exception:', type(err).__name__)
	finally:                                                # fermeture de la base dans tous les cas
		conn.close()
