def create_youtube_video(title , description):
	videodicti = { "title": title , "description": description , "like": 0, "dislike" : 0, "comments":{}
	}

	
	return videodicti


def like( videodicti ):
	if "like" in videodicti: 
		videodicti['like']+=1
	return videodicti


def dislike( videodicti ):
	if "dislike" in videodicti: 
		videodicti['dislike']+=1
	return videodicti


def add_comment(videodicti, username, comment_text):
	videodicti["comments"]= {username: comment_text}
	return videodicti 



newVideo = create_youtube_video("Y2 summer", "Come and see how is it to be in the Y2 summer!")
like(newVideo)
dislike(newVideo)
add_comment(newVideo, "Hila" , "WOWWWW!")

print(newVideo)

while newVideo["like"] < 495:
	like(newVideo)

print(newVideo)