# Project 2

Web Programming with Python and JavaScript

Welcome to Project 2: Flack

the following project is structured as follows:
Static directory:
    
    -index.js: file. This file contains functions related to the socket connection. There are also a couple of functions which were created to obtain the date in a readable format.
    
    -css/style2.css: This file contains all styles of mi project
    
    -images: This folder contains all images of the project


Templates directory:

    - channels.html: this page appears when a channel is selected by some user so he/she can type and submit a message into the channel.

    - index.html: It corresponds to the main page. Here the user is able to create a new channel or to start a private
    chat with an specific user.

    - logged.html: it is an html where the registration of an username is confirmed. This page appears only 1.5 seconds and then the user is redirected to the main page (index.html).

    - register.html: It shows a page which can only be accessed by two users which form part of a private chat.


application.py: This file ontains all of the logic on the server side.

Personal touch: As an additional feature, I placed the messages of the current user on the right and the messages of other users on the left, and set a random color for each user when logging in. In addition, I implemented a logout.