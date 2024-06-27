import sqlite3

conn = sqlite3.connect('youtube_sqlite.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )                
''')

def list_videos():
    cursor.execute('SELECT * FROM videos')
    for row in cursor.fetchall():
        print(row)
    
def add_video(name, time):
    cursor.execute('INSERT INTO videos (name, time) VALUES (?, ?)', (name, time))
    conn.commit()

def update_video(id, name, time):
    cursor.execute('UPDATE videos SET name = ?, time = ? WHERE id = ?', (name, time, id))
    conn.commit()

def delete_video(id):
    cursor.execute('DELETE FROM videos WHERE id = ?', (id, ))

def search_video(id):
    cursor.execute('SELECT * FROM videos WHERE id = ?', (id, ))
    result = cursor.fetchone()
    print(result)
    
def main():
    while True:
        print("Youtube Manager")
        print("1. List all Videos")
        print("2. Add Video")
        print("3. Update Video")
        print("4. Delete Video")
        print("5. Search Video")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        match(choice):
            case "1":
                list_videos()
            case "2":
                name = input("Enter Name: ")
                time = input("Enter Duration: ")
                add_video(name, time)
            case "3":
                id = int(input("Enter ID: "))
                name = input("Enter Name: ")
                time = input("Enter Duration: ")
                update_video(id, name, time)
            case "4":
                id = int(input("Enter ID: "))
                delete_video(id)
            case "5":
                id = int(input("Enter ID: "))
                search_video(id)
            case "6":
                break
            case _:
                print("Invalid Choice")

if __name__ == "__main__":
    main()