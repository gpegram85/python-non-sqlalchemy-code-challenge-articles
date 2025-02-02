class Article:
    # Class variable to store all Article instances
    all = []

    def __init__(self, author, magazine, title):
        # Ensure author is an instance of Author
        if not isinstance(author, Author):
            raise AttributeError("Author must be an instance of type Author.")
        self._author = author
        
        # Ensure magazine is an instance of Magazine
        if not isinstance(magazine, Magazine):
            raise AttributeError("Magazine must be an instance of type Magazine.")
        self._magazine = magazine
        
        # Ensure title is a string with length between 5 and 50 characters
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise AttributeError("Title must be a string between 5 and 50 characters inclusive.")
        self._title = title
        
        # Add the new article instance to the class variable `all`
        Article.all.append(self)

    # Property getter for author
    @property
    def author(self):
        return self._author
    
    # Property setter for author with validation
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise AttributeError("Author must be an instance of Author.")
        self._author = value
        
    # Property getter for magazine
    @property
    def magazine(self):
        return self._magazine
    
    # Property setter for magazine with validation
    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise AttributeError("Magazine must be an instance of Magazine.")
        self._magazine = value
    
    # Property getter for title
    @property
    def title(self):
        return self._title
    
    # Property setter for title with validation, ensuring immutability
    @title.setter
    def title(self, value):
        if hasattr(self, "_title"):
            raise AttributeError("Title cannot be changed after instantiation.")
        if not isinstance(value, str) or not (5 <= len(value) <= 50):
            raise AttributeError("Title must be a string between 5 and 50 characters inclusive.")
        self._title = value


class Author:
    # Class variable to store all Author instances
    all = []

    def __init__(self, name):
        # Ensure name is a non-empty string
        if not isinstance(name, str) or not len(name) > 0:
            raise AttributeError("Name must be a string greater than 0 characters.")
        self._name = name
        
        # Add the new author instance to the class variable `all`
        Author.all.append(self)

    # Property getter for name
    @property
    def name(self):
        return self._name
    
    # Property setter for name with validation, ensuring immutability
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not len(value) > 0:
            raise AttributeError("Name must be a string greater than 0 characters.")
        if hasattr(self, "_name"):
            raise AttributeError("Cannot change name after instantiation.")
        self._name = value

    # Get all articles written by this author
    def articles(self):
        return [article for article in Article.all if article.author == self]

    # Get all unique magazines this author has contributed to
    def magazines(self):
        return list({article.magazine for article in self.articles()})

    # Create and return a new article instance linked to this author and given magazine
    def add_article(self, magazine, title):
        if not isinstance(magazine, Magazine):
            raise AttributeError("Magazine must be of type Magazine.")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise AttributeError("Title must be a string between 5 and 50 characters inclusive.")
        return Article(self, magazine, title)

    # Get all unique topic areas (categories) the author has written for
    def topic_areas(self):
        categories = {magazine.category for magazine in self.magazines()}
        return list(categories) if categories else None


class Magazine:
    # Class variable to store all Magazine instances
    all = []

    def __init__(self, name, category):
        # Ensure name is a string with length between 2 and 16 characters
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise AttributeError("Name must be a string between 2 and 16 characters inclusive.")
        self._name = name
        
        # Ensure category is a non-empty string
        if not isinstance(category, str) or not len(category) > 0:
            raise AttributeError("Category must be a string greater than 0 characters.")
        self._category = category
        
        # Add the new magazine instance to the class variable `all`
        Magazine.all.append(self)

    # Property getter for name
    @property
    def name(self):
        return self._name
    
    # Property setter for name with validation
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise AttributeError("Name must be a string between 2 and 16 characters inclusive.")
        self._name = value

    # Property getter for category
    @property
    def category(self):
        return self._category
    
    # Property setter for category with validation
    @category.setter
    def category(self, value):
        if not isinstance(value, str) or not len(value) > 0:
            raise AttributeError("Category must be a string greater than 0 characters.")
        self._category = value

    # Get all articles published in this magazine
    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    # Get all unique contributors to this magazine
    def contributors(self):
        return list({article.author for article in Article.all if article.magazine == self})

    # Get a list of all article titles for this magazine
    def article_titles(self):
        titles = [article.title for article in Article.all if article.magazine == self]
        return titles if titles else None

    # Get authors who have written more than 2 articles for this magazine
    def contributing_authors(self):
        # Create dictionary to track article count for each author
        author_counts = {}

        # Iterate over all Article instances to count contributions for this magazine
        for article in Article.all:
            if article.magazine == self:
                author = article.author
                
                # Check if author is a valid Author instance and update contribution count
                if isinstance(author, Author):
                    author_counts[author] = author_counts.get(author, 0) + 1

        # Filter authors with more than 2 contributions
        contributors = [author for author, count in author_counts.items() if count > 2]
        
        # Return list if non-empty, else return None
        return contributors if contributors else None
