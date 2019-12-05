import os
from tqdm import tqdm
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pandas as pd
import pickle

# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret.
CLIENT_SECRETS_FILE = "client_secret.json"  # This is the name of your JSON file

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account and requires requests to use an SSL connection.
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'


def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_console()
    return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)


os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
service = get_authenticated_service()

# =============================================================================
# Search Query Initialisation
# =============================================================================
query = input("Ingrese termino a buscar: ")

query_results = service.search().list(
    part='snippet',
    q=query,
    order='relevance',  # You can consider using viewCount
    maxResults=50,
    type='video',  # Channels might appear in search results
    relevanceLanguage='en',
    safeSearch='moderate',
).execute()

# =============================================================================
# Get Video IDs
# =============================================================================
video_id = []
channel = []
video_title = []
video_desc = []
for item in query_results['items']:
    video_id.append(item['id']['videoId'])
    channel.append(item['snippet']['channelTitle'])
    video_title.append(item['snippet']['title'])
    video_desc.append(item['snippet']['description'])

    # =============================================================================
    # Get Comments of Top Videos
    # =============================================================================
    comments_pop = []
    for i, video in enumerate(tqdm(video_id, ncols=100)):
        response = service.commentThreads().list(
            part='snippet',
            videoId=video,
            maxResults=100,  # Only take top 100 comments...
            order='relevance',  # ... ranked on relevance
            textFormat='plainText',
        ).execute()

        comments_temp = []
        for item in response['items']:
            comments_temp.append(item['snippet']['topLevelComment']['snippet']['textDisplay'])
        comments_pop.extend(comments_temp)

output_dict = {
    'Comment': comments_pop
}

output_df = pd.DataFrame(output_dict, columns=output_dict.keys())
csv = output_df.to_csv('csv_comentarios/' + query + '.csv')
