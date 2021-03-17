import os

SUBTITLES_FORMAT = [".srt", ".ass", ".xml", ".vss"]
MOVIES_FORMAT = [".mkv", ".wav", ".mp4"]
subbtitles = list()
movies = list()


for entry in entries_names:
    file_format = os.path.splitext(entry)[1]
    if file_format in SUBTITLES_FORMAT:
        subbtitles.append(entry)
    elif file_format in MOVIES_FORMAT:
        movies.append(entry)


for i in range(len(subbtitles)):
    subbtitle_name = os.path.splitext(subbtitles[i])[0]
    subbtitle_format = os.path.splitext(subbtitles[i])[1]

    movie_name = os.path.splitext(movies[i])[0]

    os.rename(
        path + "\\" + subbtitle_name + subbtitle_format,
        path + "\\" + movie_name + subbtitle_format,
    )
