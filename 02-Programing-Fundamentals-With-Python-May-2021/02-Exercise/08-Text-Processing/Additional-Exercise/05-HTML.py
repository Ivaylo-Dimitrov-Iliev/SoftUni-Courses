title_of_article = input()
content_of_the_article = input()
comment = input()

print(f"<h1>\n    {title_of_article}\n</h1>")
print(f"<article>\n    {content_of_the_article}\n</article>")

while not comment == "end of comments":
    print(f"<div>\n    {comment}\n</div>")
    comment = input()
