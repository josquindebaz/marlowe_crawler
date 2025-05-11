import mysql.connector

from database_parameters import connection_parameters


def is_in_table(url):
    db = mysql.connector.connect(**connection_parameters)
    cursor = db.cursor()

    request = "SELECT `m_url` FROM `tbl_texte` WHERE `m_url` = %(url)s"
    cursor.execute(request, {'url': url})

    result = cursor.fetchall()
    if result:
        cursor.close()
        return True

    cursor.close()
    db.close()

    return False


def insert_in_table(article):
    if is_in_table(article.link):
        return f"{article.link} already in the table"

    text = f"{article.description}\n{article.content}"

    data = (text,
            article.author,
            article.title,
            article.link,
            article.date.strftime("%Y-%m-%d %H:%M:%S"),
            article.lang)

    request = "INSERT into `tbl_texte` (`m_data`, `m_auteur`, `m_titre`,`m_url`, `m_date`, `m_lang`) VALUES (%s, %s, %s, %s, %s, %s)"

    db = mysql.connector.connect(**connection_parameters)
    cursor = db.cursor()
    try:
        cursor.execute(request, data)
        db.commit()
    # print(cursor.rowcount, "record inserted.")
    except:
        print(f"{article.link} insertion failed")
    cursor.close()
    db.close()

    return "ok"
