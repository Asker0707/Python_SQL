import psycopg2


connect_db = psycopg2.connect(database="netology_db", user="postgres", password="superuser")

with connect_db.cursor() as cur:
    cur.execute("""
                
                INSERT INTO Users(user_id, first_name, second_name, email)
                VALUES (1, 'Steven', 'Strange', 'doctor_strange@magic.ru');
                    
                INSERT INTO user_phone (id_phone, id_user, phone)
                VALUES (1, '1', '+79688872539');
                    
                INSERT INTO Users(user_id, first_name, second_name, email)
                VALUES (2, 'Dormamu', 'Angry', 'world_is_my_dormamu@evil.com');
                    
                INSERT INTO user_phone(id_phone, id_user, phone)
                VALUES(2, '2', '+79282134121');
                    
                
                """)
    connect_db.commit()
    