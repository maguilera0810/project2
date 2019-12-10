# Project 2

Web Programming with Python and JavaScript

Welcome to Project 2: Chat with Socket IO

the following project is structured as follows:
on static directory  we can find index.js file. This file contains functions related to the socket connection. There
are also a couple of functions which were created to obtain the date in a readable format.

On the other side, on templates directory we have the following:
    - channels.html: this page appears when a channel is selected by some user so he/she can type and submit a message into the channel.
    - index.html: It corresponds to the main page. Here the user is able to create a new channel or to start a private
    chat with an specific user.
    - logged.html: it is an html where the registration of an username is confirmed. This page appears only 1.5 seconds and then the user is redirected to the main page (index.html).
    - noaccess.html: This page is shown when an unaothorized user tries to access to a chat between other two users.
    - private.html: It shows a page which can only be accessed by two users which form part of a private chat.
    - register.html: It is the page which appears at the beginning, if a user enters the page for the first time.

Finally, application.py contains all of the logic on the server side, where the registration of a new user  (if it does not use a username already registered) is performed,
and the new messages which are being submitted by  users, whether on a private chat or an specific channel are being saved here through sockets. 
