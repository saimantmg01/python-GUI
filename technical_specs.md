# Technical Specs

> Details on functionality of each functions and class

# App GUI/ Frontend
## Widgets
- StackedWidget
    - Allows to change screen from Welcome to Main without exiting the window
- Welcome Screen
    - One of two screen which holds welcome sign, input to put user name and submit button to trigger change of screen
        - SubmitButton
            - Change screen from Welcome to Display 
- Display Screen
    - Main screen where functionality of app takes place in
- History Widget
    - Shows the history content from backend
- Action Widget
    - Gives user selection of actions which user can perform
        - Takeout Button - Allows user to take book out of library
        - Return Button - Allows user to return the book to library they took
        - Preview button - Shows description of the book
        - Popup windows - Displays when users has selected an action that does not correspond with the correct function, the three cases are:
            - When the user does not select any book
            - When the user tries to return the book in library section
            - When the user tries to take out the book in user section
- User Widget
    - Holds the name submitted on welcome window as user and records the number of books in a user possession.
- Preview Widget
    - Display the description of the book
- Book Widget
    - Holds the combobox which triggers a change in display based on two following choices:
        - Library Books:
            - Shows all the books in the library available.
                - Books are hold in `QGroupBox` which contains image, text and radiobutton
        - User Books:
            - Shows the book in the possession of the user
                - Books are hold in `QGroupBox` which contains image, text and radiobutton
        

# App Logic/Backend
## Classes
- Library 
    - The library class is a container that holds all of the books in the library.
    - The library data is stored inside of a csv and is parsed by the  `parseLibData` function
    - Users can choose to take out or return books back to the library and those actions are encapulsated in the methods `deleteLibData` and `addLibData`
- History
    - provides a detail account of actions that users have taken with regard to the library
    - The history is stored inside of a csv and is parsed by the  `parseHistoryData` function
    - When a user chooses to take out or return a book, that action is added to the csv by the `adHistoryCSV` function
- Hand
    - A container that stores all the current books that the user has taken out from the library
    - Users can add or remove books from their hand with `addItem` and `removeItem` respectively.
    - The number of books that the user has can also be retrieved by using the `getNumberOfBooks` method.
## Functions
- parseHistoryData
    - parses the history data that is located in `history.csv`
    - contains an account of which user has interacted with the library, what action they chose to take, and what book they interacted with
- parseLibData
    - parses the csv that stores all book information within the library
    - the csv contains information like the book name, an author and the description of the book