import scratchattach as sa
import time

# Replace with your scratch login cookie
cookie = " "

# Login using the cookie
session = sa.login_by_id(cookie)

# Your project ID
my_project_id = 123456789  # replace with your project ID

# get trending studios
trending_studios = session.explore_studios(query="*", mode="trending", language="en", limit=40, offset=0)

# Add your project safely
for studio in trending_studios:
    if studio.open_to_all:
        current_projects = studio.projects()  # get projects already in studio
        if my_project_id in current_projects:
            print(f"⚠️ Project already in '{studio.title}' (ID: {studio.id}), skipping.")
        else:
            print(f"✅ Adding project to '{studio.title}' (ID: {studio.id})...")
            studio.add_project(my_project_id)
    time.sleep(1)