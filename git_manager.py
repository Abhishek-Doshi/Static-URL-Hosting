from github import Github
from config import CONFIG

def update_redirect_address(URL=CONFIG["URL"], HOSTED_REPO=CONFIG["HOSTED_REPO"], INDEX_FILE=CONFIG["INDEX_FILE"], ACCESS_TOKEN=CONFIG["ACCESS_TOKEN"]):
    git_hub = Github(ACCESS_TOKEN)
    repo = git_hub.get_user().get_repo(HOSTED_REPO)
    contents = repo.get_contents(INDEX_FILE)
    code = "<script>const path = location.replace('" + URL + "' + String(window.location.hash.replace('#', '')));</script>"
    repo.update_file(contents.path, "Redirect URL updated.", code, contents.sha)