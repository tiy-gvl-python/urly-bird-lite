Learned about more indepth User Permissions in addition to how to create and navigate a more complex Django Applicaiton.


# URLy Bird

## Description

Create a URL shortener/bookmarking site with Django.

## Objectives

### Learning Objectives

After completing this assignment, you should be able to:

* Extrapolate from current Django projects to build a new project of substantial size and features
* Determine which model field types to use to represent data
* Translate English descriptions of data queries into Django ORM queries
* Make use of Bootstrap and hand-written CSS to style your application
* Select generic views from Django to speed development
* Protect access and choose behavior based on user status

## Details

### Deliverables

* A Git repo called urly-bird containing at least:
  * `README.md` file explaining how to run your project
  * a `requirements.txt` file
  * a Django project

### Requirements

* No PEP8 or Pyflakes warnings or errors

## Normal Mode

Create a Django project for a bookmarking site. Users can save URLs with
a title and an optional description.

Each Bookmark should have a unique code -- something like "x1yrd3a" -- for use
in looking it up later. Create a route like "/b/{code}" that will redirect any
user -- not just logged in users -- to the Bookmark associated with that code.
The route does not have to look just like the example.

When a user -- anonymous or logged in -- uses a Bookmark URL, record that user,
Bookmark, and timestamp. A suggested name for this model is Click, even though
you can navigate to the URL without a click by entering it in your navigation
bar.

The site should have user registration, login, and logout.

On a logged in user's index page, they should see a list of the bookmarks
they've saved in reverse chronological order. The Bookmark links
should use the internal short-code route, not the original URL. From this page,
they should be able to edit and delete bookmarks.

A user's Bookmark page should be public. When viewing a user's Bookmark page
when not that user, the links to edit and delete bookmarks should not show up.

There should also be a page to view all bookmarks for all users in reverse
chronological order, paginated.

These features are restated in the following list:

* Users can create an account, log in, and log out.
* Users can save a URL as a Bookmark with a title and an optional description.
* Users can see all their bookmarks in reverse chronological order.
* Users can edit and delete their own bookmarks.
* Users can see all the bookmarks for another user in reverse chronological order.
* Users can see all the bookmarks for all users in reverse chronological order.
* Users can access a Bookmark through a URL with a short code, allowing them to share bookmarks.
* When a user accesses a Bookmark, the access is recorded with the Bookmark, the user -- or anonymous user -- and the timestamp.

## Additional Resources

* [Hashids](http://hashids.org/python/). These may be useful for creating short URLs.
