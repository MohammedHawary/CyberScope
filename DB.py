import sqlite3

def create_connection():
    return sqlite3.connect('foldersDB.db')

def create_table():
    conn = create_connection()
    cursor = conn.cursor()

    create_table_query = '''
    CREATE TABLE IF NOT EXISTS folderNames (
        id INTEGER PRIMARY KEY,
        folder_name TEXT NOT NULL
    );
    '''
    cursor.execute(create_table_query)

    conn.commit()
    conn.close()

def insert_data_1():
    conn = create_connection()
    cursor = conn.cursor()

    insert_data_query = '''
    INSERT OR IGNORE INTO folderNames (id, folder_name) VALUES
    (0, 'My Scans'),
    (1, 'All Scans')
    '''
    cursor.execute(insert_data_query)

    conn.commit()
    conn.close()

def insert_data_2():
    conn = create_connection()
    cursor = conn.cursor()
    insert_data_query = '''
    INSERT OR IGNORE INTO folderNames (id, folder_name) VALUES
    (3, 'scan 1'),
    (4, 'scan 2'),
    (5, 'scan 3');
    '''
    cursor.execute(insert_data_query)

    conn.commit()
    conn.close()

def insert_data_to_DB(ID,FolderName):
    conn = create_connection()
    cursor = conn.cursor()

    insert_data_query = f'''
    INSERT OR IGNORE INTO folderNames (id, folder_name) VALUES
    ({ID}, '{FolderName}');
    '''
    cursor.execute(insert_data_query)

    conn.commit()
    conn.close()

def select_all_data():
    conn = create_connection()
    cursor = conn.cursor()

    select_query = 'SELECT * FROM folderNames'
    cursor.execute(select_query)

    rows = cursor.fetchall()

    conn.close()

    return rows

def remove_all_data():
    conn = create_connection()
    cursor = conn.cursor()

    remove_data_query = 'DELETE FROM folderNames'
    cursor.execute(remove_data_query)

    conn.commit()
    conn.close()

def get_last_element_id():
    conn = create_connection()
    cursor = conn.cursor()

    select_last_id_query = 'SELECT MAX(id) FROM folderNames;'
    cursor.execute(select_last_id_query)

    last_id = cursor.fetchone()[0]  # Fetch the value from the result

    conn.close()
    if last_id == None:
        return -1
    return last_id

def insert_folder_data_if_not_exists(id, folder_name):
    conn = create_connection()
    cursor = conn.cursor()

    # Check if the record already exists
    select_query = f'SELECT id FROM folderNames WHERE id={id} OR folder_name="{folder_name}"'
    cursor.execute(select_query)
    existing_record = cursor.fetchone()

    if not existing_record:
        # If the record does not exist, insert it
        insert_data_query = f'''
        INSERT INTO folderNames (id, folder_name) VALUES
        ({id}, '{folder_name}');
        '''
        cursor.execute(insert_data_query)
    else:
        return 1

    conn.commit()
    conn.close()

def get_first_id_and_name():
    conn = create_connection()
    cursor = conn.cursor()

    select_first_id_query = 'SELECT id, folder_name FROM folderNames ORDER BY id LIMIT 1;'
    cursor.execute(select_first_id_query)

    first_record = cursor.fetchone()
    result = {0: None, 1: None}

    if first_record is not None:
        result[0] = first_record[0]
        result[1] = first_record[1]

    conn.close()

    return result


def delete_folder_by_name(folder_name):
    conn = create_connection()
    cursor = conn.cursor()

    # Find the record with the given folder name
    select_query = f'SELECT id FROM folderNames WHERE folder_name="{folder_name}"'
    cursor.execute(select_query)
    record_to_delete = cursor.fetchone()

    if record_to_delete:
        # If the record exists, delete it and any records with the same ID
        delete_query = f'DELETE FROM folderNames WHERE id={record_to_delete[0]} OR folder_name="{folder_name}"'
        cursor.execute(delete_query)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    # create_table()
    # insert_data_1()
    # insert_data_2()
    data = select_all_data()

    for row in data:
        print(f'ID: {row[0]}, Folder Name: {row[1]}')

    # remove_all_data()
    # print(get_last_element_id())
    # print(get_first_id_and_name()[0]," ",get_first_id_and_name()[1])
    # delete_folder_by_name_and_id('Scan 1')


    # insert_folder_data_if_not_exists(10,"scan 10")