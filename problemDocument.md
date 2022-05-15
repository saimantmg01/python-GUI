# Problem Documentation

These are some of the problems we ran into while working through our project as a team:

> Issue #1: Having two windows to pass data between them and switch to main window from welcome window
> Solution: Used QtStackedWidget to include two different widgets in same app without exiting it and move from main to welcome page. 

> Issue #2: Issues with signals related with selecting a specific book and perform user choosen actions on it
> Solution: We used QGroupBox to organize selection of books, images and add radio buttons to QButtonGroup to refer to that specific selection of books on which user actions can be performed.

> Issue #3: Removing widgets in book section of app and not updating the GUI
> Solution: Used deletelater() to destroy references and really delete a widget from GUI.

> Issue #4: Using library and history from backend
> Solution: We reorganize code in classes and import it on frontend to use associated functions from backend.
