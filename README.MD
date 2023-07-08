PervertGram
===========

PervertGram is a weekend project developed by a cyber-pervert. It provides various functionalities to interact with Instagram user data through an API.

Features
--------

*   Get followers, followings, and matches of a user.
*   Retrieve HD profile pictures of users.
*   Generate heatmaps based on user locations.
*   Fetch photos from specific locations.

Usage
-----

To use PervertGram, follow the steps below:

1.  Install the required dependencies specified in the `Pipfile`.
    
2.  Set up your Instagram credentials in the `config.json` file. Replace the `"username"` and `"pwd"` values with your Instagram username and password, respectively.
    
3.  Start the Flask app by running `app.py` using the following command:
    
    Copy code
    
    `python app.py`
    
    The app will run on `http://localhost:5000` by default.
    
4.  
To access the various functionalities with the victim/username set as "zuck", you can use the following clickable links:

*   **Get followers/followings/matches:**
    
    *   [Followings](http://localhost:5000/followings/zuck) or [API Followings](http://localhost:5000/api/followings/zuck/)
    *   [Followers](http://localhost:5000/followers/zuck) or [API Followers](http://localhost:5000/api/followers/zuck/)
    *   [Matches](http://localhost:5000/match/zuck) or [API Matches](http://localhost:5000/api/match/zuck/)
*   **Get HD profile picture:**
    
    *   [Profile Picture](http://localhost:5000/dp/zuck) or [API Profile Picture](http://localhost:5000/api/dp/zuck)
*   **Draw heatmap from user locations:**
    
    *   [Heatmap](http://localhost:5000/heatmap/zuck)
*   **Get photos from a specific location:**
    
    *   [Location](http://localhost:5000/location/%3Cint:location%3E) or [API Location](http://localhost:5000/api/location/%3Cint:location%3E)
    *   Replace `<int:location>` with the ID of the desired location.
*   **Get people from a specific location:**
    
    *   [Location People](http://localhost:5000/location-people/%3Cint:location%3E) or [API Location People](http://localhost:5000/api/location-people/%3Cint:location%3E)
    *   Replace `<int:location>` with the ID of the desired location.

Please note that these links assume the PervertGram app is running on `http://localhost:5000`. If you are running it on a different host or port, make sure to update the URLs accordingly.

Click on the links to access the respective functionalities with the "zuck" username as the victim.

If you have any further questions, feel free to ask!

File Structure
--------------

The file structure of the project is as follows:

csharpCopy code

`├── LICENSE ├── Pipfile ├── README.md ├── __pycache__ │   ├── app.cpython-311.pyc │   └── interface.cpython-311.pyc ├── app.py ├── config.json ├── images │   ├── 0.png │   ├── 1.png │   └── 2.gif ├── interface.py └── templates     ├── dp.html     ├── followship.html     └── heatmap.html`

The main files and directories in the project are:

*   `app.py`: The main Flask application file.
*   `config.json`: The configuration file to store Instagram credentials.
*   `interface.py`: The module containing the Instagram Private API interface.
*   `templates`: The directory containing HTML templates for rendering views.
*   `images`: The directory to store images used in the project.
*   `Pipfile`: The Pipenv file specifying project dependencies.
*   `README.md`: The project's README file.

Configuration
-------------

Before running the PervertGram app, ensure you set up your Instagram credentials in the `config.json` file. Replace the `"username"` and `"pwd"` values with your Instagram username and password, respectively.

jsonCopy code

`{     "username": "exampleUser",     "pwd": "examplePassword" }`

Make sure to keep your credentials secure and do not share them with others.

Disclaimer
----------

PervertGram is a project developed for educational purposes and personal use only. Use it responsibly and in compliance with Instagram's terms of service. The developers are not responsible for any misuse of this tool.

License
-------

PervertGram is released under the [MIT License](LICENSE).