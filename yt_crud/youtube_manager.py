import json

def load_data():
    try:
        with open("youtube_db.txt", "r") as file:
            db = json.load(file)
            return db
    except FileNotFoundError:
        return []  
    
def save_data(db):
    with open("youtube_db.txt", "w") as file:
        json.dump(db, file)

def list_videos(videos):
    print("*" * 30)
    print("\n")
    for i, video in enumerate(videos, start=1):
        print(f"{i}. {video['name']}, duration: {video['time']}")
    print("\n")
    print("*" * 30)

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    save_data(videos)

def update_video(videos):
    list_videos(videos)
    
    video_id = int(input("Enter video id to update: "))
    if 1 <= video_id <= len(videos):
        new_name = input("Enter video name: ")
        new_time = input("Enter video time: ")
    
        videos[video_id - 1] = {'name': new_name, 'time': new_time}
        save_data(videos)
        print("Video Updated")
    else: 
        print("Invalid Video Id!")

def delete_video(videos):
    list_videos(videos)
    
    video_id = int(input("Enter video id to delete: "))
    if 1 <= video_id <= len(videos):
        del videos[video_id - 1]
        
        save_data(videos)
        print("Video Deleted")
    else:
        print("Invalid Video Id!")


def search_video(videos):
    video_id = int(input("Enter video id to find: "))
    if 1 <= video_id <= len(videos):
        video = videos[video_id - 1]
        if video:
            print(f"Video Found: NAME - {video['name']}, TIME - {video['time']}")
        else:
            print("Video not found")
    else:
        print("Invalid Video Id!")

def main():
    videos = load_data()
    
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
                list_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                search_video(videos)
            case "6":
                break
            case _:
                print("Invalid Choice")

if __name__ == "__main__":
    main()
    