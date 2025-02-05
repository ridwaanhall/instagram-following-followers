import json

class InstagramAnalytics:
    def __init__(self, following_file, followers_file):
        self.following = self.load_json(following_file)
        self.followers = self.load_json(followers_file)
        self.following_set = self.extract_usernames(self.following, "relationships_following")
        self.followers_set = self.extract_usernames(self.followers, "followers")

    def load_json(self, file_path):
        with open(file_path, 'r') as file:
            return json.load(file)

    def extract_usernames(self, data, key):
        usernames = set()
        if key == "relationships_following":
            for item in data[key]:
                for user in item["string_list_data"]:
                    usernames.add(user["value"])
        else:
            for item in data:
                for user in item["string_list_data"]:
                    usernames.add(user["value"])
        return usernames

    def count_following(self):
        return len(self.following_set)

    def count_followers(self):
        return len(self.followers_set)

    def count_mutual_follow(self):
        return len(self.following_set & self.followers_set)

    def count_non_follow_back(self):
        return len(self.following_set - self.followers_set)

    def count_not_following_back(self):
        return len(self.followers_set - self.following_set)

    def list_non_follow_back(self):
        return list(self.following_set - self.followers_set)

    def list_not_following_back(self):
        return list(self.followers_set - self.following_set)

    def list_mutual_follow(self):
        return list(self.following_set & self.followers_set)

    def print_analytics(self):
        print(f"Following         : {self.count_following()}")
        print(f"Followers         : {self.count_followers()}")
        print(f"Mutual Follow     : {self.count_mutual_follow()}")
        print(f"Not Following Back: {self.count_non_follow_back()}")
        print(f"Not Followed Back : {self.count_not_following_back()}")
        print('')
        print(f"List of Not Following Back: {self.list_non_follow_back()}")
        print(f"List of Not Followed Back: {self.list_not_following_back()}")
        print(f"List of Mutual Follow: {self.list_mutual_follow()}")

if __name__ == "__main__":
    analytics = InstagramAnalytics('following.json', 'followers_1.json')
    analytics.print_analytics()