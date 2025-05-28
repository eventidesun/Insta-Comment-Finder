import instaloader

def find_comment_by_user(post_shortcode, target_username):
    L = instaloader.Instaloader()

    post = instaloader.Post.from_shortcode(L.context, post_shortcode)
    print(f"Looking through comments on: {post.title or post.caption[:50]}")

    matches = []

    for comment in post.get_comments():
        if comment.owner.username.lower() == target_username.lower():
            matches.append({
                "username": comment.owner.username,
                "text": comment.text,
                "date": comment.created_at_utc,
                "id": comment.id,
            })

    if matches:
        print(f"\nFound {len(matches)} comment(s) by @{target_username}:")
        for m in matches:
            print(f"[{m['date']}] {m['username']}: {m['text']}")
    else:
        print(f"\nNo comments found by @{target_username} on this post.")

if __name__ == "__main__":
    shortcode = "" # add the short code here
    target_username = "" # add who's comment you are looking for here
    find_comment_by_user(shortcode, target_username)
