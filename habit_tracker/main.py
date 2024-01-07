import openai

# import requests
#
# USERNAME = "deedadey"
# TOKEN = "Dee.Christ"
#
# PIXELA_URL = "https://pixe.la/v1/users"
# URL2 = "https://pixe.la/@deedadey"
#
# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
#
#
# # response = requests.post(url=PIXELA_URL, json=user_params)
# # print(response.text)
#
# # view_profile = requests.get(url=URL2)
# # print(view_profile.text)
#
# graphs_endpoint = f"{PIXELA_URL}/{USERNAME}/graphs"
#
# graph_config = {
#     "id": "graph01",
#     "name": "100 Days Python",
#     "unit": "days",
#     "type": "int",
#     "color": "shibafu",
# }
#
# headers = {
#     "X-USER-TOKEN": TOKEN,
# }
#
# graph_post = requests.post(url=graphs_endpoint, json=graph_config, headers=headers)
# print(graph_post.text)
#
# pixel_endpoint = f"{graphs_endpoint}/{graph_config['id']}"
#
# pixel_config = {
#     "date": "20231002",
#     "quantity": "10",
# }
#
# # pixel_post = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# # print(pixel_post.text)
#
# changes = {
#     "unit": "hours",
# }
#
# graph_post = requests.put(url=f"{graphs_endpoint}/{graph_config['id']}", json=changes, headers=headers)
#



