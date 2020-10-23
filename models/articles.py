class Articles:
    """ Articles class to define the articles object """
    def __init__(self, author, title, description, urlToImage, url, publishedAt):
        self.author = author
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.url = url
        self.publishedAt = publishedAt