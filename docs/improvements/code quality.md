# Code Quality
- Config files are more intuitive that command line arguments, which is what the original implementation used.
- Packages allow for reusability, modularity, and encapsulation.
- GhApi is neater and less verbose than interacting with the API via http requests.
- The original main.py file combined request validation and implementation, which made it hard to see what was going on.  My solution separates the two, with validation in automatic tests carried out by GitHub actions, and implementation in the methods of the RepoConfigurer class. 
- Added logging.

## If I had more time
- As it stands, the RepoConfigurer only works with a few of the repo creation options (in fact fewer than the original implementation), e.g. doesn't add a gitignore file.  These could easily be added though as the logic is similar for all of these methods, and GhApi standardises the methods even more than the original implementation
- Set up a dockerfile so that the UKHSA GitHub package can easily be converted into an image to be used for other projects.
- Version release code.

# To Do
- 